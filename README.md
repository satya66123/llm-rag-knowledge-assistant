# llm-rag-knowledge-assistant 🤖

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)](#)
[![FAISS](https://img.shields.io/badge/FAISS-VectorSearch-orange.svg)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A complete **Retrieval-Augmented Generation (RAG)** system built from scratch using Python.

This project implements:
✅ semantic vector retrieval (FAISS)  
✅ chunk-based document search  
✅ grounded answer generation using OpenAI  
✅ FastAPI backend API  
✅ Streamlit chat UI (ChatGPT-style)  
✅ sources included for transparency  

---

## 🚀 Features

- **Vector Search (FAISS)**
  - Fast semantic similarity search over embeddings

- **Chunk-Based Retrieval**
  - Documents are chunked with overlap for better retrieval accuracy

- **Grounded LLM Answering**
  - Answer generated using retrieved context
  - Includes sources (`doc_id`, `chunk_id`, `source`, `text`)

- **Persistence**
  - Stores FAISS index + metadata to disk (`storage/`) for quick restart

- **FastAPI Backend**
  - `GET /health`
  - `POST /ask`

- **Streamlit Chat UI**
  - Chat interface for interaction
  - Sidebar controls: top_k, show sources, show source text, chat memory

---

## 📂 Project Structure

```text
llm-rag-knowledge-assistant/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── embeddings.py         # Embedding + FAISS vector index
│   ├── loader.py             # Loads .txt documents
│   ├── chunking.py           # Chunking with overlap
│   ├── prompts.py            # Context builder + prompt template
│   ├── persistence.py        # Save/load FAISS index + metadata
│   ├── llm.py                # OpenAI answering
│   ├── rag.py                # RAG orchestration pipeline
│   └── main.py               # FastAPI app
│
├── data/
│   └── sample_docs/          # Knowledge base documents
│       ├── doc1.txt
│       ├── doc2.txt
│       └── doc3.txt
│
├── storage/
│   ├── faiss.index
│   └── metadata.json
│
├── ui_streamlit.py           # Streamlit chat UI
├── requirements.txt
├── planner.txt
├── LICENSE
└── README.md
⚙️ Installation
1) Create virtual environment (recommended)
bash
Copy code
python -m venv venv
Activate:

Windows:

bash
Copy code
venv\Scripts\activate
Linux/Mac:

bash
Copy code
source venv/bin/activate
2) Install dependencies
bash
Copy code
pip install -r requirements.txt
🔐 Environment Variables
This project requires an OpenAI API key.

✅ Windows PowerShell (temporary)
powershell
Copy code
$env:OPENAI_API_KEY="your_api_key_here"
⚠️ Never hardcode your API key in code files.
⚠️ Do not commit secrets to GitHub.

▶️ Run the Application
✅ 1) Start FastAPI backend
bash
Copy code
uvicorn app.main:app --reload
FastAPI runs at:

http://127.0.0.1:8000

Swagger API docs:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health

✅ 2) Start Streamlit Chat UI
Open a second terminal:

bash
Copy code
streamlit run ui_streamlit.py
Streamlit UI runs at:

http://127.0.0.1:8501

✅ API Usage
POST /ask
Request

json
Copy code
{
  "question": "What is RAG?",
  "top_k": 3
}
Response
Returns:

answer (OpenAI output)

sources (chunks retrieved from FAISS)

🧪 Notes / Troubleshooting
1) /ask gives Method Not Allowed
That means you opened /ask directly in browser (GET).
✅ Use POST /ask via Swagger /docs or Streamlit UI.

2) AuthenticationError 401
API key not set or invalid.
✅ Ensure OPENAI_API_KEY environment variable is configured.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

👤 Author
Satyasrinath
GitHub: @satya66123
Email: satyasrinath653512@gmail.com