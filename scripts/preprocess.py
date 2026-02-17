import json

INPUT_FILE = "data/raw_posts.json"
OUTPUT_FILE = "data/processed_posts.json"


def count_lines(text):
    return len(text.strip().split("\n"))


def preprocess():

    with open(INPUT_FILE, encoding="utf-8") as f:
        posts = json.load(f)

    for post in posts:
        post["line_count"] = count_lines(post["text"])

        # normalize language
        post["language"] = post["language"].capitalize()

        # ensure tags exist
        if "tags" not in post or not post["tags"]:
            post["tags"] = ["General"]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    print("✅ Preprocessing done. Saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    preprocess()
