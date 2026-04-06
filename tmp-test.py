import google.generativeai as genai
genai.configure(api_key="AIzaSyBfF-iFB8rowso1-lIKxrC53Pv5IzREask")
model = genai.GenerativeModel("gemini-2.5-flash")
try:
    resp = model.generate_content("hello")
    print("SUCCESS", resp.text)
except Exception as e:
    print("FAILED", str(e))
