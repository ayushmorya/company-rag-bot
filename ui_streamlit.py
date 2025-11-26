from pathlib import Path
from datetime import datetime

import streamlit as st

from app.config import get_settings
from app.rag_store import ingest_file
from app.rag_graph import rag_graph

# ---------------------------------------------------------
# Basic page config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Company RAG Chatbot",
    page_icon="💬",
    layout="wide",
)

settings = get_settings()

# ---------------------------------------------------------
# Custom CSS for nicer styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* Remove top padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
    }

    /* Chat message styling */
    .stChatMessage {
        border-radius: 18px !important;
        padding: 0.75rem 1rem !important;
        margin-bottom: 0.4rem !important;
    }

    /* User bubble */
    .stChatMessage[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageUser"]) {
        background: #1f2933;
    }

    /* Assistant bubble */
    .stChatMessage[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAssistant"]) {
        background: #111827;
        border: 1px solid #374151;
    }

    /* Metric cards */
    .metric-card {
        padding: 0.75rem 1rem;
        border-radius: 14px;
        border: 1px solid rgba(148, 163, 184, 0.55);
        background: radial-gradient(circle at top left, #111827, #020617);
    }

    .metric-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #9ca3af;
        margin-bottom: 0.15rem;
    }

    .metric-value {
        font-size: 1.15rem;
        font-weight: 600;
        color: #f9fafb;
    }

    .metric-sub {
        font-size: 0.70rem;
        color: #6b7280;
    }

    /* File list style */
    .file-pill {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.6rem;
        border-radius: 999px;
        border: 1px solid #4b5563;
        font-size: 0.75rem;
        margin: 0.15rem 0.15rem 0 0;
        color: #e5e7eb;
    }

    .file-pill span {
        margin-left: 0.25rem;
        color: #9ca3af;
        font-size: 0.7rem;
    }

    /* Sidebar header */
    .side-header {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.35rem;
    }

    .subtext {
        font-size: 0.8rem;
        color: #9ca3af;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Initialize session state
# ---------------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # {"role": "user"/"assistant", "content": str}

if "stats" not in st.session_state:
    st.session_state.stats = {
        "files": 0,
        "chunks": 0,
        "last_updated": None,
        "files_list": [],
    }

# ---------------------------------------------------------
# Sidebar: upload + controls
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 📂 Knowledge Base")
    st.markdown(
        "<div class='subtext'>Upload your internal documents. "
        "They'll be embedded and stored locally in a Chroma database.</div>",
        unsafe_allow_html=True,
    )

    uploaded_files = st.file_uploader(
        "Choose files",
        type=["pdf", "txt", "docx", "doc"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )

    ingest_col1, ingest_col2 = st.columns([2, 1])

    with ingest_col1:
        ingest_clicked = st.button("⚙️ Ingest to Knowledge Base", use_container_width=True)

    with ingest_col2:
        clear_clicked = st.button("🧹 Clear Chat", use_container_width=True)

    if clear_clicked:
        st.session_state.chat_history = []
        st.success("Chat cleared.")

    # Handle ingestion
    if ingest_clicked:
        if not uploaded_files:
            st.warning("Please select at least one file.")
        else:
            total_chunks = 0
            ingested_files = []

            for file in uploaded_files:
                dest_path = settings.data_dir / file.name
                dest_path.write_bytes(file.read())
                chunks = ingest_file(dest_path)
                total_chunks += chunks
                ingested_files.append(file.name)

            st.session_state.stats["files"] += len(ingested_files)
            st.session_state.stats["chunks"] += total_chunks
            st.session_state.stats["last_updated"] = datetime.now().strftime("%d %b %Y, %H:%M")
            st.session_state.stats["files_list"].extend(ingested_files)

            st.success(f"Ingested {len(ingested_files)} file(s), {total_chunks} chunk(s) added.")

    st.markdown("---")

    st.markdown("#### 📑 Ingested Files")
    if st.session_state.stats["files_list"]:
        files_html = ""
        for f in st.session_state.stats["files_list"]:
            files_html += f"<div class='file-pill'>📄 {f}</div>"
        st.markdown(files_html, unsafe_allow_html=True)
    else:
        st.caption("No files ingested yet.")

    st.markdown("---")
    st.caption("Tip: Start by uploading a few PDFs or DOCX files like policies, resumes, or FAQs.")

# ---------------------------------------------------------
# Main header + stats row
# ---------------------------------------------------------
title_col, stats_col1, stats_col2, stats_col3 = st.columns([3, 1.3, 1.3, 1.6])

with title_col:
    st.markdown("## 💬 Company RAG Chatbot")
    st.markdown(
        "Ask questions in natural language and get answers grounded in your uploaded documents."
    )

with stats_col1:
    s = st.session_state.stats
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Documents</div>
            <div class="metric-value">{s['files']}</div>
            <div class="metric-sub">Total uploaded</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stats_col2:
    s = st.session_state.stats
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Chunks</div>
            <div class="metric-value">{s['chunks']}</div>
            <div class="metric-sub">Indexed for search</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stats_col3:
    last = st.session_state.stats["last_updated"] or "—"
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Knowledge Updated</div>
            <div class="metric-value">{last}</div>
            <div class="metric-sub">Powered by Gemini + LangGraph</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

# ---------------------------------------------------------
# Chat area
# ---------------------------------------------------------
chat_container = st.container()

with chat_container:
    # Render chat history
    for msg in st.session_state.chat_history:
        avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    # Input box
    user_input = st.chat_input("Ask a question about your documents...")

    if user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(user_input)

        # Model response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking with your documents..."):
                try:
                    state = {"question": user_input}
                    result = rag_graph.invoke(state)
                    answer = result["answer"]
                except Exception as e:
                    answer = f"Sorry, something went wrong:\n\n`{e}`"

                st.markdown(answer)

        st.session_state.chat_history.append({"role": "assistant", "content": answer})