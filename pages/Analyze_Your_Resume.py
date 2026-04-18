import streamlit as st
import pandas as pd
from parser_utils import run_regex_analysis
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# ---------------- STYLES ----------------
st.markdown("""
    <style>
    .green-box {
        background: linear-gradient(45deg, rgba(0, 240, 219, 0.7) 100%, rgba(0, 131, 176, 0.05) 100%);
        padding: 30px;
        border-radius: 12px;
        color: white;
        max-width: 1290px;
        margin-top: 20px;
        margin-bottom: 40px;
        display: flex;
        justify-content: flex-start;
        text-align: center;
    }
    .green-box h2 {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .green-box p {
        font-size: 1.2rem;
        line-height: 4.5;
    }
    .thrd-box {
        background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        max-width: 1300px;
        margin-top: 35px;
        margin-bottom: 35px;
        overflow: hidden;
    }
    .thrd-box h2 {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .thrd-box p {
        font-size: 1.1rem;
        line-height: 1.5;
    }
    .tag {
        display: inline-block;
        background: rgba(0, 200, 180, 0.2);
        border: 1px solid rgba(0, 200, 180, 0.5);
        border-radius: 6px;
        padding: 2px 10px;
        margin: 3px;
        font-size: 0.9rem;
        color: white;
    }
    .skill-box {
        background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        max-width: 520px;
        margin-top: 35px;
        overflow: hidden;
        transition: 0.1s;
    }
    .skill-box:hover {
        cursor: pointer;
        transform: scale(1.02);
        border: 3px solid #6dd5ed;
    }
    .skill-box h3 {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 6px;
    }
    .skill-box p {
        font-size: 1rem;
        line-height: 1.5;
    }
    [data-testid="stVerticalBlock"] > div:has(.stFileUploader) {
        background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);
        padding: 20px;
        border-radius: 12px;
        max-width: 1300px;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
    <div class="green-box">
        <h2>Resume Analyzer</h2>
        <p>Get instant AI-powered feedback to optimize your resume</p>
    </div>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
data = pd.read_csv("data/skills_database.csv")

categories = data["category"].unique()
job_cat = st.selectbox("Job Category", categories)

filtered_roles = data[data["category"] == job_cat]["role"].unique()
selected_role = st.selectbox("Specific Role", filtered_roles)

selected_des = data.loc[data["role"] == selected_role, "description"].values[0]
skills_array = data.loc[data["role"] == selected_role, "skill"].unique()

skills_html = ", ".join([f"<span class='tag'>{s}</span>" for s in skills_array])

# ---------------- ROLE BOX ----------------
st.markdown(f"""
    <div class="thrd-box">
        <h2>{selected_role}</h2>
        <p>{selected_des}</p>
        <h2>Required Skills:</h2>
        <p>{skills_html}</p>
    </div>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
st.caption("🧾 Upload your resume to get started with AI-powered analysis")
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

# ---------------- ANALYSIS ----------------
if uploaded_file:
    st.success("Resume data saved Successfully....")
    results = run_regex_analysis(uploaded_file)
    resume_text = results["text"].lower()

    required_skills = [s.lower() for s in skills_array]

    # FIX 1: Do NOT convert matched_skills to string
    matched_skills = [s for s in required_skills if s in resume_text]
    # FIX 2: missing_skills now correctly compares two lists
    missing_skills = list(set(required_skills) - set(matched_skills))

    # FIX 3: ats_score now correctly uses list length
    ats_score = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0

    # FIX 4: Render skills as HTML tags, not raw Python lists
    matched_html = ", ".join([f"<span class='tag'>{s}</span>" for s in matched_skills]) or "<em>None found</em>"
    missing_html = ", ".join([f"<span class='tag'>{s}</span>" for s in missing_skills]) or "<em>None — great job!</em>"

    # ---------------- DONUT CHART ----------------
    def draw_donut(score):
        fig, ax = plt.subplots(figsize=(4, 4))
        sizes = [score, 100 - score]
        colors = ["#00f0db", "#2a2a2a"]
        ax.pie(
            sizes,
            startangle=90,
            wedgeprops=dict(width=0.3),
            colors=colors
        )
        ax.text(0, 0, f"{int(score)}%", ha="center", va="center", fontsize=18, color="white")
        ax.axis("equal")
        fig.patch.set_alpha(0)
        return fig

    # ---------------- STATUS ----------------
    if ats_score < 40:
        status = "Needs Improvement"
        color = "red"
    elif ats_score < 70:
        status = "Average"
        color = "orange"
    else:
        status = "Good"
        color = "green"

    # ---------------- LAYOUT ----------------
    col1, col2 = st.columns([1.2, 1.8])

    # ========== LEFT COLUMN ==========
    with col1:
        st.subheader("ATS Score")
        fig = draw_donut(ats_score)
        st.pyplot(fig)
        st.markdown(f'<p style="color:{color}; font-weight:bold;">{status}</p>', unsafe_allow_html=True)

        # FIX 5: Skill box is now inside col1
        st.markdown(f"""
            <div class="skill-box">
                <h3>Keyword Match</h3>
                <p>{int(ats_score)}%</p>
                <h3>Skills Match</h3>
                <p>{matched_html}</p>
                <h3>Missing Skills</h3>
                <p>{missing_html}</p>
            </div>
        """, unsafe_allow_html=True)

    # ========== FORMAT ANALYSIS LOGIC ==========
    import re

    # --- Section detection ---
    section_keywords = {
        "contact":     ["phone", "email", "linkedin", "github", "address", "portfolio"],
        "summary":     ["summary", "objective", "profile", "about me", "overview"],
        "experience":  ["experience", "work history", "employment", "internship", "intern"],
        "education":   ["education", "degree", "university", "college", "bachelor", "master", "phd"],
        "skills":      ["skills", "technologies", "tech stack", "tools", "competencies"],
        "projects":    ["projects", "personal projects", "academic projects", "portfolio"],
        "certifications": ["certification", "certificate", "certified", "credential", "license"],
        "achievements":["achievements", "awards", "honors", "accomplishments"],
    }

    found_sections = {}
    for section, keywords in section_keywords.items():
        found_sections[section] = any(kw in resume_text for kw in keywords)

    sections_found_count = sum(found_sections.values())
    section_score = int((sections_found_count / len(section_keywords)) * 100)

    # --- Format checks ---
    format_checks = {
        "email_present":    bool(re.search(r"[\w\.-]+@[\w\.-]+\.\w+", resume_text)),
        "phone_present":    bool(re.search(r"(\+?\d[\d\s\-().]{7,}\d)", resume_text)),
        "linkedin_present": "linkedin" in resume_text,
        "github_present":   "github" in resume_text,
        "bullet_points":    resume_text.count("•") + resume_text.count("-") > 3,
        "quantified_results": bool(re.search(r"\d+\s*(%|x|times|users|clients|projects|years|months|k\b|\$)", resume_text)),
        "action_verbs":     any(v in resume_text for v in [
                                "developed", "built", "designed", "led", "managed", "improved",
                                "implemented", "created", "achieved", "delivered", "optimized",
                                "increased", "reduced", "launched", "collaborated"]),
        "decent_length":    len(resume_text.split()) >= 200,
    }

    format_score = int((sum(format_checks.values()) / len(format_checks)) * 100)

    # ========== RIGHT COLUMN ==========
    with col2:

        # --- Format Analysis Card ---
        st.subheader("Format Analysis")

        fc = format_checks
        fs_color = "green" if format_score >= 70 else ("orange" if format_score >= 40 else "red")
        ss_color = "green" if section_score >= 70 else ("orange" if section_score >= 40 else "red")

        st.markdown(f"""
            <style>
            .analysis-card {{
                background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);
                padding: 20px;
                border-radius: 12px;
                color: white;
                margin-bottom: 20px;
            }}
            .score-row {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }}
            .score-label {{ font-size: 1rem; }}
            .score-bar-bg {{
                flex: 1;
                height: 10px;
                background: rgba(255,255,255,0.15);
                border-radius: 6px;
                margin: 0 12px;
                overflow: hidden;
            }}
            .score-bar-fill {{
                height: 100%;
                border-radius: 6px;
            }}
            .score-val {{ font-size: 1rem; font-weight: bold; min-width: 40px; text-align:right; }}
            .check-row {{ display:flex; align-items:center; gap:8px; font-size:0.9rem; margin: 4px 0; }}
            .check-icon {{ font-size: 1rem; }}
            </style>

            <div class="analysis-card">
                <div class="score-row">
                    <span class="score-label">Format Score</span>
                    <div class="score-bar-bg">
                        <div class="score-bar-fill" style="width:{format_score}%; background:{fs_color};"></div>
                    </div>
                    <span class="score-val" style="color:{fs_color};">{format_score}%</span>
                </div>
                <div class="score-row">
                    <span class="score-label">Section Score</span>
                    <div class="score-bar-bg">
                        <div class="score-bar-fill" style="width:{section_score}%; background:{ss_color};"></div>
                    </div>
                    <span class="score-val" style="color:{ss_color};">{section_score}%</span>
                </div>
                <hr style="border-color:rgba(255,255,255,0.1); margin: 12px 0;">
                <div class="check-row"><span class="check-icon">{'✅' if fc['email_present'] else '❌'}</span> Email address</div>
                <div class="check-row"><span class="check-icon">{'✅' if fc['phone_present'] else '❌'}</span> Phone number</div>
                <div class="check-row"><span class="check-icon">{'✅' if fc['linkedin_present'] else '❌'}</span> LinkedIn profile</div>
                <div class="check-row"><span class="check-icon">{'✅' if fc['github_present'] else '❌'}</span> GitHub profile</div>
                <div class="check-row"><span class="check-icon">{'✅' if fc['bullet_points'] else '❌'}</span> Bullet points used</div>
                <div class="check-row"><span class="check-icon">{'✅' if fc['quantified_results'] else '❌'}</span> Quantified achievements (numbers/metrics)</div>
                <div class="check-row"><span class="check-icon">{'✅' if fc['action_verbs'] else '❌'}</span> Action verbs used</div>
                <div class="check-row"><span class="check-icon">{'✅' if fc['decent_length'] else '❌'}</span> Sufficient content (200+ words)</div>
            </div>
        """, unsafe_allow_html=True)

        # --- Sections Found ---
        st.subheader("Sections Detected")
        section_icons = {
            "contact": "📞", "summary": "📝", "experience": "💼",
            "education": "🎓", "skills": "🛠️", "projects": "🚀",
            "certifications": "🏅", "achievements": "🏆"
        }
        cols = st.columns(4)
        for i, (sec, found) in enumerate(found_sections.items()):
            icon = section_icons.get(sec, "📄")
            badge_color = "rgba(0,200,100,0.25)" if found else "rgba(200,50,50,0.2)"
            border_color = "#00c864" if found else "#c83232"
            with cols[i % 4]:
                st.markdown(f"""
                    <div style="background:{badge_color}; border:1px solid {border_color};
                                border-radius:8px; padding:8px 10px; text-align:center;
                                font-size:0.85rem; color:white; margin-bottom:8px;">
                        {icon} {sec.capitalize()}
                    </div>
                """, unsafe_allow_html=True)

        # --- Improvement Suggestions ---
        st.subheader("Resume Improvement Suggestions")

        suggestions = []

        # Contact
        contact_tips = []
        if not fc["email_present"]:
            contact_tips.append("Add your email address")
        if not fc["phone_present"]:
            contact_tips.append("Add your phone number")
        if not fc["linkedin_present"]:
            contact_tips.append("Add your LinkedIn profile URL")
        if not fc["github_present"]:
            contact_tips.append("Add your GitHub profile link")
        if contact_tips:
            suggestions.append(("📞 Contact Information", contact_tips))

        # Summary
        if not found_sections["summary"]:
            suggestions.append(("📝 Professional Summary", [
                "Add a professional summary to highlight your key qualifications and career goals"
            ]))

        # Experience
        if not found_sections["experience"]:
            suggestions.append(("💼 Experience", [
                "Add a work experience or internship section"
            ]))
        else:
            exp_tips = []
            if not fc["quantified_results"]:
                exp_tips.append("Quantify your achievements (e.g. 'Improved performance by 30%')")
            if not fc["action_verbs"]:
                exp_tips.append("Start bullet points with strong action verbs (e.g. Built, Led, Designed)")
            if exp_tips:
                suggestions.append(("💼 Experience Quality", exp_tips))

        # Education
        if not found_sections["education"]:
            suggestions.append(("🎓 Education", ["Add your education section with degree and institution"]))

        # Skills
        if missing_skills:
            suggestions.append(("🛠️ Skills to Add", [f"`{s}`" for s in sorted(missing_skills)]))
        else:
            suggestions.append(("🛠️ Skills Section", ["Great job! All key skills are present in your resume."]))

        # Projects
        if not found_sections["projects"]:
            suggestions.append(("🚀 Projects", [
                "Add a projects section to showcase hands-on work, especially relevant to this role"
            ]))

        # Certifications
        if not found_sections["certifications"]:
            suggestions.append(("🏅 Certifications", [
                "Consider adding relevant certifications to strengthen your profile"
            ]))

        # Length
        if not fc["decent_length"]:
            suggestions.append(("📄 Content Length", [
                "Your resume appears too short — expand your experience and project details"
            ]))

        # Render suggestions
        for title, tips in suggestions:
            st.markdown(f"### {title}")
            for tip in tips:
                st.write(f"• {tip}")
                
    st.markdown(f"""
            <div class="thrd-box">
            <h2> 📚Recommended Courses </h2>
            </div>
        """, unsafe_allow_html=True)
    
    
    st.markdown(f"""
            <div class="thrd-box">
            <h2> 💁🏻‍♀️Helpful Videos</h2>
            </div>
        """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Resume Tips", "Interview Tips"])

    with tab1:
        st.subheader("Resume Writing")
        st.subheader("Resume Design")

    with tab2:
        st.write("Interview Tips")
        
        

else:
    st.info("Upload your resume to see ATS analysis")
