import os
import re

# Optional PDF and DOCX support
try:
    import docx2txt
    import PyPDF2
except ImportError:
    print("You can install docx2txt and PyPDF2 if you want to analyze DOCX/PDF files.")

# === Skills to check for ===
required_skills = ["python", "sql", "html", "css", "javascript", "django", "excel"]

def extract_text_from_file(file_path):
    text = ""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

    elif ext == ".docx":
        try:
            text = docx2txt.process(file_path)
        except:
            print("⚠️ Error reading DOCX file.")

    elif ext == ".pdf":
        try:
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
        except:
            print("⚠️ Error reading PDF file.")

    else:
        print("❌ Unsupported file format.")
    
    return text.lower()

def analyze_resume(file_path):
    resume_text = extract_text_from_file(file_path)

    if not resume_text:
        print("❌ Could not extract text.")
        return

    print("\n🔍 Analyzing resume for skills:\n")

    found = []
    missing = []

    for skill in required_skills:
        if re.search(rf'\b{skill}\b', resume_text):
            found.append(skill)
        else:
            missing.append(skill)

    print(f"✅ Skills found: {', '.join(found)}")
    print(f"❌ Skills missing: {', '.join(missing)}")

# === Run Analyzer ===
file_path = input("Enter path to resume (.txt, .pdf, .docx): ").strip()
analyze_resume(file_path)
