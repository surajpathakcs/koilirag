"""
Header Component for rendering app title, badge status, and description.
"""
import streamlit as st

def render_header(is_connected: bool):
    """
    Renders top application header with backend connection status badge.
    """
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.title("🛡️ Fonepay AI Assistant")
        st.caption("Powered by LangGraph · NeMo Guardrails · Qdrant · Groq Llama 3.3 · Logfire")
        
    with col2:
        st.write("") # Spacing adjustment
        if is_connected:
            st.markdown('<span class="badge-online">🟢 API ONLINE</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="badge-offline">🔴 API OFFLINE</span>', unsafe_allow_html=True)

    st.divider()
