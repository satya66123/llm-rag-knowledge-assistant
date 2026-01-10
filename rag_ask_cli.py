from app.loader import load_txt_documents
from app.chunking import chunk_text
from app.embeddings import FaissEmbeddingStore
from app.prompts import build_context, build_prompt
from app.persistence import save_faiss_store, load_faiss_store


def build_store_from_docs():
    docs = load_txt_documents("data/sample_docs")

    all_chunks = []
    chunk_counter = 0
    for doc in docs:
        chunks = chunk_text(doc["text"], chunk_size=450, overlap=80)
        for c in chunks:
            chunk_counter += 1
            all_chunks.append({
                "chunk_id": f"chunk_{chunk_counter}",
                "doc_id": doc["doc_id"],
                "source": doc["source"],
                "text": c
            })

    store = FaissEmbeddingStore()
    store.add_chunks(all_chunks)
    return store


def main():
    store = FaissEmbeddingStore()

    # Load existing index if available
    try:
        load_faiss_store(store)
        print("✅ Loaded FAISS index from storage/")
    except Exception:
        print("ℹ️ No saved index found. Building a new one...")
        store = build_store_from_docs()
        save_faiss_store(store)
        print("✅ Built and saved FAISS index to storage/")

    print("\n🧠 Offline RAG CLI is ready.")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("❓ Question: ").strip()
        if question.lower() in {"exit", "quit"}:
            break

        retrieved = store.search(question, top_k=3)
        context = build_context(retrieved)
        prompt = build_prompt(question, context)

        print("\n📌 Retrieved Sources:")
        for r in retrieved:
            print(f"- {r['doc_id']} | {r['chunk_id']} | distance={r.get('distance', r.get('score')):.4f}")

        print("\n🧾 Final Prompt (LLM-ready):")
        print(prompt)
        print("\n" + "=" * 90 + "\n")


if __name__ == "__main__":
    main()
