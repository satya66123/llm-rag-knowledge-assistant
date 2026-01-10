from typing import List, Dict


def build_context(retrieved_chunks: List[Dict]) -> str:
    """
    Convert retrieved chunks into a structured context for an LLM.
    """
    blocks = []
    for i, c in enumerate(retrieved_chunks, start=1):
        blocks.append(
            f"[CONTEXT {i}]\n"
            f"source: {c['source']}\n"
            f"doc_id: {c['doc_id']}\n"
            f"chunk_id: {c['chunk_id']}\n"
            f"text:\n{c['text']}\n"
        )

    return "\n---\n".join(blocks)


def build_prompt(question: str, context: str) -> str:
    """
    Final prompt template.
    """
    return f"""
You are a helpful assistant.

Answer the QUESTION using ONLY the CONTEXT below.
If the answer is not in the context, say: "I don't know based on the provided context."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
""".strip()
