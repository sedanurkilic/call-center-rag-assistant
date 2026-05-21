import chromadb
from sentence_transformers import SentenceTransformer
from app.config import GEMINI_API_KEY

# Embedding modeli — metni vektöre çevirir
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB — vektörleri saklar (yerel, dosyaya yazar)
chroma_client = chromadb.PersistentClient(path="./data/chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")


def init_vector_store():
    """Uygulama başlarken çağrılır, bağlantıyı doğrular."""
    print(f"ChromaDB hazır. Koleksiyondaki doküman sayısı: {collection.count()}")


def embed_text(text: str) -> list[float]:
    """Metni vektöre çevirir."""
    return embedding_model.encode(text).tolist()


def add_document(doc_id: str, text: str, metadata: dict):
    """Dokümanı ChromaDB'ye ekler."""
    vector = embed_text(text)
    collection.add(
        ids=[doc_id],
        embeddings=[vector],
        documents=[text],
        metadatas=[metadata]
    )


def search_documents(query: str, top_k: int = 3) -> list[dict]:
    """Soruya en yakın dokümanları getirir."""
    query_vector = embed_text(query)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )
    return results