import os
from openai import OpenAI


def generate_answer(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    Calls OpenAI to generate final answer from prompt.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    client = OpenAI(api_key=api_key)

    # noinspection PyTypeChecker
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return resp.choices[0].message.content.strip()
