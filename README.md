# Call Center RAG Assistant with FastAPI, Docker and Vector Search

A production-style **Retrieval-Augmented Generation (RAG)** backend designed for call center agents. The system retrieves relevant policy documents and generates context-aware answers using semantic vector search and a local LLM.

---

## 🚀 Features

- 📄 **Document Ingestion** — Load policy/FAQ documents into the vector knowledge base
- 🔍 **Semantic Vector Search** — ChromaDB-powered similarity search over embedded documents
- 🤖 **LLM Response Generation** — Context-aware answers grounded in retrieved documents (Ollama / Gemini API)
- ⚡ **FastAPI Backend** — Lightweight, async REST API with auto-generated Swagger docs
- 🐳 **Docker Support** — Fully containerized for consistent deployment

---

## 🏗️ Architecture

```
User Question
     │
     ▼
[FastAPI /query/ask]
     │
     ▼
[Embedding Model]        ← sentence-transformers (all-MiniLM-L6-v2)
     │
     ▼
[ChromaDB Vector Search] ← finds top-k similar document chunks
     │
     ▼
[Ollama LLM]             ← llama3.2 running locally
     │
     ▼
Context-aware Answer
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| API Framework | FastAPI |
| Vector Database | ChromaDB |
| Embedding Model | sentence-transformers (all-MiniLM-L6-v2) |
| LLM | Ollama (llama3.2) / Gemini API |
| Containerization | Docker |
| Language | Python 3.11+ |

---

## 📁 Project Structure

```
call-center-rag-assistant/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Environment config
│   ├── routers/
│   │   └── query.py         # /query/ask endpoint
│   ├── services/
│   │   ├── vector_store.py  # ChromaDB + embedding logic
│   │   └── llm_service.py   # Ollama LLM integration
│   └── models/
├── data/
│   └── sample_docs.py       # Sample call center documents
├── tests/                   # (in progress)
├── ingest_samples.py        # Script to load docs into ChromaDB
├── Dockerfile
├── requirements.txt
└── .env                     # API keys (not committed)
```

---

## ⚙️ Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/sedanurkilic/call-center-rag-assistant.git
cd call-center-rag-assistant
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
# Add your GEMINI_API_KEY if using Gemini instead of Ollama
```

### 5. Install and start Ollama

```bash
# Download from https://ollama.com
ollama pull llama3.2
```

### 6. Ingest sample documents

```bash
python ingest_samples.py
```

### 7. Run the API

```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`
Swagger docs at `http://localhost:8000/docs`

---

## 🐳 Run with Docker

```bash
docker build -t call-center-rag-assistant .
docker run -p 8000:8000 call-center-rag-assistant
```

---

## 📡 API Endpoints

### `POST /query/ask`

Ask a question and get a context-aware answer from the knowledge base.

**Request:**
```json
{
  "question": "What is the refund policy?"
}
```

**Response:**
```json
{
  "question": "What is the refund policy?",
  "answer": "Customers may request a full refund within 30 days of purchase...",
  "sources": [
    {"title": "Refund Policy", "category": "billing"},
    {"title": "Subscription Cancellation", "category": "subscription"}
  ]
}
```

---

## 🗺️ Roadmap

- [ ] `POST /documents/ingest` — Upload new documents via API
- [ ] `GET /documents` — List all documents in the knowledge base
- [ ] `DELETE /documents/{id}` — Remove a document
- [ ] Unit tests with pytest
- [ ] docker-compose with Ollama service
- [ ] Streaming responses via WebSocket
- [ ] Gemini API as alternative LLM backend
