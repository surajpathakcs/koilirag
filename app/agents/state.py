from typing import TypedDict, List, Annotated
import operator


class AgentState(TypedDict):
    messages: Annotated[List[dict], operator.add]
    current_query: str
    documents: List[str]
    # Reranked chunks that passed the score gate, with content_md/images/score.
    retrieved: List[dict]
    plan: List[str]
    status: str
    final_answer: str
    source_chunks: List[dict]
    escalation: str

    # Hallucination grading loop
    hallucination_retries: int
    grader_feedback: str
    grader_passed: bool