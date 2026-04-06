import google.generativeai as genai

genai.configure(api_key="AIzaSyCyvN-KyaJac3k9I7rOVvnfCXHPayRGxmc")

model = genai.GenerativeModel("gemini-pro")

def generate_ai_explanation(age, glucose, pulse, blink, meal_gap, symptom, risk):
    prompt = f"""
Explain this hypoglycemia risk in simple terms:

Age: {age}
Glucose: {glucose}
Pulse: {pulse}
Blink: {blink}
Meal gap: {meal_gap}
Symptom: {symptom}
Risk: {risk}

Give:
1. Reason
2. What to do
3. Safety note
"""

    response = model.generate_content(prompt)
    return response.text