from fastapi import FastAPI
from app.services.vector_store import init_vector_store
from app.routers import query

app = FastAPI(title="Call Center RAG Assistant")

init_vector_store()

app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
def root():
    return {"message": "Call Center RAG Assistant çalışıyor!"}