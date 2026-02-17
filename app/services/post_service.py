from app.services.llm_service import get_llm
from app.services.fewshot_service import FewShotService
from app.prompts.post_prompt import build_prompt

class PostService:

    def __init__(self):
        self.llm = get_llm()
        self.fs = FewShotService()

    def get_tags(self):
        return self.fs.get_tags()

    def generate(self, tag, length, language, tone, hooks):

        examples = self.fs.get_examples(length, language, tag)

        prompt = build_prompt(
            tag=tag,
            length=length,
            language=language,
            tone=tone,
            include_hooks=hooks,
            examples=examples
        )

        response = self.llm.invoke(prompt)
        return response.content
