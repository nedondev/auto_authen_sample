from dotenv import load_dotenv
import os

load_dotenv()
#if none exist return None
USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
