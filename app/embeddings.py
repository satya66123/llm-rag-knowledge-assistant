from typing import List, Dict
import faiss
#import numpy as np
from sentence_transformers import SentenceTransformer


class FaissEmbeddingStore:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None

        # Stores chunk metadata by position in FAISS index
        self.chunk_metadata: List[Dict] = []

    def add_chunks(self, chunks: List[Dict]):
        """
        chunks: List of dicts
        Each dict: {chunk_id, doc_id, source, text}
        """
        texts = [c["text"] for c in chunks]
        embeddings = self.model.encode(texts, convert_to_numpy=True)

        embeddings = embeddings.astype("float32")
        dim = embeddings.shape[1]

        if self.index is None:
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(embeddings)

        # Save metadata aligned with embeddings
        self.chunk_metadata.extend(chunks)

    def search(self, query: str, top_k: int = 3):
        if self.index is None:
            raise ValueError("FAISS index not initialized. Add chunks first.")

        query_emb = self.model.encode([query], convert_to_numpy=True).astype("float32")
        distances, indices = self.index.search(query_emb, top_k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx == -1:
                continue
            meta = self.chunk_metadata[idx]
            results.append({
                "score": float(dist),
                "chunk_id": meta["chunk_id"],
                "doc_id": meta["doc_id"],
                "source": meta["source"],
                "text": meta["text"]
            })

        return results
