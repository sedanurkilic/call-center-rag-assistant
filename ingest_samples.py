from data.sample_docs import SAMPLE_DOCUMENTS
from app.services.vector_store import add_document

for i, doc in enumerate(SAMPLE_DOCUMENTS):
    doc_id = f"doc_{i}"
    add_document(
        doc_id=doc_id,
        text=doc["content"],
        metadata={"title": doc["title"], "category": doc["category"]}
    )
    print(f"Yüklendi: {doc['title']}")

print("\nTüm dokümanlar ChromaDB'ye eklendi.")