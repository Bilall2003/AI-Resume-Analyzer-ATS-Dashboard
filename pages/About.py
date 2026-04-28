import streamlit as st

st.markdown("""
<style>
.firstbox{
    background: linear-gradient(45deg, rgba(120, 180, 200, 0.3), rgba(0, 131, 176, 0.1));
    width: 600px;
    height: 900px;
    border-radius: 20px;
    padding: 20px;
    color: black;
    margin: 100px auto; /* center horizontally */
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    gap: 15px; /* spacing between elements */
    color: white;
}

.profileimg{
    border-radius:50%;
    border:3px solid black;
}

.github-icon{
    width:40px;
    cursor:pointer;
    transition: transform 0.2s;
}

.github-icon:hover{
    transform: scale(1.1);
}

</style>

<div class="firstbox">
    <img class="profileimg" src="https://avatars.githubusercontent.com/u/189706034?v=4" height="150">
    <h2>Bilal Ahmed</h2>
    <p2> Motivated computer science student specializing in data science and applied AI, hands-on experience with
machine learning, NLP, and end-to-end data projects. Skilled in transforming complex datasets into actionable
insights using Python, SQL, and modern analytical frameworks. Committed to building efficient, scalable, and
reliable data-driven solutions, and eager to contribute to high-impact analytical and AI-driven teams.</p2>
</div>
""", unsafe_allow_html=True)