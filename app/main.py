# ============================================================
# CRITICAL: logfire MUST be configured before ALL other imports
# so that spans from all modules are captured from the start.
# ============================================================
import logfire
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["NEMOGUARDRAILS_LLM_FRAMEWORK"] = "langchain"
os.environ["NEMOGUARDRAILS_LLM"] = "llama-3.3-70b-versatile"
# Prevent fastembed/huggingface_hub symlink failures on Windows.
# Without this, the embedding model download silently corrupts and NeMo
# returns "an internal error has occurred" instead of classifying intents.
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"

# Point fastembed to a project-local cache directory instead of the Windows
# Temp folder, which suffers from symlink permission failures.
fastembed_cache_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".cache", "fastembed"
)
os.environ["FASTEMBED_CACHE_PATH"] = fastembed_cache_path

# Only force offline mode if the model is already cached locally (e.g. on a dev
# machine after the first run). On a fresh environment (like a new Render
# deploy) with no cache yet, leave this unset so fastembed is allowed to
# download the model instead of failing silently.
if os.path.isdir(fastembed_cache_path) and os.listdir(fastembed_cache_path):
    os.environ["HF_HUB_OFFLINE"] = "1"


logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))

# Now safe to import app modules - logfire is already active
from fastapi import FastAPI, Response
from app.agents.graph import rag_agent
from app.agents.nodes.responder import generate_node
from app.guardrails import initialize_rails, guard, GuardrailStatus

from pydantic import BaseModel
from typing import Optional


# Initialize FastAPI
app = FastAPI(title="Fonepay AI Assistant API")

# Automatic HTTP request/response span creation (Disabled to avoid GET / spam)
# logfire.instrument_fastapi(app)

import logging
logging.getLogger("nemoguardrails").setLevel(logging.DEBUG)


@app.on_event("startup")
def startup_event():
    initialize_rails()

class QueryRequest(BaseModel):
    q: str
    thread_id: Optional[str] = "default_user"
    
    
@app.get("/")
def home():
    return {"message": "Fonepay AI Assistant API is live."}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/graph")
def get_graph_image():
    """
    Returns the Mermaid image of the agent's workflow.
    """
    try:
        png_bytes = rag_agent.get_graph().draw_mermaid_png()
        return Response(content=png_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"Could not generate graph image: {e}"}
    
    
@app.post("/query")
def query(request: QueryRequest):
    """
    Executes the LangGraph RAG flow with memory using a POST request.
    """
    q = request.q
    thread_id = request.thread_id

    initial_state = {
        "messages": [{"role": "user", "content": q}],
        "current_query": q,
        "documents": [],
        "plan": ["Start"],
        "status": "Initializing Graph...",
        "hallucination_retries": 0,
        "grader_feedback": "",
        "grader_passed": False,
        "source_chunks": [],
        "escalation": "none"
    }

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    with logfire.span("📡 Query: {q_snippet}", q_snippet=q[:60]) as pipeline_span:

        if pipeline_span:
            pipeline_span.set_attribute(
                "request.query_length",
                len(q)
            )
            pipeline_span.set_attribute(
                "request.thread_id",
                thread_id
            )

        try:

            # --------------------------------------------------
            # Gate 1: NeMo Guardrails
            # --------------------------------------------------
            guard_result = guard(q)


            # --------------------------------------------------
            # Security / policy block
            # --------------------------------------------------
            if guard_result.status == GuardrailStatus.BLOCKED:

                if pipeline_span:
                    pipeline_span.set_attribute(
                        "request.status",
                        "blocked"
                    )
                    pipeline_span.set_attribute(
                        "request.blocked_reason",
                        guard_result.reason or "unknown"
                    )

                return {
                    "question": q,
                    "answer": guard_result.response,
                    "thought_process": [
                        "Intent: Guardrails Blocked",
                        f"Reason: {guard_result.reason}"
                    ],
                    "status": "Blocked by guardrails.",
                    "sources": [],
                    "source_chunks": [],
                    "escalation": "none"
                }


            # --------------------------------------------------
            # Dialog handling
            # greeting / farewell / capabilities
            # --------------------------------------------------
            if guard_result.status == GuardrailStatus.DIALOG:

                if pipeline_span:
                    pipeline_span.set_attribute(
                        "request.status",
                        "dialog"
                    )

                return {
                    "question": q,
                    "answer": guard_result.response,
                    "thought_process": [
                        "Intent: Dialog",
                        f"Reason: {guard_result.reason}"
                    ],
                    "status": "Handled by dialog rail.",
                    "sources": [],
                    "source_chunks": [],
                    "escalation": "none"
                }


            # --------------------------------------------------
            # Guardrail failure
            # --------------------------------------------------
            if guard_result.status == GuardrailStatus.ERROR:

                logfire.warning(
                    "⚠️ Guardrail engine error.",
                    guardrail_reason=guard_result.reason
                )

                if pipeline_span:
                    pipeline_span.set_attribute(
                        "request.guardrail_error",
                        True
                    )

                return {
                    "question": q,
                    "answer": "The assistant is temporarily unavailable. Please try again later.",
                    "thought_process": [
                        "Guardrail execution failed."
                    ],
                    "status": "guardrail_error",
                    "sources": [],
                    "source_chunks": [],
                    "escalation": "none"
                }


            # --------------------------------------------------
            # Normal RAG execution
            # --------------------------------------------------
            final_output = rag_agent.invoke(
                initial_state,
                config=config
            )

            if pipeline_span:
                pipeline_span.set_attribute(
                    "request.status",
                    "success"
                )

            return {
                "question": q,
                "answer": final_output.get("final_answer"),
                "thought_process": final_output.get("plan"),
                "status": final_output.get("status"),
                "sources": final_output.get("documents", []),
                "source_chunks": final_output.get("source_chunks", []),
                "escalation": final_output.get("escalation", "none")
            }


        except Exception as e:

            if pipeline_span:
                pipeline_span.set_attribute(
                    "request.status",
                    "error"
                )
                pipeline_span.set_attribute(
                    "request.error",
                    str(e)[:200]
                )

            logfire.error(
                "❌ Backend Execution Failed: {error}",
                error=str(e)
            )

            return {
                "question": q,
                "answer": "I apologize, but I encountered an internal error while processing your request. Please try again later.",
                "thought_process": [
                    "Error encountered during execution."
                ],
                "status": "error",
                "sources": [],
                "source_chunks": [],
                "escalation": "none"
            }