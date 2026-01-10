# llm-rag-knowledge-assistant

## 🤖 LLM RAG Knowledge Assistant (End-to-End Project)

This repository contains a step-by-step implementation of a **Retrieval-Augmented Generation (RAG)** system built from scratch using Python.

✅ Built incrementally like real AI engineers:
- first build retrieval foundation (embeddings + vector search)
- then build chunk-based retrieval
- then build context + prompt packaging
- then integrate OpenAI
- then expose the system via FastAPI + Streamlit Chat UI

---

# ✅ Progress Timeline (Day-wise)

## 📅 Day 1 — FAISS Embeddings Pipeline ✅

### 🎯 Goal
Build the **core semantic memory layer**, which is the foundation of every RAG system.

### ✅ Implemented
- ✅ Python project setup (clean structure)
- ✅ SentenceTransformer model download + load
- ✅ Text embedding generation
- ✅ FAISS index creation (vector database behavior)
- ✅ Semantic search working end-to-end

### ✅ Output Verified
- Query embeddings generated
- Top relevant sentence retrieved
- No hidden errors (exit code 0)

### 📄 Script
Run:
```bash
python text_embeddings.py
📅 Day 2 — Document Loading + Chunking + Retrieval ✅
🎯 Goal
Move from toy examples to a real RAG retriever, by embedding & searching chunks (not full documents).

✅ Implemented
✅ Load .txt documents from data/sample_docs/

✅ Document loader (app/loader.py)

✅ Chunking with overlap (app/chunking.py)

✅ Embed each chunk

✅ Store chunk metadata:

chunk_id

doc_id

source

text

✅ Retrieve Top-K relevant chunks

✅ Output Verified
Loaded 3 docs

Created multiple chunks

Query like "What is RAG?" returns correct chunk from RAG document

📄 Script
Run:
python rag_retrieval_day2.py

📅 Day 3 — FULL SYSTEM COMPLETION (4 Parts) ✅✅✅✅
Day 3 is the final sprint day where the project was completed to 100%.

✅ Day 3 — Part 1: Context Builder + Prompt Builder ✅
🎯 Goal
Convert raw retrieved chunks into an LLM-ready context pack, and build a clean instruction prompt.

✅ Implemented
📄 app/prompts.py

Includes:

✅ build_context(retrieved_chunks)

formats chunks into structured context

includes source/doc/chunk ids for traceability

✅ build_prompt(question, context)

prompt template that forces grounded answer:

“Answer using ONLY the provided context”

If not in context → “I don’t know”

✅ Why This Is Important
This is what separates real RAG from just semantic search.
It ensures:
✅ grounded answers
✅ reduced hallucinations
✅ source traceability

✅ Day 3 — Part 2: Persistence (Save/Load FAISS Index) ✅
🎯 Goal
Make the project production-ready by avoiding re-embedding every run.

✅ Implemented
📄 app/persistence.py

✅ Save FAISS index to disk (faiss.index)

✅ Save metadata as JSON (metadata.json)

✅ Load index + metadata on startup

✅ Output Verified
First run builds index and saves

Future runs load instantly from disk

✅ Day 3 — Part 3: Offline RAG Ask CLI Pipeline ✅
🎯 Goal
Create a full offline RAG pipeline:

Question → Retrieval → Context → Prompt

✅ Implemented
📄 rag_ask_cli.py

Features:

✅ Asks question in terminal

✅ Retrieves top-k chunks

✅ Builds context pack

✅ Prints final prompt (LLM-ready)

✅ Shows sources (doc/chunk ids)

✅ Why This Matters
This proves the pipeline is correct even before OpenAI integration.

✅ Day 3 — Part 4: OpenAI + FastAPI + Streamlit UI (100% Completion) ✅
🎯 Goal
Complete a real usable RAG product:

Question → RAG retrieval → OpenAI answer → API response → Chat UI

✅ Implemented
✅ OpenAI LLM Answering
📄 app/llm.py

calls OpenAI API

returns grounded answer

📄 app/rag.py

full RAG function:

retrieve chunks

build context

build prompt

call OpenAI

return answer + sources

✅ FastAPI Backend
📄 app/main.py

Endpoints:

✅ GET /health

✅ POST /ask

Response includes:

answer

sources used (doc/chunk ids + text)

Swagger docs:

✅ /docs

✅ Streamlit Chat UI
📄 ui_streamlit.py

UI Features:

✅ Chat-style interface

✅ Sidebar controls:

top_k

show sources toggle

show full source text toggle

enable chat memory toggle

✅ Clear chat button

✅ Displays answer + expandable sources

📂 Final Project Structure
text
Copy code
llm-rag-knowledge-assistant/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── chunking.py
│   ├── prompts.py
│   ├── persistence.py
│   ├── llm.py
│   ├── rag.py
│   └── main.py
│
├── data/
│   └── sample_docs/
│       ├── doc1.txt
│       ├── doc2.txt
│       └── doc3.txt
│
├── storage/
│   ├── faiss.index
│   └── metadata.json
│
├── text_embeddings.py
├── rag_retrieval_day2.py
├── rag_ask_cli.py
├── rag_ask_openai.py
├── ui_streamlit.py
│
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Setup & Installation
1) Install dependencies

pip install -r requirements.txt
🔐 Environment Variable
Set your OpenAI key:

✅ PowerShell (temporary for session)
powershell
Copy code
$env:OPENAI_API_KEY="your_api_key_here"
▶️ Run Instructions
✅ Run FastAPI Server

uvicorn app.main:app --reload
Swagger docs: http://127.0.0.1:8000/docs

Health check: http://127.0.0.1:8000/health

✅ Run Streamlit UI
(keep FastAPI running in another terminal)


streamlit run ui_streamlit.py
UI will open at:

http://127.0.0.1:8501

🏆 Final Outcome
✅ A complete end-to-end RAG Chat Assistant system:

chunk-based retrieval with FAISS

grounded OpenAI answering

FastAPI backend

Streamlit chat interface

sources shown for transparency

🧑‍💻 Author: satya66123 -satyasrinath653512@gmail.com
Built using a disciplined, real engineering approach (Day-wise incremental development).

---

If you want, I can also generate:
✅ **README with screenshots section**  
✅ A polished **“Project Demo” section**  
✅ A final **LinkedIn post** with Day 1/2/3 breakdown + GitHub link