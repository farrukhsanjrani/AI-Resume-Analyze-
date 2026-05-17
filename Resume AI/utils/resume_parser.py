import os
from docx import Document
import PyPDF2

def extract_text_from_pdf(file_path):
    """PDF file se text nikalne ke liye"""
    text = ""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"PDF Parsing Error: {e}")
    return text

def extract_text_from_docx(file_path):
    """Word (.docx) file se text nikalne ke liye"""
    text = ""
    try:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            if paragraph.text:
                text += paragraph.text + "\n"
    except Exception as e:
        print(f"DOCX Parsing Error: {e}")
    return text

# Is function ka naam humne wapas 'extract_text_from_resume' kar diya hai
# taake aapki app.py file bina crash kiye isko direct import kar sake.
def extract_text_from_resume(file_path):
    """Main function jo file extension dekh kar sahi parser chalaye ga"""
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext in ['.docx', '.doc']:
        return extract_text_from_docx(file_path)
    else:
        print(f"Unsupported file format: {ext}")
        return ""