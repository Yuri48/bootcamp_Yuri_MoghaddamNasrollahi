import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file"""
    load_dotenv()

def get_key(key: str):
    """Fetch a key from environment variables"""
    return os.getenv(key)