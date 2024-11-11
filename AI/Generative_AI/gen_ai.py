# Import necessary modules
import kaggle 
import os
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import HTML, Markdown, display

# Load environment variables from the .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise ValueError("GOOGLE_API_KEY is not set in the environment")

from kaggle.kaggle_secrets import UserSecretsClient

GOOGLE_API_KEY=UserSecretsClient().get_secret("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
