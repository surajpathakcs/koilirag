import time
import logfire
from flashrank import Ranker, RerankRequest

# Lazy initialization - Ranker is loaded on first use to ensure logfire.configure() has run
_ranker = None


def _get_ranker() -> Ranker:
    """
    Initializes the FlashRank engine lazily. 
    FlashRank uses a local ONNX model (ms-marco-MiniLM-L-6-v2) for ultra-fast reranking.
    """
    global _ranker
    if _ranker is None:
        logfire.info("🧠 Initializing FlashRank Model (TinyBERT) locally...")
        try:
            # We use a specific cache directory to avoid permission issues in production
            _ranker = Ranker(cache_dir="/tmp/flashrank")
        except Exception:
            _ranker = Ranker()
    return _ranker



def rerank_documents(query: str, documents: list[dict], top_n: int = 5) -> list[dict]:
    """
    Refines retrieval results by re-scoring documents against the query semantically.
    
    Why FlashRank? 
    Standard vector search (Cosine Similarity) is fast but mathematically "fuzzy."
    FlashRank uses a Cross-Encoder approach which is much more precise but usually slow.
    FlashRank solves this by using highly optimized, quantized ONNX models locally.
    """
    if not documents:
        return []

    with logfire.span("⚖️ Semantic Reranking") as span:
        start = time.perf_counter()
        try:
            ranker = _get_ranker()
            
            # FlashRank expects a list of dictionaries with 'id' and 'text'. 
            # We also pass 'meta' so we can recover the source.
            passages = [
                {"id": i, "text": doc["content"], "meta": {"source": doc.get("source", "Unknown")}}
                for i, doc in enumerate(documents)
            ]

            request = RerankRequest(query=query, passages=passages)
            results = ranker.rerank(request)
            
            # Results are returned sorted by highest semantic score first
            reranked_docs = []
            for res in results[:top_n]:
                reranked_docs.append({
                    "content": res['text'],
                    "source": res.get("meta", {}).get("source", "Unknown")
                })

            latency_ms = (time.perf_counter() - start) * 1000
            top_score = results[0]['score'] if results else None

            if span:
                span.set_attribute("reranker.input_count", len(documents))
                span.set_attribute("reranker.output_count", len(reranked_docs))
                span.set_attribute("reranker.latency_ms", round(latency_ms, 1))
                if top_score is not None:
                    span.set_attribute("reranker.top_score", round(float(top_score), 4))

            return reranked_docs

        except Exception as e:
            latency_ms = (time.perf_counter() - start) * 1000
            if span:
                span.set_attribute("reranker.input_count", len(documents))
                span.set_attribute("reranker.latency_ms", round(latency_ms, 1))
                span.set_attribute("reranker.error", str(e)[:200])
            logfire.error("❌ Semantic Reranking Failed: {error}", error=str(e))
            # Fallback to the original Qdrant order to ensure the user still gets an answer
            return documents[:top_n]
