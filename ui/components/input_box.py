"""
Input box component supporting user text input and prompt suggestion buttons.
"""
import streamlit as st
from typing import Optional
from ui.config import EXAMPLE_PROMPTS

def render_input_box(messages_empty: bool) -> Optional[str]:
    """
    Renders prompt chips if no conversation exists yet, and returns prompt input.
    """
    selected_prompt: Optional[str] = None
    
    # Prompt suggestion buttons if chat is fresh
    if messages_empty:
        st.markdown("**Suggested Queries:**")
        cols = st.columns(2)
        for i, prompt_text in enumerate(EXAMPLE_PROMPTS):
            col = cols[i % 2]
            if col.button(prompt_text, key=f"suggestion_{i}", use_container_width=True):
                selected_prompt = prompt_text

    # Main chat input bar
    user_input = st.chat_input("Ask a question about Fonepay Merchant Services, APIs, or Hardware...")
    
    return selected_prompt or user_input
