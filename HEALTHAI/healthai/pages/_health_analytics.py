import streamlit as st
from utils import prompt_utils, data_utils, visualization_utils
st.set_page_config("HealthAI", layout="wide")
st.title("HEALTH AI - INTELLIGENT HEALTHCARE ASSISTANT")
st.header("📊 Health Analytics Dashboard")
df = data_utils.get_sample_health_data()
st.subheader("Sample Health Data")
st.dataframe(df)
st.subheader("Summary Metrics")
summary = data_utils.summarize_metrics(df)
st.json(summary)
st.subheader("Heart Rate Trend")
heart_rate_fig = visualization_utils.plot_heart_rate(df)
st.plotly_chart(heart_rate_fig, use_container_width=True)
st.subheader("Blood Pressure Trend")
bp_fig = visualization_utils.plot_blood_pressure(df)
st.plotly_chart(bp_fig, use_container_width=True)
st.subheader("Glucose Level Trend")
glucose_fig = visualization_utils.plot_glucose(df)
st.plotly_chart(glucose_fig, use_container_width=True)
st.markdown("""
### Note:
This is sample health data for demonstration purposes.
""")
st.markdown("### HealthAI Dashboard")
st.markdown("""
            ### Contact:
            - Email: gaddamhemanthyadav@gmail.com 
            - Phone: 6281119496
            - Address:  SVCE
            """)