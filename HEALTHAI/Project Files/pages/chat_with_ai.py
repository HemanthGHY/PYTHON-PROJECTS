import streamlit as st
from utils.prompt_utils import answer_patient_query
from utils.model_utils import call_ibm_granite

st.title("HEALTH AI - INTELLIGENT HEALTHCARE ASSISTANT")
st.header("🗣 Patient Chat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def handle_send():
    question = st.session_state.user_question.strip()
    if question:
        try:
            prompt = answer_patient_query(question)
            reply = call_ibm_granite(prompt)
            st.session_state.chat_history.append((question, reply))
            st.session_state.user_question = "" 
        except Exception as e:
            st.error(f"Error generating chat response: {str(e)}")

st.subheader("Chat History")
for q, a in reversed(st.session_state.chat_history):
    st.write(f"**You:** {q}")
    st.write(f"**AI:** {a}")

st.text_input("Ask a medical question:", key="user_question", on_change=handle_send)
