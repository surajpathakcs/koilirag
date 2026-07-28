import logfire
from app.agents.state import AgentState
from app.services.retrieval.qdrant_service import search_enterprise_knowledge
from app.services.retrieval.ranking_service import rerank_documents

def retrieve_node(state: AgentState):
    """
    Performs vector search and semantic reranking for technical queries.
    """
    query = state["current_query"]
    
    with logfire.span("🔍 Knowledge Retrieval") as span:
        # search_enterprise_knowledge already creates child spans for
        # embedding + qdrant search, so they nest under this parent.
        raw_results = search_enterprise_knowledge(query, limit=15)

        # rerank_documents creates its own child span (⚖️ Semantic Reranking)
        reranked_results = rerank_documents(query, raw_results, top_n=4)

        formatted_docs = [f"SOURCE: {doc.get('source', 'Unknown')}\nCONTENT: {doc['content']}" for doc in reranked_results]

        source_chunks = [{"id": doc.get("source", "Unknown"), "snippet": doc.get("content", "")[:500]} for doc in reranked_results]

        # Structured span attributes on the parent retrieval span
        if span:
            span.set_attribute("retrieval.query_length", len(query))
            span.set_attribute("retrieval.candidate_count", len(raw_results))
            span.set_attribute("retrieval.reranked_count", len(reranked_results))
    
    return {
        "documents": formatted_docs,
        "source_chunks": source_chunks,
        "status": f"Found technical context.",
        "plan": state["plan"] + ["Context Retrieved"]
    }
