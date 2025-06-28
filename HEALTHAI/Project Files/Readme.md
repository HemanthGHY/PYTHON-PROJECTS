# HealthAI - Intelligent Healthcare Assistant 🩺

HealthAI is an AI-powered healthcare assistant built using **IBM WatsonX Granite** and Streamlit. It provides intelligent features to assist patients and healthcare professionals with disease prediction, health analytics, patient chat, and personalized treatment planning.

---

## Features
- **Disease Prediction**: Predict potential diseases based on symptoms.
- **Health Analytics**: Visualize health metrics and trends.
- **Patient Chat**: Interact with an AI assistant for medical queries.
- **Personalized Treatment Planning**: Generate evidence-based treatment plans tailored to individual needs.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/HemanthGHY/PYTHON-PROJECTS.git
   cd healthai
2. Install dependencies:
    pip install -r requirements.txt
3. Run the application:
    streamlit run app.py

### Project Structure:
healthai/
├── [app.py]                   # Main application file
├── pages/                     # Contains individual page files
│   ├── _health_analytics.py   # Health Analytics page
│   ├── patient_chat_page.py   # Patient Chat page
│   ├── disease_predict_page.py # Disease Prediction page
│   ├── treatment_plan_page.py # Treatment Plan page
├── utils/                     # Utility functions
│   ├── prompt_utils.py        # Prompt generation utilities
│   ├── model_utils.py         # IBM WatsonX model utilities
│   ├── data_utils.py          # Data handling utilities
│   ├── visualization_utils.py # Visualization utilities
├── assets/                    # Static assets (images, etc.)
├── ├── style.css              # Css file for Custom styles
│   ├── health_banner.jpeg     # Banner image
├── [requirements.txt]         # Project dependencies
├── [Readme.md]                # Project documentation


### Technologies Used
- **IBM WatsonX Granite**: For AI-powered healthcare assistant capabilities
- **Streamlit**: For building the web application.
- **IBM WatsonX AI**: For AI-powered healthcare functionalities.
- **Pandas**: For data manipulation and analysis.
- **Plotly**: For interactive visualizations.
- **Python Dotenv**: For managing environment variables.

### Environment Variables
    Create a .env file in the root directory with the following variables:

        WATSONX_API_KEY=<your_ibm_watsonx_api_key>
        WATSONX_PROJECT_ID=<your_ibm_watsonx_project_id>

### Contact For questions or feedback, please contact:
- **Name**: Gaddam Hemanth
- **Email**: gaddamhemanthyadav@gmail.com
- **GitHub**: https://github.com/HemanthGHY
