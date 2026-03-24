import pandas as pd

job_data = {

"Data & AI": {

    "Data Scientist": {
        "description": "Analyze complex data to extract insights, build predictive models, and support data-driven decision making.",
        "skills": [
            "python","pandas","numpy","scikit-learn","machine learning",
            "statistics","data visualization","sql","deep learning",
            "tensorflow","pytorch","nlp","feature engineering","model evaluation"
        ]
    },

    "Machine Learning Engineer": {
        "description": "Design, build, and deploy machine learning models into production environments.",
        "skills": [
            "python","tensorflow","pytorch","mlops","docker","kubernetes",
            "model deployment","api","deep learning","data pipelines"
        ]
    },

    "Data Analyst": {
        "description": "Interpret data, create reports, and visualize trends to support business decisions.",
        "skills": [
            "excel","sql","power bi","tableau","python","pandas",
            "data visualization","statistics","reporting","dashboarding"
        ]
    },

    "AI Engineer": {
        "description": "Develop AI systems using deep learning, NLP, and advanced algorithms for intelligent applications.",
        "skills": [
            "python","deep learning","nlp","transformers","llm",
            "tensorflow","pytorch","huggingface","computer vision"
        ]
    }
},

"Software Engineering": {

    "Backend Developer": {
        "description": "Build and maintain server-side logic, APIs, and databases for web applications.",
        "skills": [
            "python","django","flask","api","rest","sql","postgresql",
            "mongodb","authentication","microservices"
        ]
    },

    "Frontend Developer": {
        "description": "Develop user interfaces and enhance user experience for web applications.",
        "skills": [
            "html","css","javascript","react","vue","bootstrap",
            "responsive design","ui/ux","web performance"
        ]
    },

    "Full Stack Developer": {
        "description": "Work on both frontend and backend systems to develop complete web applications.",
        "skills": [
            "html","css","javascript","react","node.js","express",
            "mongodb","sql","api","git"
        ]
    },

    "Software Engineer": {
        "description": "Design, develop, and optimize software systems with strong programming and problem-solving skills.",
        "skills": [
            "data structures","algorithms","oop","system design",
            "python","java","c++","git","debugging"
        ]
    }
},

"Cloud & DevOps": {

    "DevOps Engineer": {
        "description": "Automate and manage infrastructure, CI/CD pipelines, and deployment processes.",
        "skills": [
            "docker","kubernetes","ci/cd","jenkins","github actions",
            "linux","aws","azure","gcp","monitoring"
        ]
    },

    "Cloud Engineer": {
        "description": "Design and manage cloud-based infrastructure and services.",
        "skills": [
            "aws","azure","gcp","cloud architecture","networking",
            "virtual machines","storage","security"
        ]
    },

    "Site Reliability Engineer": {
        "description": "Ensure reliability, scalability, and performance of systems through automation and monitoring.",
        "skills": [
            "linux","monitoring","logging","automation","kubernetes",
            "incident management","scripting"
        ]
    }
},

"Cybersecurity": {

    "Cybersecurity Analyst": {
        "description": "Protect systems and networks by identifying vulnerabilities and responding to security incidents.",
        "skills": [
            "network security","penetration testing","firewalls",
            "siem","risk analysis","cryptography","incident response"
        ]
    },

    "Ethical Hacker": {
        "description": "Simulate cyberattacks to identify and fix security vulnerabilities in systems.",
        "skills": [
            "penetration testing","kali linux","metasploit","burp suite",
            "vulnerability scanning","web security"
        ]
    }
},

"Business & Analytics": {

    "Business Analyst": {
        "description": "Analyze business processes and data to improve efficiency and decision-making.",
        "skills": [
            "excel","sql","data analysis","requirement gathering",
            "stakeholder communication","process modeling"
        ]
    },

    "Product Analyst": {
        "description": "Analyze product performance and user behavior to guide product improvements.",
        "skills": [
            "sql","python","data analysis","a/b testing",
            "product metrics","user behavior analysis"
        ]
    }
}

}

rows = []

for category, roles in job_data.items():
    for role, details in roles.items():
        description = details["description"]
        for skill in details["skills"]:
            rows.append([category, role, description, skill])

df = pd.DataFrame(rows, columns=["category","role","description","skill"])

df.to_csv("skills_database.csv", index=False)