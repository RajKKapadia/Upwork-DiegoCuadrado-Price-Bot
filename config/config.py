import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
AZURE_VERSION = os.getenv('AZURE_VERSION')
AZURE_API_BASE = os.getenv('AZURE_API_BASE')
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
FROM = os.getenv('FROM')
BACKEND_URL = os.getenv('BACKEND_URL')
CONNECTION_STRING = os.getenv('CONNECTION_STRING')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

ERROR_MESSAGE = 'We are facing a techincal issue at this time. Estamos teniendo un problema en este momento, intentalo de nuevo más tarde.'
