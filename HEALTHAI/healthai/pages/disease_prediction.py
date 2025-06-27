import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import prompt_utils

st.set_page_config(page_title="HealthAI", layout="wide")

st.title("HEALTH AI - INTELLIGENT HEALTHCARE ASSISTANT")
st.sidebar.title("Patient Profile")

if "name" not in st.session_state:
    st.session_state["name"] = ""
if "age" not in st.session_state:
    st.session_state["age"] = 18
if "gender" not in st.session_state:
    st.session_state["gender"] = "Male"
if "medical_history" not in st.session_state:
    st.session_state["medical_history"] = ""
if "recent_symptoms" not in st.session_state:
    st.session_state["recent_symptoms"] = ""
if "avg_heart_rate" not in st.session_state:
    st.session_state["avg_heart_rate"] = 70
if "avg_bp_systolic" not in st.session_state:
    st.session_state["avg_bp_systolic"] = 120
if "avg_bp_diastolic" not in st.session_state:
    st.session_state["avg_bp_diastolic"] = 80
if "avg_glucose" not in st.session_state:
    st.session_state["avg_glucose"] = 90
if "current_symptoms" not in st.session_state:
    st.session_state["current_symptoms"] = ""
if "api_data" not in st.session_state:
    st.session_state["api_data"] = {}

st.session_state["name"] = st.sidebar.text_input("Name", value=st.session_state["name"], key="name_input")
st.session_state["age"] = st.sidebar.number_input("Age", min_value=0, max_value=120, value=st.session_state["age"], step=1, key="age_input")
st.session_state["gender"] = st.sidebar.radio("Gender", options=["Male", "Female"], index=["Male", "Female"].index(st.session_state["gender"]), key="gender_radio")
st.session_state["medical_history"] = st.sidebar.text_area("Medical History", value=st.session_state["medical_history"], placeholder="Enter any relevant medical history here", key="medical_history_input")
st.session_state["recent_symptoms"] = st.sidebar.text_area("Recent Symptoms", value=st.session_state["recent_symptoms"], placeholder="Enter any recent symptoms here", key="recent_symptoms_input")
st.session_state["avg_heart_rate"] = st.sidebar.number_input("Average Heart Rate (bpm)", min_value=40, max_value=200, value=st.session_state["avg_heart_rate"], step=1, key="heart_rate_input")
st.session_state["avg_bp_systolic"] = st.sidebar.number_input("Average Blood Pressure Systolic (mmHg)", min_value=80, max_value=200, value=st.session_state["avg_bp_systolic"], step=1, key="bp_systolic_input")
st.session_state["avg_bp_diastolic"] = st.sidebar.number_input("Average Blood Pressure Diastolic (mmHg)", min_value=40, max_value=120, value=st.session_state["avg_bp_diastolic"], step=1, key="bp_diastolic_input")
st.session_state["avg_glucose"] = st.sidebar.number_input("Average Blood Glucose (mg/dl)", min_value=50, max_value=300, value=st.session_state["avg_glucose"], step=1, key="glucose_input")

st.sidebar.markdown("---")
st.header("Disease Prediction System")
st.subheader("Enter Symptoms and Patient data to receive potential condition predictions.")

st.session_state["current_symptoms"] = st.text_area("Current Symptoms", placeholder="Enter your current symptoms here", key="current_symptoms_input")

if st.button("Generate Prediction", key="generate_prediction_main"):
    if st.session_state["current_symptoms"]:
        prediction= prompt_utils.predict_disease_query(
            symptoms=st.session_state["current_symptoms"],
            age=st.session_state["age"],
            gender=st.session_state["gender"],
            medical_history=st.session_state["medical_history"],
            avg_glucose=st.session_state["avg_glucose"],
            avg_heart_rate=st.session_state["avg_heart_rate"],
            avg_bp_systolic=st.session_state["avg_bp_systolic"],
            avg_bp_diastolic=st.session_state["avg_bp_diastolic"],
            recent_symptoms=st.session_state["recent_symptoms"]
        )
        st.session_state["api_data"] = prediction
        st.write("### Prediction Results")
        st.write(prediction)
        st.success("Prediction generated successfully!")
        st.session_state["current_symptoms"] = ""
        current_symptoms = st.session_state["current_symptoms"]
        
    else:
        st.warning("Please enter symptoms to generate a prediction.")