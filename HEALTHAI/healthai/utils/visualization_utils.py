import plotly.express as px

def plot_heart_rate(df):
    return px.line(df, x="Date", y="Heart Rate", title="Heart Rate Trend")

def plot_blood_pressure(df):
    return px.line(df, x="Date", y=["Systolic", "Diastolic"], title="Blood Pressure")

def plot_glucose(df):
    fig = px.line(df, x="Date", y="Glucose", title="Glucose Level")
    fig.add_hline(y=100, line_dash="dash", annotation_text="Normal", line_color="green")
    return fig