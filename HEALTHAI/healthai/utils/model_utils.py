from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
URL = "https://eu-de.ml.cloud.ibm.com" 


def init_granite_model(api_key, project_id):
    try:
        credentials = Credentials(
            url=URL,
            api_key=api_key
        )

        client = APIClient(credentials)

        
        params = {
            "decoding_method": "greedy",
            "max_new_tokens": 200
        }

        model_id = "ibm/granite-3-3-8b-instruct"

        
        model = ModelInference(
            model_id=model_id,
            api_client=client,
            params=params,
            project_id=project_id,
            space_id=None,  
            verify=False    
        )
        return model
    except Exception as e:
        raise ValueError(f"Error initializing model: {str(e)}")

def call_ibm_granite(prompt):
    try:
        model = init_granite_model(API_KEY, PROJECT_ID)
        response = model.generate(prompt)
        return response["results"][0]["generated_text"]
    except Exception as e:
        return f"Error: {str(e)}"