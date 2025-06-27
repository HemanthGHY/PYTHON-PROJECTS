import os
from dotenv import load_dotenv
from utils.model_utils import call_ibm_granite

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")

if not API_KEY or not PROJECT_ID:
    raise ValueError("Environment variables WATSONX_API_KEY or WATSONX_PROJECT_ID are not set.")

def predict_disease_query(symptoms, age, gender, medical_history, avg_heart_rate, avg_bp_systolic, avg_bp_diastolic, avg_glucose, recent_symptoms):

    prediction_prompt = f"""
    As a medical AI assistant, predict potential health conditions based on the following patient data:
    Current Symptoms: {symptoms}
    Age: {age}
    Gender: {gender}
    Medical History: {medical_history}
    Recent Health Metrics:
    - Average Heart Rate: {avg_heart_rate} bpm
    - Average Blood Pressure: {avg_bp_systolic}/{avg_bp_diastolic} mmHg
    - Average Blood Glucose: {avg_glucose} mg/dl
    - Recently Reported Symptoms: {recent_symptoms}
    Format your response as:
    1. Potential condition name
    2. Likelihood (High/Medium/Low)
    3. Brief explanation
    4. Recommended next steps
    Provide the top 3 most likely conditions based on the data provided."""
    prediction = call_ibm_granite(prompt=prediction_prompt)
    return prediction



def answer_patient_query(query) :
    query_prompt = f"""
    As a healthcare AI assistant, provide a helpful, accurate, and evidence-based response to the following patient question:
    PATIENT QUESTION: {query}
    Provide a clear, empathetic response that:
    - Directly addresses the question
    - Includes relevant medical facts
    - Acknowledges limitations (when appropriate)
    - Suggests when to seek professional medical advice
    - Avoids making definitive diagnoses
    - Uses accessible, non-technical language
    RESPONSE :"""
    answer = call_ibm_granite(prompt=query_prompt)
    return answer

def generate_treatment_plan(condition,age,gender,medical_history):
    treatment_prompt = f"""
    As a medical AI assistant, generate a personalized treatment plan for the following scenario:
    Patient Profile:
    - Condition: {condition}
    - Age: {age}
    - Gender: {gender}
    - Medical History: {medical_history}
    Create a comprehensive, evidence-based treatment plan that includes:
    1. Recommended medications (include dosage guidelines if appropriate)
    2. Lifestyle modifications
    3. Follow-up testing and monitoring
    4. Dietary recommendations
    5. Physical activity guidelines
    6. Mental health considerations
    Format this as a clear, structured treatment plan that follows current medical guidelines while being personalized to this patient's specific needs.
    """
    
    treatment_plan = call_ibm_granite(prompt=treatment_prompt)
    return treatment_plan
