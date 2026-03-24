import pandas as pd

job_data = {

"Data & AI": {

    "Data Scientist": [
        "python","pandas","numpy","scikit-learn","machine learning",
        "statistics","data visualization","sql","deep learning",
        "tensorflow","pytorch","nlp","feature engineering","model evaluation"
    ],

    "Machine Learning Engineer": [
        "python","tensorflow","pytorch","mlops","docker","kubernetes",
        "model deployment","api","deep learning","data pipelines"
    ],

    "Data Analyst": [
        "excel","sql","power bi","tableau","python","pandas",
        "data visualization","statistics","reporting","dashboarding"
    ],

    "AI Engineer": [
        "python","deep learning","nlp","transformers","llm",
        "tensorflow","pytorch","huggingface","computer vision"
    ]
},

"Software Engineering": {

    "Backend Developer": [
        "python","django","flask","api","rest","sql","postgresql",
        "mongodb","authentication","microservices"
    ],

    "Frontend Developer": [
        "html","css","javascript","react","vue","bootstrap",
        "responsive design","ui/ux","web performance"
    ],

    "Full Stack Developer": [
        "html","css","javascript","react","node.js","express",
        "mongodb","sql","api","git"
    ],

    "Software Engineer": [
        "data structures","algorithms","oop","system design",
        "python","java","c++","git","debugging"
    ]
},

"Cloud & DevOps": {

    "DevOps Engineer": [
        "docker","kubernetes","ci/cd","jenkins","github actions",
        "linux","aws","azure","gcp","monitoring"
    ],

    "Cloud Engineer": [
        "aws","azure","gcp","cloud architecture","networking",
        "virtual machines","storage","security"
    ],

    "Site Reliability Engineer": [
        "linux","monitoring","logging","automation","kubernetes",
        "incident management","scripting"
    ]
},

"Cybersecurity": {

    "Cybersecurity Analyst": [
        "network security","penetration testing","firewalls",
        "siem","risk analysis","cryptography","incident response"
    ],

    "Ethical Hacker": [
        "penetration testing","kali linux","metasploit","burp suite",
        "vulnerability scanning","web security"
    ]
},

"Business & Analytics": {

    "Business Analyst": [
        "excel","sql","data analysis","requirement gathering",
        "stakeholder communication","process modeling"
    ],

    "Product Analyst": [
        "sql","python","data analysis","a/b testing",
        "product metrics","user behavior analysis"
    ]
}

}

rows = []

for category, roles in job_data.items():
    for role, skills in roles.items():
        for skill in skills:
            rows.append([category, role, skill])

df = pd.DataFrame(rows, columns=["category","role","skill"])

df.to_csv("skills_database.csv", index=False)
