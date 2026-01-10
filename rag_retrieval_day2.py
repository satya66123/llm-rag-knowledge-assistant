from app.loader import load_txt_documents
from app.chunking import chunk_text
from app.embeddings import FaissEmbeddingStore


def main():
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

    print(f"✅ Loaded {len(docs)} documents")
    print(f"✅ Created {len(all_chunks)} chunks")

    store = FaissEmbeddingStore()
    store.add_chunks(all_chunks)

    query = "What is RAG?"
    results = store.search(query, top_k=3)

    print("\n🔎 Query:", query)
    print("\nTop Results:\n")

    for i, r in enumerate(results, start=1):
        print(f"--- Result {i} ---")
        print("Doc:", r["doc_id"])
        print("Chunk:", r["chunk_id"])
        print("Source:", r["source"])
        print("Score:", r["score"])
        print("Text:", r["text"][:400], "...")
        print()

    print("✅ Day 2 retrieval pipeline working")


if __name__ == "__main__":
    main()
