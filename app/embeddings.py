from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

class EmbeddingStore:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = None
        self.texts = []

    def add_documents(self, documents: list[str]):
        embeddings = self.model.encode(documents)

        # FAISS requires float32
        embeddings = np.array(embeddings).astype("float32")
        dimension = embeddings.shape[1]

        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)

        # noinspection PyArgumentList
        self.index.add(embeddings)
        self.texts.extend(documents)

    def search(self, query: str, top_k: int = 3):
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])

        return results
