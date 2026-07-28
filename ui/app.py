"""
Main Streamlit Application Entrypoint.
Enterprise Agentic RAG User Interface.
"""
import streamlit as st
import os
import sys

# Ensure project root is accessible in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ui.config import API_BASE_URL, API_TIMEOUT, SessionKeys, CUSTOM_CSS
from ui.api_client import RAGApiClient
from ui.components.header import render_header
from ui.components.sidebar import render_sidebar
from ui.components.chat_feed import render_chat_feed
from ui.components.input_box import render_input_box


def initialize_session():
    """Initializes default values in Streamlit Session State."""
    if SessionKeys.MESSAGES not in st.session_state:
        st.session_state[SessionKeys.MESSAGES] = []
    if SessionKeys.THREAD_ID not in st.session_state:
        st.session_state[SessionKeys.THREAD_ID] = "default_user"


def main():
    # 1. Page Configuration
    st.set_page_config(
        page_title="Fonepay AI Assistant Dashboard",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # 2. Inject Custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # 3. Initialize Session State
    initialize_session()

    # 4. Instantiate API Client & Health Check
    api_client = RAGApiClient(base_url=API_BASE_URL, timeout=API_TIMEOUT)
    is_connected = api_client.check_health()
    st.session_state[SessionKeys.IS_CONNECTED] = is_connected

    # 5. Render Header & Sidebar
    render_header(is_connected=is_connected)
    render_sidebar(api_client=api_client)

    # 6. Render Current Chat Feed
    render_chat_feed(messages=st.session_state[SessionKeys.MESSAGES])

    # 7. Render Input Box & Handle Query Submission
    prompt = render_input_box(messages_empty=len(st.session_state[SessionKeys.MESSAGES]) == 0)

    if prompt:
        # Check backend connectivity before submitting
        if not is_connected:
            st.error("❌ Cannot send query. The FastAPI backend server is currently unreachable. Start server on http://127.0.0.1:8000")
            return

        thread_id = st.session_state[SessionKeys.THREAD_ID]

        # Append User Turn
        st.session_state[SessionKeys.MESSAGES].append({
            "role": "user",
            "content": prompt
        })

        # Display Spinner & Send Query to LangGraph Backend
        with st.spinner("🧠 LangGraph Agent executing planning, retrieval & answer generation..."):
            response = api_client.send_query(query=prompt, thread_id=thread_id)

        # Append Assistant Turn
        st.session_state[SessionKeys.MESSAGES].append({
            "role": "assistant",
            "content": response.answer,
            "thought_process": response.thought_process,
            "sources": response.sources,
            "status": response.status
        })

        # Trigger Rerun to update chat feed seamlessly
        st.rerun()


if __name__ == "__main__":
    main()
