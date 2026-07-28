import logfire
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from app.agents.state import AgentState
from app.agents.nodes.planner import planner_node
from app.agents.nodes.retriever import retrieve_node
from app.agents.nodes.responder import generate_node
from app.agents.nodes.grader import grader_node


workflow = StateGraph(AgentState)


# Nodes
workflow.add_node("planner", planner_node)
workflow.add_node("retriever", retrieve_node)
workflow.add_node("responder", generate_node)
workflow.add_node("grader", grader_node)


# Flow
workflow.set_entry_point("planner")

workflow.add_edge("planner", "retriever")
workflow.add_edge("retriever", "responder")
workflow.add_edge("responder", "grader")


def grade_router(state: AgentState):
    if state["grader_passed"]:
        return "approved"

    return "retry"

workflow.add_conditional_edges(
    "grader",
    grade_router,
    {
        "approved": END,
        "retry": "responder"
    }
)


checkpointer = MemorySaver()

rag_agent = workflow.compile(
    checkpointer=checkpointer
)