from typing import List


def chunk_text(text: str, chunk_size: int = 450, overlap: int = 80) -> List[str]:
    """
    Splits text into overlapping chunks for RAG retrieval.
    """
    text = text.strip()
    if not text:
        return []

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
