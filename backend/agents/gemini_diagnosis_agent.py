import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def gemini_diagnosis_agent(symptoms):
    prompt = f"""
You are a healthcare assistant.

Patient symptoms:
{symptoms}

Provide:
1. Possible causes.
2. Recommended specialist.
3. Home care advice.
4. When to seek urgent care.

Do NOT give a final diagnosis.
Always advise consulting a doctor.
"""

    response = model.generate_content(prompt)

    return response.text