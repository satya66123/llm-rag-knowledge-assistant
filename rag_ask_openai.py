from app.embeddings import FaissEmbeddingStore
from app.persistence import load_faiss_store
from app.rag import answer_with_rag
import os
print("KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))



def main():
    store = FaissEmbeddingStore()
    load_faiss_store(store)

    q = input("❓ Ask question: ").strip()
    result = answer_with_rag(store, q, top_k=3)

    print("\n✅ ANSWER:\n")
    print(result["answer"])

    print("\n📌 SOURCES USED:\n")
    for s in result["sources"]:
        print(f"- {s['source']} | {s['chunk_id']} | dist={s.get('distance', s.get('score')):.4f}")


if __name__ == "__main__":
    main()
