"""
Configuration settings and theme definitions for the Streamlit UI application.
"""
import os
from typing import Dict, Any

# --- API Configuration ---
API_BASE_URL: str = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "300"))
# print("API_BASE_URL:", API_BASE_URL)

# --- Session State Keys ---
class SessionKeys:
    MESSAGES: str = "chat_messages"
    THREAD_ID: str = "current_thread_id"
    IS_CONNECTED: str = "api_connected"
    GRAPH_IMAGE: str = "graph_image_bytes"

# --- Example Prompt Suggestions ---
EXAMPLE_PROMPTS = [
    "How do I assign an IPN to a merchant?",
    "What are the seven user roles in the TMS?",
    "How does a checker approve a pending request?",
    "How do I configure Pumari billing setup?"
]

# --- Custom CSS Styling ---
CUSTOM_CSS = """
<style>
    /* ── Koili Assistant — clean, centred, ChatGPT-like ───────────────── */

    :root {
        --koili-accent: #10a37f;
        --koili-text: #202123;
        --koili-muted: #6e6e80;
        --koili-line: #ececf1;
        --koili-bubble: #f7f7f8;
    }

    html, body, [class*="css"], input, textarea, button {
        font-family: ui-sans-serif, -apple-system, "Segoe UI", Roboto,
                     "Helvetica Neue", Arial, sans-serif;
    }

    .stApp { background: #ffffff; color: var(--koili-text); }

    /* Centred reading column */
    [data-testid="stMainBlockContainer"], .main .block-container {
        max-width: 48rem;
        padding-top: 1.5rem;
        padding-bottom: 6rem;
    }

    /* Hide Streamlit chrome */
    #MainMenu, footer, [data-testid="stDecoration"] { display: none; }
    [data-testid="stHeader"] { background: transparent; }

    /* ── Header ──────────────────────────────────────────────────────── */
    .koili-header {
        display: flex; align-items: center; gap: .7rem;
        padding: .2rem 0 1rem;
    }
    .koili-mark {
        width: 34px; height: 34px; border-radius: 9px;
        background: var(--koili-accent); color: #fff;
        display: flex; align-items: center; justify-content: center;
        font-weight: 700; font-size: 1rem; letter-spacing: -.02em;
        flex: 0 0 auto;
    }
    .koili-name { font-size: 1.02rem; font-weight: 600; line-height: 1.2; }
    .koili-sub  { font-size: .78rem; color: var(--koili-muted); line-height: 1.2; }
    .koili-dot {
        margin-left: auto; font-size: .74rem; color: var(--koili-muted);
        display: flex; align-items: center; gap: .4rem;
    }
    .koili-dot i {
        width: 7px; height: 7px; border-radius: 50%;
        background: var(--koili-accent); display: inline-block;
    }
    .koili-dot.off i { background: #e5484d; }

    /* ── Empty state ─────────────────────────────────────────────────── */
    .koili-hero {
        text-align: center; padding: 3rem 0 1.6rem;
    }
    .koili-hero h1 {
        font-size: 1.65rem !important; font-weight: 600 !important;
        margin: 0 0 .4rem !important; letter-spacing: -.02em;
        color: var(--koili-text) !important;
    }
    .koili-hero p { color: var(--koili-muted); font-size: .92rem; margin: 0; }

    /* ── Chat turns ──────────────────────────────────────────────────── */
    [data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: .35rem 0 !important;
        gap: .75rem;
    }
    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li {
        font-size: .95rem; line-height: 1.65; color: var(--koili-text);
    }
    /* User turn reads as a soft bubble */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"])
    [data-testid="stChatMessageContent"] {
        background: var(--koili-bubble);
        border-radius: 14px;
        padding: .7rem .95rem;
    }
    [data-testid="stChatMessage"] img {
        border-radius: 8px;
        border: 1px solid var(--koili-line);
        margin: .35rem 0 .8rem;
    }

    /* ── Expanders (thought process / sources) ───────────────────────── */
    [data-testid="stExpander"] {
        border: 1px solid var(--koili-line) !important;
        border-radius: 10px !important;
        background: #fff !important;
        box-shadow: none !important;
    }
    [data-testid="stExpander"] summary p { font-size: .82rem !important; color: var(--koili-muted) !important; }

    /* ── Suggestion chips ────────────────────────────────────────────── */
    .stButton > button {
        background: #fff !important;
        color: var(--koili-text) !important;
        border: 1px solid var(--koili-line) !important;
        border-radius: 12px !important;
        font-weight: 400 !important;
        font-size: .875rem !important;
        text-align: left !important;
        padding: .7rem .9rem !important;
        box-shadow: none !important;
        transition: background .15s ease, border-color .15s ease !important;
    }
    .stButton > button:hover {
        background: var(--koili-bubble) !important;
        border-color: #d9d9e3 !important;
        color: var(--koili-text) !important;
        transform: none !important;
    }

    /* ── Input bar ───────────────────────────────────────────────────── */
    [data-testid="stChatInput"] {
        border: 1px solid #d9d9e3 !important;
        border-radius: 16px !important;
        background: #fff !important;
        box-shadow: 0 2px 10px rgba(0,0,0,.05) !important;
    }
    [data-testid="stChatInput"] textarea { font-size: .95rem !important; }

    /* ── Sidebar ─────────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: var(--koili-bubble) !important;
        border-right: 1px solid var(--koili-line) !important;
    }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        font-size: .8rem !important; text-transform: uppercase;
        letter-spacing: .06em; color: var(--koili-muted) !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] li { font-size: .85rem; }

    hr { border-color: var(--koili-line) !important; }
</style>
"""


