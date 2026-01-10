# llm-rag-knowledge-assistant

## 🤖 LLM RAG Knowledge Assistant

A complete **Retrieval-Augmented Generation (RAG)** system built from scratch using Python.

This project supports:
- ✅ Document ingestion from local text files
- ✅ Chunking with overlap
- ✅ Embedding generation using SentenceTransformers
- ✅ Vector similarity search using FAISS
- ✅ Grounded answer generation using OpenAI
- ✅ FastAPI backend API (`/ask`)
- ✅ Streamlit Chat UI with sources and controls

---

## 🚀 Features

- **Vector Search (FAISS)**
  - Semantic similarity search over chunk embeddings.

- **Chunk-Based Retrieval**
  - Retrieval works on small chunks (not full documents) for higher relevance.

- **Grounded Answering**
  - The assistant answers using only retrieved context.
  - Returns **sources used** for transparency.

- **Persistence**
  - Saves FAISS index and metadata to disk for faster restarts.

- **FastAPI Backend**
  - `/health` and `/ask` endpoints.

- **Streamlit Chat UI**
  - Chat-style interface with sidebar controls.

---

## 📂 Project Structure

```text
llm-rag-knowledge-assistant/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── embeddings.py         # FAISS embedding store
│   ├── loader.py             # Load .txt documents
│   ├── chunking.py           # Text chunking with overlap
│   ├── prompts.py            # Context builder + prompt template
│   ├── persistence.py        # Save/load FAISS index + metadata
│   ├── llm.py                # OpenAI integration
│   ├── rag.py                # RAG orchestration
│   └── main.py               # FastAPI backend app⚙️ Setup
1) Install dependencies
pip install -r requirements.txt

🔐 Environment Variables

This project requires an OpenAI API key.

✅ Windows PowerShell (temporary session)
$env:OPENAI_API_KEY="your_api_key_here"

▶️ Run the Application
1) Start FastAPI backend
uvicorn app.main:app --reload


Backend runs at:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health

2) Start Streamlit Chat UI (recommended)

In a new terminal:

streamlit run ui_streamlit.py


Streamlit runs at:

http://127.0.0.1:8501

✅ API Usage
POST /ask

Request Body

{
  "question": "What is RAG?",
  "top_k": 3
}


Response
Returns:

answer

sources (doc_id, chunk_id, source path, chunk text)

🏆 Result

You get a complete portfolio-ready RAG assistant:

✅ Retrieval (FAISS)
✅ Grounded LLM answering (OpenAI)
✅ Sources included
✅ API-ready backend
✅ Chat UI ready for demo

🧑‍💻 Author

Built using a disciplined production-style engineering approach.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.
See the [`LICENSE`](LICENSE) file for details.

│
├── data/
│   └── sample_docs/          # Your knowledge base
│       ├── doc1.txt
│       ├── doc2.txt
│       └── doc3.txt
│
├── storage/
│   ├── faiss.index
│   └── metadata.json
│
├── ui_streamlit.py           # Streamlit Chat UI
├── requirements.txt
├── planner.txt
└── README.md
⚙️ Setup
1) Install dependencies
pip install -r requirements.txt

🔐 Environment Variables

This project requires an OpenAI API key.

✅ Windows PowerShell (temporary session)
$env:OPENAI_API_KEY="your_api_key_here"

▶️ Run the Application
1) Start FastAPI backend
uvicorn app.main:app --reload


Backend runs at:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health

2) Start Streamlit Chat UI (recommended)

In a new terminal:

streamlit run ui_streamlit.py


Streamlit runs at:

http://127.0.0.1:8501

✅ API Usage
POST /ask

Request Body

{
  "question": "What is RAG?",
  "top_k": 3
}


Response
Returns:

answer

sources (doc_id, chunk_id, source path, chunk text)

🏆 Result

You get a complete portfolio-ready RAG assistant:

✅ Retrieval (FAISS)
✅ Grounded LLM answering (OpenAI)
✅ Sources included
✅ API-ready backend
✅ Chat UI ready for demo

🧑‍💻 Author

Built using a disciplined production-style engineering approach.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.
See the [`LICENSE`](LICENSE) file for details.
