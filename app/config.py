from dotenv import load_dotenv
import os

load_dotenv()  # .env dosyasını oku

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")   # içindeki değeri al   