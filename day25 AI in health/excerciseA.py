import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found")

# Create Gemini client
client = genai.Client(api_key=api_key)

TRIAGE_PROMPT = """
You are a symptom triage assistant, NOT a doctor.

Classify the urgency of the user's symptoms as:

LOW
MEDIUM
HIGH
EMERGENCY

Give a short explanation for the classification.

Always include this disclaimer:

"This information is for general guidance only and is not a medical diagnosis. Please consult a qualified healthcare professional for medical advice."

If the symptoms may indicate an emergency, clearly tell the user to seek emergency medical care immediately.
"""


def triage(symptom_description):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=symptom_description,
        config=types.GenerateContentConfig(
            system_instruction=TRIAGE_PROMPT
        )
    )

    return response.text


print(triage("Mild headache since this morning."))