from pathlib import Path
from typing import List, Dict


def load_txt_documents(folder_path: str) -> List[Dict]:
    """
    Loads all .txt files from a folder and returns a list of docs.
    Each doc has: doc_id, source, text
    """
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    txt_files = sorted(folder.glob("*.txt"))
    if not txt_files:
        raise ValueError(f"No .txt files found in: {folder_path}")

    docs = []
    for i, file_path in enumerate(txt_files, start=1):
        text = file_path.read_text(encoding="utf-8").strip()
        if not text:
            continue

        docs.append({
            "doc_id": f"doc_{i}",
            "source": str(file_path),
            "text": text
        })

    return docs
