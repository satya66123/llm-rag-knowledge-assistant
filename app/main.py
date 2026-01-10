from contextlib import asynccontextmanager
from typing import List, Dict, Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.embeddings import FaissEmbeddingStore
from app.persistence import load_faiss_store
from app.rag import answer_with_rag
from fastapi import Query



# Global FAISS store loaded once at startup
store = FaissEmbeddingStore()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Lifespan event handler:
    - Startup: load FAISS index + metadata once
    - Shutdown: (optional) cleanup
    """
    load_faiss_store(store)
    yield
    # shutdown cleanup (if needed)


app = FastAPI(
    title="LLM RAG Knowledge Assistant",
    version="1.0.0",
    lifespan=lifespan
)


class AskRequest(BaseModel):
    question: str = Field(..., min_length=3, description="User question")
    top_k: int = Field(default=3, ge=1, le=10, description="Number of chunks to retrieve")


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: List[Dict[str, Any]]

@app.get("/")
def root():
    return {"message": "RAG API is running. Use /docs to test."}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ask")
def ask_get(q: str = Query(..., min_length=3), top_k: int = 3):
    """
    Browser friendly: /ask?q=What%20is%20RAG&top_k=3
    """
    result = answer_with_rag(store, q, top_k=top_k)
    return result


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    """
    RAG endpoint:
    - retrieves top_k chunks from FAISS
    - builds context/prompt
    - calls OpenAI
    - returns answer + sources
    """
    result = answer_with_rag(store, req.question, top_k=req.top_k)
    return result
