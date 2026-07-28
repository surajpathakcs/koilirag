"""
Sidebar component for session management, workflow visualization, and system parameters.
"""
import streamlit as st
from ui.config import SessionKeys
from ui.api_client import RAGApiClient

def render_sidebar(api_client: RAGApiClient):
    """
    Renders sidebar controls, thread state, and architecture inspection tools.
    """
    with st.sidebar:
        st.header("⚙️ Session Controls")
        
        # Thread Selection for LangGraph MemorySaver
        current_thread = st.text_input(
            "Session Thread ID",
            value=st.session_state.get(SessionKeys.THREAD_ID, "default_user"),
            help="LangGraph MemorySaver isolated thread key for conversation state."
        )
        st.session_state[SessionKeys.THREAD_ID] = current_thread
        
        # Clear Conversation Button
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state[SessionKeys.MESSAGES] = []
            st.rerun()
            
        st.divider()
        
        # Architecture Workflow Viewer
        st.subheader("🗺️ Agent Architecture")
        with st.expander("State Graph Diagram", expanded=False):
            if st.button("Fetch Live Graph", use_container_width=True):
                graph_bytes = api_client.get_workflow_graph()
                if graph_bytes:
                    st.session_state[SessionKeys.GRAPH_IMAGE] = graph_bytes
                else:
                    st.error("Failed to load workflow graph from backend.")
            
            if SessionKeys.GRAPH_IMAGE in st.session_state:
                st.image(st.session_state[SessionKeys.GRAPH_IMAGE], caption="LangGraph State Diagram")
                
        st.divider()
        
        # System Architecture Notes
        st.subheader("System Stack")
        st.markdown(
            """
            - **Gateway**: Portkey / Groq `Llama 3.3`
            - **Safety**: NeMo Guardrails
            - **Agent Core**: LangGraph Linear Flow
            - **Vector Database**: Qdrant Cloud
            - **Reranker**: FlashRank Cross-Encoder
            - **Tracing**: Pydantic Logfire
            """
        )
