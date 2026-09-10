"""
Chat feed component. Assistant answers embed [[IMAGE: name]] markers that were
placed (server-side) at the steps each screenshot illustrates; here we render
each marker as the actual image, inline, between the surrounding text.
"""
import re
import requests
import streamlit as st
from typing import List, Dict, Any

from ui.config import API_BASE_URL

_MARKER = re.compile(r"\[\[IMAGE:\s*(manual_img_\d{1,4}\.(?:png|jpe?g))\s*\]\]", re.IGNORECASE)


@st.cache_data(show_spinner=False, ttl=3600)
def _fetch_image(name: str) -> bytes | None:
    """Fetch a screenshot through the API's /images proxy, server-side, so the
    browser never needs to reach the API or MinIO directly."""
    try:
        r = requests.get(f"{API_BASE_URL}/images/{name}", timeout=15)
        r.raise_for_status()
        return r.content
    except Exception:
        return None


def _show_image(data: bytes):
    """Full-width image across Streamlit versions. `use_container_width` was
    deprecated for st.image in favour of width="stretch"; older builds accept
    neither, so fall back to a plain call."""
    for kwargs in ({"width": "stretch"}, {"use_container_width": True}, {}):
        try:
            st.image(data, **kwargs)
            return
        except TypeError:
            continue
        except Exception:
            return


def _render_answer(content: str):
    """Render the answer, swapping each [[IMAGE: name]] marker for the actual
    screenshot at that exact position — so every step is followed by the shot
    that illustrates it, then the next step."""
    pos = 0
    for m in _MARKER.finditer(content):
        before = content[pos:m.start()].strip()
        if before:
            st.markdown(before)
        data = _fetch_image(m.group(1))
        if data:
            _show_image(data)
        else:
            st.caption(f"⚠️ screenshot {m.group(1)} unavailable")
        pos = m.end()
    tail = content[pos:].strip()
    if tail:
        st.markdown(tail)


_AVATARS = {"assistant": "🟢", "user": "🧑"}


def render_chat_feed(messages: List[Dict[str, Any]]):
    if not messages:
        return  # the empty state lives in the input box hero

    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        thought_process = msg.get("thought_process", [])
        sources = msg.get("sources", [])
        status = msg.get("status", "")

        with st.chat_message(role, avatar=_AVATARS.get(role)):
            if thought_process:
                with st.expander("Reasoning steps", expanded=False):
                    for idx, step in enumerate(thought_process, 1):
                        st.markdown(f"**Step {idx}:** `{step}`")

            if status == "Blocked by guardrails.":
                st.warning("🛡️ Response intercepted by safety guardrails.")

            if role == "assistant":
                _render_answer(content)
            else:
                st.markdown(content)

            if sources:
                with st.expander(f"Manual sections used ({len(sources)})", expanded=False):
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
