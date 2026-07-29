"""
Configuration settings and theme definitions for the Streamlit UI application.
"""
import os
from typing import Dict, Any

# --- API Configuration ---
API_BASE_URL: str = os.environ["API_BASE_URL"]
API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "60"))
print("API_BASE_URL:", API_BASE_URL)

# --- Session State Keys ---
class SessionKeys:
    MESSAGES: str = "chat_messages"
    THREAD_ID: str = "current_thread_id"
    IS_CONNECTED: str = "api_connected"
    GRAPH_IMAGE: str = "graph_image_bytes"

# --- Example Prompt Suggestions ---
EXAMPLE_PROMPTS = [
    "How do I become a Fonepay merchant?",
    "What is the difference between static and dynamic QR?",
    "How do I integrate Fonepay dynamic QR with my POS?",
    "Can Indian customers use UPI for QR payments in Nepal?"
]

# --- Custom CSS Styling ---
CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

    /* Global Typography & Background */
    html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #f1f5f9 100%);
        background-attachment: fixed;
        color: #1e293b;
    }

    /* Top Banner Header */
    h1, h2, h3 {
        color: #0f172a !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }

    .stCaption {
        color: #475569 !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #cbd5e1 !important;
        box-shadow: 2px 0 12px rgba(0, 0, 0, 0.03);
    }

    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #0f172a !important;
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li {
        color: #334155 !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25) !important;
    }

    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4) !important;
        background: linear-gradient(135deg, #4338ca 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
    }

    /* Badges */
    .badge-online {
        background: linear-gradient(135deg, #959669 0%, #39b619 100%);
        color: #ffffff;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
        display: inline-block;
    }
    
    .badge-offline {
        background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
        color: #ffffff;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
        display: inline-block;
    }

    /* Expander / Cards */
    div[data-testid="stExpander"] {
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
        background: #ffffff !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02) !important;
        overflow: hidden !important;
        margin-bottom: 0.5rem !important;
    }

    /* Chat Messages */
    .stChatMessage {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 1.2rem !important;
        margin-bottom: 0.75rem !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
        color: #1e293b !important;
    }

    .stChatMessage [data-testid="stMarkdownContainer"] p {
        color: #1e293b !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
    }

    /* Chat Input Bar */
    .stChatInputContainer {
        border-radius: 12px !important;
        border: 1.5px solid #6366f1 !important;
        background: #ffffff !important;
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.12) !important;
    }

    .stChatInputContainer textarea {
        color: #0f172a !important;
    }

    /* Custom Code Blocks & Inputs */
    input[type="text"] {
        background: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }
</style>
"""

