"""
Chat feed component for rendering message turns, thought steps, retrieved
sources, and the screenshots that belong to the retrieved manual sections.
"""
import re
import requests
import streamlit as st
from typing import List, Dict, Any

from ui.config import API_BASE_URL

_IMAGE_MARKER = re.compile(r"\[\[IMAGE:\s*[^\]]+?\s*\]\]")
_IMG_NAME = re.compile(r"^manual_img_\d{1,4}\.(png|jpe?g)$", re.IGNORECASE)


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


def _render_screenshots(source_chunks: List[Dict[str, Any]]):
    """Show every screenshot from the retrieved chunks, grouped by section,
    deduplicated, in retrieval order."""
    seen: set[str] = set()
    groups: List[tuple[str, List[str]]] = []
    for ch in source_chunks:
        imgs = [n for n in ch.get("images", []) if _IMG_NAME.match(n or "") and n not in seen]
        for n in imgs:
            seen.add(n)
        if imgs:
            groups.append((ch.get("id", "Manual section"), imgs))

    if not groups:
        return

    total = sum(len(i) for _, i in groups)
    with st.expander(f"📷 Screenshots from the manual ({total})", expanded=True):
        for label, imgs in groups:
            st.caption(label)
            cols = st.columns(min(3, len(imgs)))
            for i, name in enumerate(imgs):
                data = _fetch_image(name)
                with cols[i % len(cols)]:
                    if data:
                        st.image(data, use_container_width=True)
                    else:
                        st.caption(f"⚠️ {name} unavailable")


def render_chat_feed(messages: List[Dict[str, Any]]):
    if not messages:
        st.info("💡 Ask a question below to start chatting with the Koili TMS Assistant.")
        return

    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        thought_process = msg.get("thought_process", [])
        sources = msg.get("sources", [])
        source_chunks = msg.get("source_chunks", [])
        status = msg.get("status", "")

        with st.chat_message(role):
            if thought_process:
                with st.expander("🧠 Agent Thought Process & Graph Steps", expanded=False):
                    for idx, step in enumerate(thought_process, 1):
                        st.markdown(f"**Step {idx}:** `{step}`")

            if status == "Blocked by guardrails.":
                st.warning("🛡️ Response intercepted by safety guardrails.")

            # Answer text — strip any stray [[IMAGE: ...]] markers the model
            # may have echoed; screenshots are rendered separately below.
            if role == "assistant":
                st.markdown(_IMAGE_MARKER.sub("", content).strip())
                _render_screenshots(source_chunks)
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
