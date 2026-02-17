def build_prompt(tag, length, language, tone, include_hooks, examples):

    length_map = {
        "Short": "1-5 lines",
        "Medium": "6-10 lines",
        "Long": "11-15 lines"
    }

    prompt = f"""
You are an expert LinkedIn ghostwriter.

Write a high-quality LinkedIn post.

TOPIC: {tag}
LENGTH: {length_map[length]}
LANGUAGE: {language}
TONE: {tone}

RULES:
- No preamble
- Start with a strong hook
- Clear structure
- Add spacing between lines
- End with CTA or thought-provoking question
"""

    if language == "Hinglish":
        prompt += "\nWrite Hindi+English mix but script must be English."

    if include_hooks:
        prompt += """
Also generate:
1) 3 hook options
2) Final post
Format clearly.
"""

    if examples:
        prompt += "\n\nMatch writing style similar to examples:\n"

        for i, ex in enumerate(examples[:2]):
            prompt += f"\nExample {i+1}:\n{ex['text']}\n"

    return prompt
