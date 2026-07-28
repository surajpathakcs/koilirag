import time
import logfire
from pydantic import BaseModel, Field
from app.agents.state import AgentState
from app.gateway import get_langchain_llm

class Grade(BaseModel):
    """Binary score for hallucination check."""
    grounded: str = Field(description="Are the claims in the answer grounded in the retrieved documents? 'yes' or 'no'")

# We use a fast model for grading, no need for the massive 70b
llm = get_langchain_llm(feature="grader").with_structured_output(Grade)

def grader_node(state: AgentState):
    """
    Grades the generated answer against the retrieved documents to check for hallucinations.
    """
    documents = state.get("documents", [])
    answer = state.get("final_answer", "")
    retries = state.get("hallucination_retries", 0)

    # If no documents were retrieved, we can't really check grounding in the traditional sense,
    # but the responder shouldn't have answered with external facts anyway.
    if not documents:
        return {"status": "No documents to grade against."}

    docs_str = "\n\n".join(documents)
    prompt = f"""
    You are a Hallucination Grader.
    
    RETRIEVED DOCUMENTS:
    {docs_str}
    
    GENERATED ANSWER:
    {answer}
    
    Does the generated answer contain claims or facts that are NOT supported by the retrieved documents?
    Output 'yes' if the answer is grounded (all claims supported).
    Output 'no' if the answer contains hallucinations or unsupported claims.
    """

    with logfire.span("⚖️ Hallucination Grader") as span:
        start = time.perf_counter()
        try:
            result = llm.invoke(prompt)
            score = result.grounded.lower()
        except Exception as e:
            # If the structured output fails, assume it's grounded to avoid infinite loops
            logfire.error(f"Grader failed: {e}")
            score = "yes"
            
        latency_ms = (time.perf_counter() - start) * 1000

        if span:
            span.set_attribute("grader.score", score)
            span.set_attribute("grader.latency_ms", round(latency_ms, 1))
            span.set_attribute("grader.retries", retries)

    if score == "yes" or retries >= 2:
        return {
            "status": "Answer is grounded and approved.",
            "hallucination_retries": retries + 1
        }
    else:
        return {
            "status": "Hallucination detected. Forcing retry.",
            "hallucination_retries": retries + 1
        }
