"""
Chat feed component. Assistant answers embed [[IMAGE: name]] markers that were
placed (server-side) at the steps each screenshot illustrates; here we render
each marker as the actual image, inline, between the surrounding text.
"""
import re
import base64
import mimetypes
import requests
import streamlit as st
from typing import List, Dict, Any

from ui.config import API_BASE_URL

_MARKER = re.compile(r"\[\[IMAGE:\s*(manual_img_\d{1,4}\.(?:png|jpe?g))\s*\]\]", re.IGNORECASE)


@st.cache_data(show_spinner=False, ttl=3600)
def _image_data_uri(name: str) -> str | None:
    """Fetch a screenshot through the API's /images proxy (server-side) and
    return it as a data: URI so it embeds directly in the markdown — keeps
    numbered-list continuity that separate st.image() calls would break."""
    try:
        r = requests.get(f"{API_BASE_URL}/images/{name}", timeout=15)
        r.raise_for_status()
        mime = mimetypes.guess_type(name)[0] or "image/jpeg"
        b64 = base64.b64encode(r.content).decode()
        return f"data:{mime};base64,{b64}"
    except Exception:
        return None


def _render_answer(content: str):
    """Render the answer as one markdown block, each [[IMAGE: name]] marker
    swapped for the inline screenshot at its position."""
    def repl(m: re.Match) -> str:
        uri = _image_data_uri(m.group(1))
        if uri:
            return f"\n\n![{m.group(1)}]({uri})\n\n"
        return f"\n\n_⚠️ {m.group(1)} unavailable_\n\n"

    st.markdown(_MARKER.sub(repl, content))


def render_chat_feed(messages: List[Dict[str, Any]]):
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
            if thought_process:
                with st.expander("🧠 Agent Thought Process & Graph Steps", expanded=False):
                    for idx, step in enumerate(thought_process, 1):
                        st.markdown(f"**Step {idx}:** `{step}`")

            if status == "Blocked by guardrails.":
                st.warning("🛡️ Response intercepted by safety guardrails.")

            if role == "assistant":
                _render_answer(content)
            else:
                st.markdown(content)

            if sources:
                with st.expander(f"📚 Retrieved Knowledge Sources ({len(sources)})", expanded=False):
                    for idx, doc in enumerate(sources, 1):
                        text = doc if isinstance(doc, str) else str(doc)
                        source_name = f"Chunk #{idx}"
                        if text.startswith("SOURCE: "):
                            head, _, body = text.partition("\nCONTENT: ")
                            source_name = head.replace("SOURCE: ", "").split("\n")[0].strip()
                            text = body.strip()
                        st.markdown(f"**Source {idx}:** `{source_name}`")
                        st.caption(text[:300] + ("..." if len(text) > 300 else ""))
                        if idx < len(sources):
                            st.divider()
