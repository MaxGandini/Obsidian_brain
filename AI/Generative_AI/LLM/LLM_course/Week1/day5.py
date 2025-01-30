import os
import requests
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

model = 'gpt-4o-mini'
openai = OpenAI()
