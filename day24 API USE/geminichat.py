import os

from google import genai
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "Set the GEMINI_API_KEY environment variable before running this program."
    )

client = genai.Client(api_key=api_key)
# Initialize the chat session (it automatically maintains history)
conversation = client.chats.create(model="gemini-3.6-flash")

def chat(user_input):
    response = conversation.send_message(user_input)
    return response.text

print("Chat started! Type 'exit' or 'quit' to stop.\n")

# Main continuous conversation loop
while True:
    user_input = input("You: ")
    
    # Check if the user wants to end the conversation
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Ending chat. Goodbye!")
        break
    
    # Ignore empty inputs
    if not user_input.strip():
        continue

    response = chat(user_input)
    print(f"Gemini: {response}\n")
    