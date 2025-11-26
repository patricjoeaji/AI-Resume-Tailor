from pyPDF2 import PdfReader
from modules.text_cleaner import clean_text
from modules.keyword_extractor import extract_keywords
from modules.matcher import match_keywords
from modules.resume_builder import build_tailored_resume
def read_resume_from_pdf(pdf_path):
    reader=PdfReader(pdf_path)
    full_text=""
    for page in reader.pages:
        full_text+=page.extract_text()+"\n"
    return full_text
def main():
    pdf_path=input("Enter the path to your resume PDF file: ").strip()
    try:
        resume_text=read_resume_from_pdf(pdf_path)
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return
    print("resume text extracted successfully.")
    print("\nPaste the Job Description (type END on a new line to finish):")
    print("--------------------------------------------------")

    jd_lines = []

    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        jd_lines.append(line)
    job_description = "\n".join(jd_lines)

    if not job_description.strip():
        print("\n❌ Job Description cannot be empty.")
        return
    resume_tokens=clean_text(resume_text)
    jd_keywords=extract_keywords(job_description)
    match_result=match_keywords(resume_tokens,jd_keywords)
    final_output=build_tailored_resume(resume_text,match_result)
    print("\n========== TAILORED RESUME OUTPUT ==========\n")
    print(final_output)
    print("\n========== END ==========\n")
