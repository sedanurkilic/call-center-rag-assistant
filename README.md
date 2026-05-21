# Call Center RAG Assistant
### FastAPI · ChromaDB · Vector Search · Local LLM (Ollama) · Docker

A production-style **Retrieval-Augmented Generation (RAG)** backend designed for call center agents. The system retrieves relevant policy documents and generates context-aware, hallucination-resistant answers using semantic vector search and a locally-running LLM.

> **LLM Backend:** This project uses **Ollama (llama3.2)** running locally by default — no API key or internet required for inference. The architecture is designed to be LLM-agnostic; swapping to **Gemini API** or **OpenAI** requires only changing the `llm_service.py` module.

---

## 🚀 Features

- 📄 **Document Ingestion** — Load policy/FAQ documents into the vector knowledge base
- 🔍 **Semantic Vector Search** — ChromaDB-powered similarity search over embedded documents
- 🤖 **Local LLM Inference** — Context-aware answers via Ollama (llama3.2) — runs fully offline
- ⚡ **FastAPI Backend** — Lightweight async REST API with auto-generated Swagger/OpenAPI docs
- 🐳 **Docker Support** — Fully containerized for consistent, portable deployment

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
[ChromaDB Vector Search] ← finds top-k semantically similar document chunks
     │
     ▼
[Ollama llama3.2]        ← local LLM, no internet required
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
| LLM | Ollama (llama3.2) — local, offline |
| Containerization | Docker |
| Language | Python 3.11+ |

---

## 📁 Project Structure

```
call-center-rag-assistant/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Environment config (.env)
│   ├── routers/
│   │   └── query.py         # POST /query/ask endpoint
│   ├── services/
│   │   ├── vector_store.py  # ChromaDB + embedding logic
│   │   └── llm_service.py   # Ollama LLM integration
│   └── models/
├── data/
│   └── sample_docs.py       # Sample call center policy documents
├── tests/
│   ├── test_api.py          # FastAPI endpoint tests
│   └── test_vector_store.py # Vector search unit tests
├── ingest_samples.py        # Script to load docs into ChromaDB
├── Dockerfile
├── requirements.txt
└── .env.example
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

### 4. Install and start Ollama

```bash
# Download from https://ollama.com
ollama pull llama3.2
```

### 5. Ingest sample documents

```bash
python ingest_samples.py
```

### 6. Run the API

```bash
uvicorn app.main:app --reload
```

- API: `http://localhost:8000`
- Swagger docs: `http://localhost:8000/docs`

---

## 🐳 Run with Docker

```bash
docker build -t call-center-rag-assistant .
docker run -p 8000:8000 call-center-rag-assistant
```

---

## 📡 API Endpoints

### `POST /query/ask`

Ask a question and get a grounded, context-aware answer from the knowledge base.

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

## 🧪 Tests

```bash
pip install pytest
pytest tests/
```

---

## 🗺️ Roadmap

### Core API
- [ ] `POST /documents/ingest` — Upload new documents via API
- [ ] `GET /documents` — List all documents in the knowledge base
- [ ] `DELETE /documents/{id}` — Remove a document

### Speech & Conversation Intelligence _(aligned with contact center use cases)_
- [ ] Call transcript ingestion and analysis
- [ ] Speaker-based conversation chunking (agent vs. customer turns)
- [ ] Customer intent classification from transcripts
- [ ] Sentiment analysis on customer utterances
- [ ] Automated call summarization

### Infrastructure
- [ ] Unit and integration tests with pytest
- [ ] docker-compose with Ollama service included
- [ ] Streaming LLM responses via WebSocket
- [ ] Gemini API / OpenAI as pluggable LLM backends
- [ ] CI/CD pipeline with GitHub Actions

---

## Switching LLM Backend

The LLM layer is intentionally decoupled. To switch from Ollama to Gemini API:

1. Add `GEMINI_API_KEY` to your `.env`
2. Update `app/services/llm_service.py` to use `google-generativeai`

No other changes needed.