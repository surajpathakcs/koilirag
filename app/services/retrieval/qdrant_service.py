import logfire
from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.config import settings
from app.services.retrieval.embedding import embed_query


# Initialize Qdrant Client
client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY
)

def search_enterprise_knowledge(query: str, limit: int = 8):
    """
    Performs a high-precision search in the enterprise knowledge base.
    Uses the modern query_points interface.
    """
    with logfire.span("🗄️ Qdrant Vector Search") as span:
        try:
            query_vector = embed_query(query)

            # Using query_points - the modern standard for Qdrant
            response = client.query_points(
                collection_name=settings.QDRANT_COLLECTION,
                query=query_vector,
                limit=limit,
                with_payload=True # JSON
            )

            results = []
            for res in response.points:
                results.append({
                    "content": res.payload.get("text", ""),
                    "source": res.payload.get("source", "Unknown"),
                    "score": res.score
                })

            # Structured span attributes
            top_score = results[0]["score"] if results else None
            if span:
                span.set_attribute("qdrant.collection", settings.QDRANT_COLLECTION)
                span.set_attribute("qdrant.limit", limit)
                span.set_attribute("qdrant.result_count", len(results))
                if top_score is not None:
                    span.set_attribute("qdrant.top_score", round(top_score, 4))

            return results
        except Exception as e:
            if span:
                span.set_attribute("qdrant.error", str(e)[:200])
            logfire.error("❌ Qdrant Search Failed: {error}", error=str(e))
            return []
