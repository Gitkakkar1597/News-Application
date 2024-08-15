# config/config.py
from dotenv import load_dotenv
import os

def load_env_vars():
    load_dotenv()
    return {
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),
        'NEWS_API_KEY': os.getenv('NEWS_API_KEY')
    }
