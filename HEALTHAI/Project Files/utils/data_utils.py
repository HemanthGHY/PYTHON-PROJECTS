import pandas as pd

def get_sample_health_data():
    return pd.DataFrame({
        "Date": pd.date_range(start="2025-06-01", periods=7),
        "Heart Rate": [72, 75, 78, 76, 74, 77, 79],
        "Systolic": [120, 122, 121, 118, 119, 123, 121],
        "Diastolic": [80, 82, 79, 81, 83, 80, 78],
        "Glucose": [98, 97, 101, 99, 96, 102, 100]
    })

def summarize_metrics(df):
    return {
        "Avg Heart Rate": f"{df['Heart Rate'].mean():.2f} bpm",
        "Avg Glucose": f"{df['Glucose'].mean():.2f} mg/dL"
    }