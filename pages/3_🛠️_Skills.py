import streamlit as st
import numpy as np
import time

st.markdown("# 🛠️ Skills & Expertise")

st.subheader("🩺 Medical Field")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    - **Anatomy & Physiology**
    - **First Aid & CPR**
    - **Medical Terminology**
    - **Patient Care Basics**
    """)
with col2:
    medical_progress = st.progress(0)
    for i in range(101):
        medical_progress.progress(i)
        time.sleep(0.01)
    st.success("Medical Knowledge: 85%")

st.subheader("💻 Technology")
tech_skills = {
    "Python": 80,
    "Streamlit": 75,
    "HTML/CSS": 70,
    "Data Analysis": 65
}

for skill, level in tech_skills.items():
    st.metric(label=skill, value=f"{level}%")

st.subheader("🎯 Test My Skills!")
selected_skill = st.selectbox("Choose a skill to see demo:", 
                            ["Medical Quiz", "Tech Challenge", "Creativity Test"])

if selected_skill == "Medical Quiz":
    st.info("**Question**: What does CPR stand for?")
    answer = st.radio("Select answer:", ["Cardiopulmonary Resuscitation", "Central Pulse Recovery", "Cardiac Pressure Response"])
    if answer == "Cardiopulmonary Resuscitation":
        st.success("✅ Correct!")
    else:
        st.error("❌ Try again!")

st.markdown("---")
st.info("🔥 **Creativity**: Generating unique solutions daily!")