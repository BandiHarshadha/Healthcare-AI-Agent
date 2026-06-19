import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def gemini_diagnosis_agent(symptoms: str):
    if not GEMINI_API_KEY:
        return "Gemini API key is missing. Please add GEMINI_API_KEY in .env file."

    prompt = f"""
You are a safe healthcare AI assistant.

Patient symptoms:
{symptoms}

Give:
1. Possible causes
2. Recommended specialist
3. Home care advice
4. Emergency warning signs

Important:
- Do not give a final diagnosis.
- Tell the user to consult a qualified doctor.
"""

    response = model.generate_content(prompt)
    return response.text