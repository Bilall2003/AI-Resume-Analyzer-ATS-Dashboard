import streamlit as st

st.set_page_config(layout="centered")
st.markdown("""
            <style>

            .green-box {
                background: linear-gradient(45deg, rgba(0, 180, 219, 0.7) 100%, rgba(0, 131, 176, 0.05) 100%);    
                padding:20px;     
                width:2500px; 
                border-radius: 12px;
                color: white;
                max-width: 800px;
                margin-top: 15px;
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
                line-height: 1.5;
            }
            </style>

            <div class="green-box">
                <h2>Smart Resume AI</h2>
                <p>
                    Transform your career with AI-powered resume analysis and building.<br>
                    Get personalized insights and create professional resumes that stand out.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
st.markdown("""
                <style>
                .sec-box {
                background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);          
                    padding: 20px;
                    width:2500px; 
                    border-radius: 12px;
                    color: white;
                    max-width: 800px;
                    margin-top: 70px;
                    position: relative;
                    overflow:hidden;
                }

                /* Animation */
                @keyframes Syncimg {
                    0%, 100% { transform: translateX(50px); z-index: 1; }
                    50% { transform: translateX(-50px); z-index: -1; }
                }

                .secmoveright {
                    width: 40px;
                    position: relative;
                    animation: Syncimg 2s infinite ease-in-out;
                }

                .sec-box h2 {
                    font-size: 2.5rem;
                    font-weight: bold;
                    margin-bottom: 10px;
                }

                .sec-box p {
                    font-size: 1.2rem;
                    line-height: 1.5;
                }

                .sec-box:hover {
                    cursor: pointer;
                    transform: scale(1.02);
                    transition: 0.1s;
                    border:3px solid #6dd5ed
                }
                </style>

                <div class="sec-box">
                    <img class="secmoveright" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/refs/heads/main/script/assets/rb_image.png">
                    <h2>AI-Powered Analysis</h2>
                    <p>
                        Get instant feedback on your resume with advanced AI analysis that identifies strengths and areas for improvement.
                    </p>
                </div>
                """, unsafe_allow_html=True)

st.markdown("""
            <style>
            .thrd-box {
                background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);           
                padding: 20px;
                width:2500px;
                border-radius: 12px;
                color: white;
                max-width: 800px;
                margin-top: 35px;
                overflow:hidden;
            }
                /* Animation */
            @keyframes Syncimg {
                0%, 100% { transform: translateX(50px); z-index: 1; }
                50% { transform: translateX(-50px); z-index: -1; }
            }

            .thrdmoveright {
                width: 70px;
                position: relative;
                animation: Syncimg 2s infinite ease-in-out;
                overflow:hidden;
            }

            .thrd-box h2 {
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 10px;
            }

            .thrd-box p {
                font-size: 1.2rem;
                line-height: 1.5;
            }
            
            .thrd-box:hover {
                cursor: pointer;
                transform: scale(1.02);
                transition: 0.1s;
                border:3px solid #6dd5ed 
            }
            </style>

            <div class="thrd-box">
                <img class="thrdmoveright" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/refs/heads/main/script/assets/rb_image%20(1).png">
                <h2>Dashboard Exploration</h2>
                <p>
                        visual interfaces that aggregate key performance indicators and metrics from various data sources into a single, easy-to-digest format.
                </p>
            </div>
            """, unsafe_allow_html=True)
st.markdown("""
            <style>
            .forth-box {
                background: linear-gradient(45deg, rgba(120, 180, 200, 0.3) 100%, rgba(0, 131, 176, 0.05) 100%);          
                padding: 20px;
                width:2500px; 
                border-radius: 12px;
                color: white;
                max-width: 800px;
                margin-top: 35px;
                overflow: hidden
            }
            
                /* Animation */
            @keyframes Syncimg {
                0%, 100% { transform: translateX(50px); z-index: 1; }
                50% { transform: translateX(-50px); z-index: -1; }
            }

            .forthmoveright {
                width: 40px;
                position: relative;
                animation: Syncimg 2s infinite ease-in-out;
            }

            .forth-box h2 {
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 10px;
            }

            .forth-box p {
                font-size: 1.2rem;
                line-height: 1.5;
            }
            .forth-box:hover {
                cursor: pointer;
                transform: scale(1.02);
                transition: 0.1s;
                border:3px solid #6dd5ed  
            }
            
            
            </style>
            <div class="forth-box">
                <img class="forthmoveright" src="https://raw.githubusercontent.com/Bilall2003/Smart-Resume-Analyzer-Job-Recommendation-System/refs/heads/main/script/assets/img%203.avif">
                <h2>Career Insights</h2>
                <p>
                    Access detailed analytics and personalized recommendations to enhance your career prospects.
                </p>
            </div>
            
            """, unsafe_allow_html=True)
