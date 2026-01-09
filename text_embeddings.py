from app.embeddings import EmbeddingStore

store = EmbeddingStore()

docs = [
    "RAG combines retrieval with generation.",
    "FAISS is used for vector similarity search.",
    "LLMs can hallucinate without grounding."
]

store.add_documents(docs)

results = store.search("What is RAG?")
print(results)
