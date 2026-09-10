"""
Compact product header: Koili mark, name, and a small connection dot.
"""
import streamlit as st


def render_header(is_connected: bool):
    dot_class = "koili-dot" if is_connected else "koili-dot off"
    dot_label = "Online" if is_connected else "Backend offline"

    st.markdown(
        f"""
        <div class="koili-header">
            <div class="koili-mark">K</div>
            <div>
                <div class="koili-name">Koili Assistant</div>
                <div class="koili-sub">Terminal Management System · user manual</div>
            </div>
            <div class="{dot_class}"><i></i>{dot_label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
