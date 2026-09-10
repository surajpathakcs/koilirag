"""
Chat feed component for rendering message turns, thought steps, and retrieved sources.
"""
import re
import streamlit as st
from typing import List, Dict, Any

from ui.config import API_BASE_URL

_IMAGE_MARKER = re.compile(r"\[\[IMAGE:\s*([^\]]+?)\s*\]\]")


def _render_with_screenshots(content: str):
    """Render assistant text, replacing [[IMAGE: name]] markers with the actual
    screenshot fetched through the API's /images proxy."""
    pos = 0
    for m in _IMAGE_MARKER.finditer(content):
        before = content[pos:m.start()].strip()
        if before:
            st.markdown(before)
        name = m.group(1).strip()
        st.image(f"{API_BASE_URL}/images/{name}", use_container_width=True)
        pos = m.end()
    tail = content[pos:].strip()
    if tail:
        st.markdown(tail)

def render_chat_feed(messages: List[Dict[str, Any]]):
    """
    Renders the active conversation feed including user inputs, assistant responses,
    expandable thought logs, and source cards.
    """
    if not messages:
        st.info("💡 Ask a question below to start chatting with the Koili TMS Assistant.")
        return

    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        thought_process = msg.get("thought_process", [])
        sources = msg.get("sources", [])
        status = msg.get("status", "")

        with st.chat_message(role):
            # 1. Render thought process expander if present
            if thought_process:
                with st.expander("🧠 Agent Thought Process & Graph Steps", expanded=False):
                    for idx, step in enumerate(thought_process, 1):
                        st.markdown(f"**Step {idx}:** `{step}`")
            
            # 2. Guardrails / Warning notice
            if status == "Blocked by guardrails.":
                st.warning("🛡️ Response intercepted by safety guardrails.")

            # 3. Main content (assistant answers may embed screenshot markers)
            if role == "assistant":
                _render_with_screenshots(content)
            else:
                st.markdown(content)
            
            # 4. Render retrieved sources expander if documents exist
            if sources:
                with st.expander(f"📚 Retrieved Knowledge Sources ({len(sources)})", expanded=False):
                    for idx, doc in enumerate(sources, 1):
                        meta = doc.get("metadata", {}) if isinstance(doc, dict) else {}
                        page_content = doc.get("page_content", str(doc)) if isinstance(doc, dict) else str(doc)
                        
                        source_name = meta.get("source", f"Document Chunk #{idx}")
                        # Extract source from string if it matches our RAG's new string format
                        if isinstance(doc, str) and doc.startswith("SOURCE: "):
                            parts = doc.split("\nCONTENT: ", 1)
                            if len(parts) == 2:
                                source_name = parts[0].replace("SOURCE: ", "").strip()
                                page_content = parts[1].strip()

                        score = meta.get("score")
                        
                        st.markdown(f"**Source {idx}:** `{source_name}`" + (f" | *Score: {score:.4f}*" if score else ""))
                        st.caption(page_content[:300] + ("..." if len(page_content) > 300 else ""))
                        if idx < len(sources):
                            st.divider()
