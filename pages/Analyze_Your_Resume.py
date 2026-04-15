import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
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
                <p>
                    Get instant AI-powered feedback to optimize your resume
                </p>
            </div>
            """, unsafe_allow_html=True)

data = pd.read_csv("data/skills_database.csv")

# Step 1: Get unique categories
categories = data["category"].unique()

# Step 2: Select category
job_cat = st.selectbox("Job Category", categories)

# Step 3: Filter roles based on selected category
filtered_roles = data[data["category"] == job_cat]["role"].unique()

# Step 4: Select role
selected_role = st.selectbox("Specific Role", filtered_roles)

# select description
selected_des = data.loc[data["role"] == selected_role, "description"].values[0]

# select skills
skills_array = data.loc[data["role"] == selected_role, "skill"].unique()

skills_html = ", ".join([f"<span class='tag'>{s}</span>" for s in skills_array])

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
            <h2>{selected_role if selected_role else "Select a role"}</h2>
            <p>{selected_des if selected_des else "No description available."}</p>
            <h2>Required Skills:</h2>
            <p>{skills_html if skills_html else "Skills will appear here."}</p>
        </div>
        """, unsafe_allow_html=True)

# 1. Inject the CSS (without the <div> tag)
# This CSS 'finds' the container and colors it
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

# Now, simply calling the uploader puts it inside that styled area
st.caption("🧾Upload your resume to get started with AI-powered analysis")
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
from parser_utils import run_regex_analysis
if uploaded_file:
    results = run_regex_analysis(uploaded_file)
    with st.expander("Debug: Search for 'linkedin' in raw text"):
        if "linkedin" in results['text'].lower():
            st.write("Found 'linkedin' in text, but Regex missed it.")
            # Show a snippet of where it found it
            start_index = results['text'].lower().find("linkedin")
            st.text(results['text'][start_index:start_index+50])
        else:
            st.write("The word 'linkedin' is NOT in the extracted text at all.")