from app.services.vector_store import search_documents
from app.services.llm_service import generate_answer

question = "What is the refund period?"

print(f"Soru: {question}")

results = search_documents(question, top_k=2)
chunks = results["documents"][0]

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk[:100]}...")

answer = generate_answer(question, chunks)
print(f"💬 Cevap: {answer}")