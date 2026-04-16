import streamlit as st
import pandas as pd
from parser_utils import run_regex_analysis
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
            <style>

            .green-box {
                background: linear-gradient(45deg, rgba(0, 240, 219, 0.7) 100%, rgba(0, 131, 176, 0.05) 100%);    
                padding:30px;     
                width:2500px; 
                border-radius: 12px;
                color: white;
                max-width: 1290px;
                margin-top: 20px;
                margin-bottom: 40px;
                display:flex;
                justify-content:flex-start;
                text-align:center;
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
            </style>

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
        <style>
        .thrd-box {{
        background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%); 
        padding: 20px;
        width:2500px;
        border-radius: 12px;
        color: white;
        max-width: 1300px; 
        margin-top: 35px;
        margin-bottom: 35px;
        overflow:hidden;
        }}

        .thrd-box h2 {{
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 10px;
        }}

        .thrd-box p {{
            font-size: 1.1rem;
            line-height: 1.5;
        }}
        </style>
        
        <div class="thrd-box">
            <h2>{selected_role}</h2>
            <p>{selected_des}</p>
            <h2>Required Skills:</h2>
            <p>{skills_html}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- UPLOAD BOX STYLE ----------------
st.markdown("""
    <style>
    [data-testid="stVerticalBlock"] > div:has(.stFileUploader) {
       background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%); 
        padding: 20px;
        width:2500px;
        border-radius: 12px;
        color: white;
        max-width: 1300px; 
        overflow:hidden;
    }
    </style>
""", unsafe_allow_html=True)

st.caption("🧾 Upload your resume to get started with AI-powered analysis")
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])


# ---------------- ANALYSIS ----------------
if uploaded_file:
    results = run_regex_analysis(uploaded_file)
    resume_text = results["text"].lower()

    required_skills = [s.lower() for s in skills_array]

    matched_skills = [s for s in required_skills if s in resume_text]
    
    matched_skills=str(matched_skills)
    missing_skills = list(set(required_skills) - set(matched_skills))

    ats_score = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0

    # ---------------- DONUT ----------------
    def draw_donut(score):
        fig, ax = plt.subplots()
        sizes = [score, 100 - score]

        ax.pie(
            sizes,
            startangle=90,
            wedgeprops=dict(width=0.3)
        )

        ax.text(0, 0, f"{int(score)}", ha='center', va='center', fontsize=18)
        ax.axis('equal')

        return fig

    # ---------------- LAYOUT ----------------
    col1, col2 = st.columns([1.2, 1.8])

    # ========== LEFT ==========
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("ATS Score")

        fig = draw_donut(ats_score)
        st.pyplot(fig)

        if ats_score < 40:
            status = "Needs Improvement"
            color = "red"
        elif ats_score < 70:
            status = "Average"
            color = "orange"
        else:
            status = "Good"
            color = "green"

        st.markdown(f'<p style="color:{color}; font-weight:bold;">{status}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # -------- Skills Match --------
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ========== RIGHT ==========
        
    st.markdown(f"""
                <style>
                .skill-box {{
                    background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);           
                    padding: 20px;
                    width:520px;
                    border-radius: 12px;
                    color: white;
                    max-width: 1300px;
                    margin-top: 35px;
                    overflow:hidden;
                }}
                
                .skill-box h2 {{
                    font-size: 2.5rem;
                    font-weight: bold;
                    margin-bottom: 10px;
                }}

                .skill-box p {{
                    font-size: 1.2rem;
                    line-height: 1.5;
                }}
                
                .skill-box:hover {{
                    cursor: pointer;
                    transform: scale(1.02);
                    transition: 0.1s;
                    border:3px solid #6dd5ed 
                }}
                </style>

                <div class="skill-box">
                    <h3>keyword Match</h3>
                      {int(ats_score)}%
                    <h3>Skills Match</h3>
                    <p>
                            {matched_skills}
                    </p>
                    <h3>Missing Skills</h3>
                            {missing_skills}
                </div>
                """, unsafe_allow_html=True)
    with col2:

        # -------- Format Analysis --------
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Format Analysis")

        # (you can replace with real logic later)
        format_score = 65
        section_score = 26

        st.write(f"Format Score: {format_score}%")
        st.write(f"Section Score: {section_score}%")

        st.markdown('</div>', unsafe_allow_html=True)

        # -------- Suggestions --------
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Resume Improvement Suggestions")

        st.markdown("### 📞 Contact Information")
        st.write("• Add your LinkedIn profile URL")

        st.markdown("### 📝 Professional Summary")
        st.write("• Add a professional summary to highlight your key qualifications")

        st.markdown("### 💼 Skills Section")
        if missing_skills:
            st.write("• Add missing relevant skills")
        else:
            st.write("• Great job! No major skill gaps")

        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Upload your resume to see ATS analysis")