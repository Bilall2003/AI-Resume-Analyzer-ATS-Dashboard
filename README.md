<div align="center">

# 🧠 AI Resume ATS Analyzer

### Intelligent Resume Screening & ATS Score Prediction

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">

<p>
A Machine Learning powered web application that analyzes resumes, predicts ATS compatibility,
identifies missing skills, and provides personalized recommendations to improve hiring chances.
</p>

</div>

---

# 📖 Overview

Modern companies use **Applicant Tracking Systems (ATS)** to filter resumes before they reach recruiters.

**AI Resume ATS Analyzer** simulates this process by evaluating resumes against selected job roles and provides intelligent insights including:

-  ATS Compatibility Score
-  Skill Matching Analysis
-  Missing Skills Detection
-  Resume Improvement Suggestions
-  Learning Resource Recommendations
-  Analytics Dashboard

---

# ✨ Features

## 📄 Resume Analysis

- Upload Resume (**PDF / DOCX**)
- Select Job Category & Role
- ATS Compatibility Score
- Skill Match Percentage
- Missing Skills Detection
- Personalized Resume Suggestions
- Recommended Courses for Missing Skills

---

## 📊 Analytics Dashboard

Visualize resume insights with interactive charts.

Features include:

- 📈 Total Resumes Analyzed
- ⭐ Average ATS Score
- 🏆 High Performing Resumes
- 📊 Skill Distribution
- 💼 Job Category Trends
- 📅 Resume Upload Trends

---

# 🖥️ Application Workflow

```text
                 Resume Upload
                       │
                       ▼
             Text Extraction
          (PDF / DOCX Parsing)
                       │
                       ▼
              Text Cleaning
                       │
                       ▼
             Skill Extraction
                       │
                       ▼
          ATS Score Calculation
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
 Missing Skills              Skill Matching
        │                             │
        └──────────────┬──────────────┘
                       ▼
        Suggestions & Course Recommendation
```

---

# 🛠️ Tech Stack

<table>
<tr>
<td><b>Language</b></td>
<td>Python</td>
</tr>

<tr>
<td><b>Framework</b></td>
<td>Streamlit</td>
</tr>

<tr>
<td><b>Machine Learning</b></td>
<td>Scikit-learn</td>
</tr>

<tr>
<td><b>Data Processing</b></td>
<td>Pandas, NumPy</td>
</tr>

<tr>
<td><b>NLP</b></td>
<td>NLTK</td>
</tr>

<tr>
<td><b>Visualization</b></td>
<td>Plotly</td>
</tr>

<tr>
<td><b>Document Parsing</b></td>
<td>PDFPlumber, Docx2txt</td>
</tr>

</table>

---

# 📂 Project Structure

```text
resume-ats-analyzer/
│
├── app.py
│
├── pages/
│   ├── resume_analyzer.py
│   └── dashboard.py
│
├── src/
│   ├── resume_parser.py
│   ├── text_cleaner.py
│   ├── skill_matcher.py
│   ├── ats_score.py
│   └── suggestions.py
│
├── data/
│   ├── skills_database.csv
│   └── coursera_courses.csv
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-ats-analyzer.git

cd resume-ats-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---


# 🎯 ATS Evaluation Includes

✔ Resume Parsing

✔ Keyword Matching

✔ Skills Analysis

✔ Missing Skills Detection

✔ ATS Compatibility Score

✔ Resume Suggestions

✔ Course Recommendations

---

# 📊 Future Improvements

- AI Resume Rewriting
- Cover Letter Generator
- Resume Ranking
- LinkedIn Profile Analysis
- Interview Question Generator
- GPT-powered Resume Feedback
- Multi-language Resume Support

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---



