import streamlit as st

st.markdown("""
<style>
.firstbox{
    background: linear-gradient(45deg, rgba(120, 180, 200, 0.3), rgba(0, 131, 176, 0.1));
    width: 600px;
    height: 400px;
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

</style>

<div class="firstbox">
    <img class="profileimg" src="https://avatars.githubusercontent.com/u/189706034?v=4" height="150">
    <h2>Bilal Ahmed</h2>
    <p2>CS student in Data Science & AI  | ML & NLP projects | Python & SQL | Turning data into scalable, real-world solutions </p2>
</div>
""", unsafe_allow_html=True)