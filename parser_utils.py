import re
import pdfplumber

def run_regex_analysis(uploaded_file):
    # 1. Extract Text (Keep it here to keep the main page clean)
    with pdfplumber.open(uploaded_file) as pdf:
        text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    
    # 2. Regex Patterns
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_pattern = r'\b(?:\+?\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}\b'
    linkedin_pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/in/[\w\-\_]+'
    
    # 3. Execution
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    links = re.findall(linkedin_pattern, text)
    
    return {
        "text": text,
        "emails": emails,
        "phones": phones,
        "links": links
    }