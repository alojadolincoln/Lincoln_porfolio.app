import streamlit as st

st.markdown("# 🚀 Projects & Creations")

st.subheader("📱 Featured Projects")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
    ### 🩺 **Medical Symptom Checker**
    Interactive web app to analyze symptoms and suggest possible conditions.
    - Streamlit + Python
    - Medical database integration
    - User-friendly interface
    """)
with col2:
    st.success("🔥 Live Demo")
    if st.button("🚀 Launch Demo"):
        st.balloons()

st.markdown("---")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
    ### ✨ **Astrology Insights Dashboard**
    Daily horoscopes, compatibility checker, and birth chart generator.
    - Data visualization
    - API integration
    - Responsive design
    """)
with col2:
    st.success("⭐ Featured")
    if st.button("🌟 View Project"):
        st.info("Coming Soon!")

st.markdown("---")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
    ### 🎮 **Game Stats Tracker**
    Track your gaming progress, leaderboards, and achievements.
    - Real-time data
    - Multi-game support
    - Competitive analytics
    """)
with col2:
    st.success("🎮 Active")

st.subheader("🎯 Explore More")
project_type = st.selectbox("Filter by category:", 
                          ["All", "Medical", "Technology", "Gaming", "Anime"])
st.write("**Selected projects will appear here based on your interests!**")