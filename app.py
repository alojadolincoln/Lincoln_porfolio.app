import streamlit as st

st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .css-1d391kg {padding-left: 1rem;}
    .css-1d391kg {padding-right: 1rem;}
    @media (max-width: 768px) {
        .main .block-container {padding-top: 1rem; padding-left: 0.5rem; padding-right: 0.5rem;}
    }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🌟 Home - Welcome to My Universe!")

if st.button("📱 Mobile View Optimized", use_container_width=True):
    st.success("✅ Perfect for all devices!")

# Responsive columns (1 column on mobile, 2 on desktop)
col1, col2 = st.columns([3, 1]) if st.get_option("theme.base") != "dark" else st.columns([2, 1])

with col1:
    st.markdown("""
    ## 👋 Hi, I'm **Lincoln**!
    
    **Student • Tech Enthusiast • Science Explorer**
    
    Passionate about **Technology**, **Astrology**, **Medicine**, and **Science**.
    I love **gaming** and **anime** in my free time!
    
    **Observant • Adaptive • Team Player**
    """)

with col2:
    st.image("profile.jpg", width=250, caption="Lincoln ✨")

st.subheader("📊 My Journey")
if st.columns(1)[0]:  # Force single column on mobile
    col1, col2, col3, col4 = st.columns([1,1,1,1])
else:
    col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Projects", "5+")
with col2:
    st.metric("Skills", "Medical + Tech")
with col3:
    st.metric("Games Played", "100+")
with col4:
    st.metric("Anime Watched", "50+")
