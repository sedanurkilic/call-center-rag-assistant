import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def generate_answer(question: str, context_chunks: list[str]) -> str:
    """Soruyu ve ilgili doküman parçalarını Ollama'ya gönderir, cevap üretir."""

    context = "\n\n".join(context_chunks)

    prompt = f"""You are a call center assistant. Answer the question using only the documents below.
If the answer is not in the documents, say 'I don't have information on this topic.'

DOCUMENTS:
{context}

QUESTION: {question}

ANSWER:"""

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]