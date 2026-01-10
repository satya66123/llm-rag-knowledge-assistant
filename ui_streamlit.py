import streamlit as st
import requests
from typing import List, Dict

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="RAG Chat Assistant", page_icon="🤖", layout="wide")

st.title("🤖 RAG Chat Assistant")
st.caption("FAISS + Chunking + OpenAI + FastAPI + Streamlit UI")

# ----------------------------
# Sidebar Controls
# ----------------------------
with st.sidebar:
    st.header("⚙️ Controls")

    top_k = st.slider("Top K Chunks", min_value=1, max_value=10, value=3, step=1)

    show_sources = st.checkbox("Show sources", value=True)
    show_source_text = st.checkbox("Show full source text", value=False)

    enable_chat_memory = st.checkbox(
        "Enable chat memory (send previous messages to model)",
        value=False
    )

    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.markdown("✅ API URL:")
    st.code(API_URL)

# ----------------------------
# Session State
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

def format_chat_history(messages: List[Dict]) -> str:
    """
    Convert chat history to a compact text block to send as extra context.
    """
    lines = []
    for m in messages[-8:]:  # last 8 messages for safety
        role = m["role"].upper()
        lines.append(f"{role}: {m['content']}")
    return "\n".join(lines)

# ----------------------------
# Show chat history
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# New message
# ----------------------------
user_input = st.chat_input("Ask something like: What is RAG?")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant message
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Optional: include chat memory by modifying question
                question = user_input
                if enable_chat_memory and len(st.session_state.messages) > 1:
                    history_block = format_chat_history(st.session_state.messages[:-1])
                    question = (
                        f"Conversation history:\n{history_block}\n\n"
                        f"User question:\n{user_input}"
                    )

                payload = {
                    "question": question,
                    "top_k": int(top_k)
                }

                res = requests.post(API_URL, json=payload, timeout=90)
                res.raise_for_status()
                data = res.json()

                answer = data.get("answer", "").strip()
                sources = data.get("sources", [])

                if not answer:
                    answer = "⚠️ No answer returned."

                st.markdown(answer)

                # Sources
                if show_sources:
                    with st.expander("📌 Sources used", expanded=False):
                        for i, s in enumerate(sources, start=1):
                            doc_id = s.get("doc_id")
                            chunk_id = s.get("chunk_id")
                            src = s.get("source")
                            score = s.get("distance", s.get("score"))

                            st.markdown(f"**{i}. {doc_id} | {chunk_id}**")
                            st.caption(f"Source: {src}")
                            st.caption(f"Score/Distance: {score}")

                            if show_source_text:
                                st.markdown(s.get("text", ""))
                            else:
                                # preview
                                preview = (s.get("text", "")[:250] + "...")
                                st.markdown(preview)

                            st.divider()

                # Save assistant answer in chat
                st.session_state.messages.append({"role": "assistant", "content": answer})

            except Exception as e:
                st.error(f"❌ API Error: {e}")
