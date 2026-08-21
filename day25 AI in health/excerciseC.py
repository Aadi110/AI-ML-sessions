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



def generate_quiz(topic, num_questions=3):
    prompt = f"""
Create {num_questions} multiple-choice questions about {topic}.

For each question include:
1. The question
2. Four options (A, B, C, D)
3. The correct answer
4. A one-sentence explanation
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


def grade_short_answer(question, student_answer, correct):

    prompt = f"""
Q: {question}
Correct Answer: {correct}
Student Answer: {student_answer}

Give constructive feedback, not just correct/incorrect.
Explain briefly what the student got right or wrong.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


# Test quiz generation
print("===== QUIZ =====")

quiz = generate_quiz("Python programming", 3)

print(quiz)


# Test short-answer grading
print("\n===== SHORT ANSWER GRADING =====")

question = "What is a list in Python?"
student_answer = "A list stores multiple values in one variable."
correct = "A list is an ordered, mutable collection that can store multiple values."

feedback = grade_short_answer(
    question,
    student_answer,
    correct
)

print(feedback)