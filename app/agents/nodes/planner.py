import time
import logfire
from app.agents.state import AgentState
from app.gateway import get_langchain_llm

# Portkey-backed LLM: fallback + cache + retry — same .invoke() interface as ChatGroq
llm = get_langchain_llm(feature="planner")

def planner_node(state: AgentState):
    """
    The Planner acts as a Query Contextualizer. 
    It rewrites the user's latest query to be fully self-contained based on the chat history.
    """
    history = ""
    for msg in state["messages"][:-1]:
        role = "User" if msg["role"] == "user" else "Assistant"
        history += f"{role}: {msg['content']}\n"
    
    user_message = state["messages"][-1]["content"] if state["messages"] else ""
    
    prompt = f"""
    You are an intelligent Query Contextualizer for the Fonepay AI Assistant. 
    Your job is to rewrite the user's latest message into a standalone, highly specific search query 
    optimized for a vector database (RAG).
    
    CONVERSATION HISTORY:
    {history}
    
    LATEST MESSAGE:
    "{user_message}"
    
    Instructions:
    - If the latest message lacks context (e.g., "how do I turn it on?", "what does the red light mean?"), 
      use the history to figure out what 'it' refers to (e.g., "Fonepay Soundbox red light meaning").
    - If the message is already self-contained, just return it as a clean search query.
    - NEVER answer the question. ONLY output the rewritten search query.
    - DO NOT include conversational filler like "Here is the query:". Output just the query itself.
    """
    
    with logfire.span("🧠 Query Contextualizer") as span:
        start = time.perf_counter()
        decision = llm.invoke(prompt).content.strip()
        latency_ms = (time.perf_counter() - start) * 1000

        if span:
            span.set_attribute("planner.rewritten_query", decision)
            span.set_attribute("planner.original_query_length", len(user_message))
            span.set_attribute("planner.latency_ms", round(latency_ms, 1))
    
    return {
        "current_query": decision,
        "status": f"Rewrote query for context. Searching for: '{decision}'",
        "plan": ["Intent: RAG Contextualization", f"Search Term: {decision}"]
    }
