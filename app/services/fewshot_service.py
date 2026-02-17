import pandas as pd
import json

class FewShotService:
    def __init__(self, file_path="data/processed_posts.json"):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)

        self.df = pd.json_normalize(posts)
        self.df["length"] = self.df["line_count"].apply(self.categorize_length)

        all_tags = self.df["tags"].sum()
        self.unique_tags = list(set(all_tags))

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif line_count <= 10:
            return "Medium"
        return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_examples(self, length, language, tag):
        df = self.df[
            (self.df["length"] == length) &
            (self.df["language"] == language) &
            (self.df["tags"].apply(lambda t: tag in t))
        ]
        return df.to_dict(orient="records")
