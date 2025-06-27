import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import prompt_utils

st.set_page_config(page_title="HealthAI", layout="wide")

st.title("HEALTH AI - INTELLIGENT HEALTHCARE ASSISTANT")
st.sidebar.title("🧑🏻‍⚕️ Patient Profile")

if "name" not in st.session_state:
    st.session_state["name"] = ""
if "age" not in st.session_state:
    st.session_state["age"] = 18
if "gender" not in st.session_state:
    st.session_state["gender"] = "Male"
if "medical_history" not in st.session_state:
    st.session_state["medical_history"] = ""
if "medical_condition" not in st.session_state:
    st.session_state["medical_condition"] = ""

st.session_state["name"] = st.sidebar.text_input("Name", value=st.session_state["name"], key="name_input")
st.session_state["age"] = st.sidebar.number_input("Age", min_value=0, max_value=120, value=st.session_state["age"], step=1, key="age_input")
st.session_state["gender"] = st.sidebar.radio("Gender", options=["Male", "Female"], index=["Male", "Female"].index(st.session_state["gender"]), key="gender_radio")
st.session_state["medical_history"] = st.sidebar.text_area("Medical History", value=st.session_state["medical_history"], placeholder="Enter any relevant medical history here", key="medical_history_input")
st.sidebar.markdown("---")

st.header("Treatment Planning System")
st.subheader("Personalized Treatment Plan Generator.")

st.session_state["medical_condition"] = st.text_area("Medical Condition", placeholder="Enter your Condition", key="medical_condition_input")

if st.button("Generate Treatment", key="generate_prediction_main"):
    if st.session_state["medical_condition"]:
        prediction= prompt_utils.generate_treatment_plan(
            age=st.session_state["age"],
            gender=st.session_state["gender"],
            medical_history=st.session_state["medical_history"],
            condition=st.session_state["medical_condition"]  
        )
        st.write("### Prediction Results")
        st.write(prediction)
        st.success("Prediction generated successfully!")
    else:
        st.warning("Please enter medical conditions to generate a Treatment Plan.")