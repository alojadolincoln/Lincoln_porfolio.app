import streamlit as st

st.markdown("# 🌟 Home - Welcome to My Universe!")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ## 👋 Hi, I'm **Lincoln**!
    
    **Student • Tech Enthusiast • Science Explorer**
    
    Passionate about **Technology**, **Astrology**, **Medicine**, and **Science**.
    I love **gaming** and **anime** in my free time!
    
    **Observant • Adaptive • Team Player**
    """)
with col2:
    st.image("profile.jpg", width=300, caption="Lincoln - Tech Enthusiast ✨")

st.subheader("📊 My Journey")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Projects", "5+")
with col2:
    st.metric("Skills", "Medical + Tech")
with col3:
    st.metric("Games Played", "100+")
with col4:
    st.metric("Anime Watched", "50+")

st.info("💡 Scroll down to explore my skills, projects, and connect with me!")