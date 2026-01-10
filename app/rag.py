from typing import Dict, Any
from app.prompts import build_context, build_prompt
from app.llm import generate_answer


def answer_with_rag(store, question: str, top_k: int = 3) -> Dict[str, Any]:
    retrieved = store.search(question, top_k=top_k)
    context = build_context(retrieved)
    prompt = build_prompt(question, context)
    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": retrieved
    }
