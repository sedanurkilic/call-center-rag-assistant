from fastapi import APIRouter
from app.services.vector_store import search_documents
from app.services.llm_service import generate_answer

router = APIRouter()

@router.post("/ask")
def ask_question(question: str):
    chunks_result = search_documents(question, top_k=3)
    chunks = chunks_result["documents"][0]
    answer = generate_answer(question, chunks)
    return {
        "question": question,
        "answer": answer,
        "sources": chunks_result["metadatas"][0]
    }