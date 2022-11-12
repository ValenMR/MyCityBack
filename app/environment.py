from dotenv import load_dotenv, find_dotenv
import os

if not os.getenv("CLOUD_EXECUTION", False):
    load_dotenv(find_dotenv())

# Load environment variables
LEXICA_URL = os.getenv("LEXICA_URL", "")