import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="HEALTH AI",
    page_icon="🩺",
    layout="wide"
)
st.markdown(
    """
    <style>
    body {
        background-image: url('assets/health_background.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("HealthAI - Intelligent Healthcare Assistant")
st.header("Welcome to HealthAI 🩺")
st.markdown("""
    This is an AI-powered healthcare assistant built with **IBM WatsonX Granite**.
    
    ### Features:
    - Disease Prediction
    - Health Analytics
    - Patient Chat with AI
    - Personalized Treatment Planning
""")
st.image("assets/health_banner.jpeg", use_container_width=True)

