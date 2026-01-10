import json
from pathlib import Path
import faiss


def save_faiss_store(store, folder="storage"):
    """
    Saves FAISS index + chunk metadata to disk.
    """
    Path(folder).mkdir(parents=True, exist_ok=True)

    if store.index is None:
        raise ValueError("No FAISS index found to save.")

    faiss.write_index(store.index, str(Path(folder) / "faiss.index"))

    with open(Path(folder) / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(store.chunk_metadata, f, ensure_ascii=False, indent=2)


def load_faiss_store(store, folder="storage"):
    """
    Loads FAISS index + chunk metadata from disk.
    """
    index_path = Path(folder) / "faiss.index"
    meta_path = Path(folder) / "metadata.json"

    if not index_path.exists() or not meta_path.exists():
        raise FileNotFoundError("Saved FAISS index / metadata not found.")

    store.index = faiss.read_index(str(index_path))

    with open(meta_path, "r", encoding="utf-8") as f:
        store.chunk_metadata = json.load(f)
