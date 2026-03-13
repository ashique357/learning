"""
Solution Architect Learning Assistant
Hosted on Hugging Face Spaces with Groq API
"""

import streamlit as st
import os
from pathlib import Path
from rag_engine import RAGEngine
from ingestion import DocumentIngestion

# Page config
st.set_page_config(
    page_title="Solution Architect Learning Assistant",
    page_icon="🎓",
    layout="wide",
)

# Auto-ingest if chroma_db doesn't exist
if not Path("./chroma_db").exists():
    with st.spinner("🔄 First run: Processing learning materials..."):
        ingestion = DocumentIngestion("./learning-content")
        ingestion.ingest()
    st.success("✅ Learning materials processed!")

# Initialize RAG engine
if "rag_engine" not in st.session_state:
    with st.spinner("🔄 Loading RAG engine..."):
        try:
            st.session_state.rag_engine = RAGEngine()
            st.session_state.engine_loaded = True
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.session_state.engine_loaded = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("🎓 Learning Assistant")
    st.markdown("---")

    model_options = [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "mixtral-8x7b-32768",
    ]
    selected_model = st.selectbox("Select Model", model_options, index=0)

    if st.button("🔄 Reload Model"):
        with st.spinner("Loading..."):
            st.session_state.rag_engine = RAGEngine(model_name=selected_model)
        st.success(f"✓ Loaded {selected_model}")

    st.markdown("---")
    st.subheader("📚 Subjects")
    subjects = [
        "01-linux-os-fundamentals",
        "02-basic-networking",
        "03-database",
        "04-system-architecture",
        "05-docker",
        "06-kubernetes",
        "07-aws",
        "08-ci-cd",
        "09-design-patterns",
        "10-monitoring-observability",
        "11-security-compliance",
        "12-message-queues-streaming",
        "13-api-design-management",
        "14-java",
        "15-spring-boot",
        "16-python",
        "17-django",
        "18-fastapi",
        "19-frontend",
    ]
    selected_subject = st.selectbox("Filter by subject", ["All"] + subjects)

    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main content
st.title("🎓 Solution Architect Learning Assistant")
st.markdown("Ask questions about any topic in your learning roadmap!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message and message["sources"]:
            with st.expander("📚 Sources"):
                for source in message["sources"]:
                    st.markdown(f"- **{source['subject']}** / {source['file']}")

# Chat input
if prompt := st.chat_input("Ask a question about your learning topics..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.engine_loaded:
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                try:
                    result = st.session_state.rag_engine.query(prompt)
                    st.markdown(result["answer"])

                    if result["sources"]:
                        with st.expander("📚 Sources"):
                            for source in result["sources"]:
                                st.markdown(
                                    f"- **{source['subject']}** / {source['file']}"
                                )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": result["answer"],
                            "sources": result["sources"],
                        }
                    )
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    else:
        st.error("❌ RAG engine not loaded. Check GROQ_API_KEY in Space Secrets.")
