import streamlit as st
import textwrap

st.markdown(textwrap.dedent("""
<style>
.firstbox{
    background: linear-gradient(45deg, rgba(120, 180, 200, 0.3), rgba(0, 131, 176, 0.1));
    width: 600px;
    border-radius: 20px;
    padding: 25px;
    margin: 100px auto;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    gap: 10px;
    color: white;
    text-align: center;
}
.profileimg{
    border-radius:50%;
    border:3px solid black;

}
.socials{
    display:flex;
    gap:50px;
    margin-top:15px;

}
.socials img{
    width:100px;
    transition:0.1s;
}
.socials img:hover{
    transform:scale(1.15);
}
</style>

<div class="firstbox">
    <img class="profileimg" src="https://avatars.githubusercontent.com/u/189706034?v=4" height="150">
    <h2>Bilal Ahmed</h2>
    <p>
    Motivated Computer Science student specializing in Data Science and Applied AI,
    with hands-on experience in Machine Learning, NLP, and end-to-end data projects.
    Skilled in transforming complex datasets into actionable insights using Python,
    SQL, and modern analytical frameworks. Passionate about building scalable,
    reliable, and data-driven solutions.
    </p>
    <div class="socials">
        <a href="https://github.com/Bilall2003" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/github.png">
        </a>
        <a href="https://www.linkedin.com/in/bilal-ahmed-56b105248/" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/linkedin.png">
        </a>
        <a href="mailto:ahmedbilal988766@gmail.com">
            <img src="https://img.icons8.com/ios-filled/50/gmail.png">
        </a>
    </div>
</div>
"""), unsafe_allow_html=True)