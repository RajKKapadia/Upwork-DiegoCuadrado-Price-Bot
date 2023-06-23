import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
FROM = os.getenv('FROM')
BACKEND_URL = os.getenv('BACKEND_URL')
