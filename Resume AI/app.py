from flask import Flask, render_template, request
import os

from utils.resume_parser import extract_text_from_resume
from utils.ai_analyzer import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    if 'resume' not in request.files:
        return "No file uploaded"

    file = request.files['resume']

    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    resume_text = extract_text_from_resume(filepath)

    result = analyze_resume(resume_text)

    return render_template(
        'result.html',
        result=result
    )

if __name__ == '__main__':
    app.run(debug=True)