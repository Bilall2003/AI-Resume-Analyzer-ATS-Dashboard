# AI Resume ATS Analyzer

AI Resume ATS Analyzer is a machine learning powered web application that evaluates resumes based on job role requirements and provides actionable improvement suggestions.

The system simulates how Applicant Tracking Systems (ATS) analyze resumes used by modern recruiters.

## Features

Resume Analysis
- Job category and role selection
- Resume upload (PDF / DOCX)
- ATS compatibility score
- Skill matching analysis
- Missing skills detection
- Resume improvement suggestions
- Course recommendations for missing skills

Analytics Dashboard
- Total resumes analyzed
- Average ATS score
- High performing resumes
- Skill distribution insights
- Job category trends
- Resume uploads by month

## Technologies Used

Python  
Streamlit  
Pandas  
NumPy  
Scikit-learn  
NLTK  
Plotly  
PDFPlumber  
Docx2txt  

## Project Structure

resume-ats-analyzer
│
├── app.py
├── pages/
│ ├── resume_analyzer.py
│ └── dashboard.py
│
├── src/
│ ├── resume_parser.py
│ ├── text_cleaner.py
│ ├── skill_matcher.py
│ ├── ats_score.py
│ └── suggestions.py
│
├── data/
│ ├── skills_database.csv
│ └── coursera_courses.csv
│
├── requirements.txt
└── README.md
