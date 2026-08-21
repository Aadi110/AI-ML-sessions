import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)


policy_documents = [
    "License renewal needs valid ID + proof of address, costs $45.",
    "Property tax appeals: file within 30 days of notice.",
    "Business permits: processed in 10-15 business days.",
]


def citizen_bot(question):

    context = "\n".join(policy_documents)

    prompt = (
        f"Answer using ONLY this information. "
        f"If the answer is not covered, say you don't know.\n\n"
        f"{context}\n\n"
        f"Question: {question}"
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


# Test the chatbot
print(citizen_bot("How much does license renewal cost?"))