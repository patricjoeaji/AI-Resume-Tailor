from .text_cleaner import clean_text
NOISE_WORDS = {
    "looking", "seeking", "required", "experience", "responsibilities",
    "skills", "requirements", "ability", "work", "team", "role",
    "opportunity", "great", "excellent", "strong"
}
def extract_keywords(job_description):
    tokens = clean_text(job_description)
    keywords = [word for word in tokens if len(word) >= 3 and word not in NOISE_WORDS]
    return keywords