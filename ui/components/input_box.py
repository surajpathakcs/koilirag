"""
Empty-state hero with suggestion chips, plus the chat input bar.
"""
import streamlit as st
from typing import Optional
from ui.config import EXAMPLE_PROMPTS


def render_input_box(messages_empty: bool) -> Optional[str]:
    selected_prompt: Optional[str] = None

    if messages_empty:
        st.markdown(
            """
            <div class="koili-hero">
                <h1>How can I help with Koili TMS?</h1>
                <p>Ask about branches, users and roles, merchants, IPN devices,
                   schemes, partners, billing, settings or audit logs.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        cols = st.columns(2)
        for i, prompt_text in enumerate(EXAMPLE_PROMPTS):
            if cols[i % 2].button(prompt_text, key=f"suggestion_{i}", use_container_width=True):
                selected_prompt = prompt_text

    user_input = st.chat_input("Message Koili Assistant…")

    return selected_prompt or user_input
