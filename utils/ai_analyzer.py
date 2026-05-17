import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# .env file se variables load karne ke liye
load_dotenv()

# API Key check
api_key = os.getenv("AIzaSyBwjRRXew7IEiwJ3J_P6uhIKkQb9YY2e-4")
if not api_key:
    # Agar .env file na chal rahi ho to fallback key
    api_key = "AIzaSyBwjRRXew7IEiwJ3J_P6uhIKkQb9YY2e-4"

# Bilkul simple configuration bina kisi extra options ke
genai.configure(api_key=api_key)

# v1beta aur standard libraries dono ke liye sub se behtar model calling string
model = genai.GenerativeModel('models/gemini-2.5-flash')

def analyze_resume(resume_text):
    # Prompt ko optimize kiya hai taake bina Job Description ke bhi 100 mein se numeric score mile
    prompt = f"""
    Analyze this resume as an expert ATS (Applicant Tracking System).
    
    CRITICAL INSTRUCTION: Calculate a general ATS score out of 100 based on standard industry expectations, formatting, keyword density, and structural quality. Do NOT return text like 'Cannot be calculated without a job description'. Provide a realistic numeric percentage score (e.g., '75%').
    
    Return ONLY valid JSON matching this schema:
    {{
        "ats_score": "Provide the numeric percentage score here",
        "skills": [],
        "missing_skills": ["List general highly-demanded skills in their field that are missing here"],
        "job_recommendations": ["Suggest 2-3 suitable roles based on their experience"],
        "strengths": [],
        "weaknesses": [],
        "summary": "A brief overview of the candidate's profile"
    }}
    
    Resume:
    {resume_text}
    """
    
    # AI se response generate karwana
    response = model.generate_content(prompt)
    content = response.text
    
    # Markdown symbols (```json) ko saaf karna
    content = content.replace("```json", "").replace("```", "").strip()
    
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("Error: Model returned invalid JSON")
        return {"error": "Invalid JSON response from AI", "raw_content": content}