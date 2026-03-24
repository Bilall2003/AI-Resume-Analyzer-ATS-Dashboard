import streamlit as st

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

job_cat=st.selectbox("Job Category",range(1,10))

# uploaded_file = st.file_uploader(
#     "Upload Resume",
#     type=["pdf","docx"]
# )

# if uploaded_file:
#     st.success("Resume uploaded successfully!")
    