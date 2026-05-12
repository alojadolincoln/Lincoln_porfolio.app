import streamlit as st

st.set_page_config(
    page_title="Lincoln's Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🚀 Welcome to Lincoln\'s Portfolio</h1>', unsafe_allow_html=True)

st.markdown("""
**Navigate through my digital universe using the sidebar!** 🌌

**Explore my world of:**
- **Technology & Science** 💻
- **Astrology & Cosmos** ✨
- **Medical Knowledge** 🩺
- **Gaming Adventures** 🎮
- **Anime Universe** ⚔️

---
""")

name = st.text_input("👋 What's your name?", "Visitor")
if st.button("✨ Connect with Lincoln"):
    st.balloons()
    st.success(f"🌟 Hello {name}! Thanks for visiting my portfolio!")

st.info("🧠 Student | Tech Enthusiast | Science Lover | Gamer | Anime Fan")