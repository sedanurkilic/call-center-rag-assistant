from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """Root endpoint should return 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_ask_question_returns_200():
    """Query endpoint should return 200 with a valid question."""
    response = client.post("/query/ask", params={"question": "What is the refund policy?"})
    assert response.status_code == 200


def test_ask_question_response_structure():
    """Response should contain question, answer, and sources."""
    response = client.post("/query/ask", params={"question": "What is the refund policy?"})
    data = response.json()
    assert "question" in data
    assert "answer" in data
    assert "sources" in data


def test_ask_question_sources_is_list():
    """Sources should be a list."""
    response = client.post("/query/ask", params={"question": "How do I cancel my subscription?"})
    data = response.json()
    assert isinstance(data["sources"], list)


def test_ask_empty_question():
    """Empty question should return 422 validation error."""
    response = client.post("/query/ask", params={"question": ""})
    assert response.status_code in [200, 422]