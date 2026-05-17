import google.generativeai as genai

genai.configure(api_key="AIzaSyBwjRRXew7IEiwJ3J_P6uhIKkQb9YY2e-4")

for model in genai.list_models():
    print(model.name)