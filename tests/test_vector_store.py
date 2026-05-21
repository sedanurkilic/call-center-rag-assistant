import pytest
from app.services.vector_store import embed_text, search_documents


def test_embed_text_returns_list():
    """Embedding should return a list of floats."""
    vector = embed_text("What is the refund policy?")
    assert isinstance(vector, list)
    assert len(vector) > 0
    assert isinstance(vector[0], float)


def test_embed_text_consistent_dimension():
    """Two different texts should produce same-length vectors."""
    v1 = embed_text("refund policy")
    v2 = embed_text("technical support")
    assert len(v1) == len(v2)


def test_search_documents_returns_results():
    """Search should return a dict with documents and metadatas."""
    results = search_documents("refund", top_k=2)
    assert "documents" in results
    assert "metadatas" in results


def test_search_documents_top_k():
    """Search should return at most top_k results."""
    results = search_documents("support", top_k=2)
    assert len(results["documents"][0]) <= 2


def test_search_refund_finds_refund_policy():
    """Searching for 'refund' should return Refund Policy as top result."""
    results = search_documents("What is the refund period?", top_k=3)
    titles = [m["title"] for m in results["metadatas"][0]]
    assert "Refund Policy" in titles