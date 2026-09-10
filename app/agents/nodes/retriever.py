import logfire
from app.config import settings
from app.agents.state import AgentState
from app.services.retrieval.qdrant_service import search_enterprise_knowledge
from app.services.retrieval.ranking_service import rerank_documents
from app.services.answer_mode import gate_by_score


def retrieve_node(state: AgentState):
    """
    Vector search -> cross-encoder rerank -> score gate.

    The gate keeps only the chunks the reranker actually rates as answering the
    query (usually one section, sometimes two alternative methods), so the
    responder is never handed sections it will ignore.
    """
    query = state["current_query"]

    with logfire.span("🔍 Knowledge Retrieval") as span:
        raw_results = search_enterprise_knowledge(query, limit=settings.RETRIEVAL_CANDIDATES)
        reranked_results = rerank_documents(query, raw_results, top_n=settings.RETRIEVAL_TOP_N)
        kept = gate_by_score(reranked_results)

        formatted_docs = [
            f"SOURCE: {doc.get('source', 'Unknown')}\n"
            f"SECTION: {doc.get('section_path') or 'N/A'}\n"
            f"CONTENT: {doc.get('content_md') or doc['content']}"
            for doc in kept
        ]

        source_chunks = [
            {
                "id": doc.get("section_path") or doc.get("source", "Unknown"),
                "snippet": doc.get("content", "")[:500],
                "images": doc.get("images", []),
                "score": round(doc.get("score", 0.0), 4),
            }
            for doc in kept
        ]

        if span:
            span.set_attribute("retrieval.query_length", len(query))
            span.set_attribute("retrieval.candidate_count", len(raw_results))
            span.set_attribute("retrieval.reranked_count", len(reranked_results))
            span.set_attribute("retrieval.kept_count", len(kept))
            if kept:
                span.set_attribute("retrieval.top_score", round(kept[0].get("score", 0.0), 4))

    return {
        "documents": formatted_docs,
        "retrieved": kept,
        "source_chunks": source_chunks,
        "status": "Found relevant manual sections.",
        "plan": state["plan"] + [f"Context Retrieved ({len(kept)} section(s))"],
    }
