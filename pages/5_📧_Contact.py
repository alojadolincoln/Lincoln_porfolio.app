import streamlit as st
import time

st.markdown("# 📧 Let's Connect!")

# Contact form
st.subheader("💬 Send me a message")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.selectbox("Subject", 
                          ["General Inquiry", "Collaboration", "Gaming", "Anime", "Medical", "Tech Project"])
    message = st.text_area("Message")
    
    col1, col2, col3 = st.columns([1,1,2])
    
    with col1:
        st.form_submit_button("✨ Send Message", type="primary")
    with col2:
        st.form_submit_button("🎮 Challenge Me to a Game!")
    with col3:
        st.form_submit_button("🌟 Recommend Anime")
    
    if st.form_submit_button("🚀 Connect on GitHub"):
        st.success("📂 GitHub connection requested!")

# Success message
if 'button_pressed' in st.session_state:
    st.success("✅ Message sent successfully! I'll respond within 24 hours.")
    st.balloons()

# Social links
st.subheader("🔗 Find Me Here")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("💻 GitHub"):
        st.info("https://github.com/alojadolincoln")
with col2:
    if st.button("📧 Email"):
        st.info("alojadolincolngodz@gmail.com")
with col3:
    if st.button("🙎 Facebook"):
        st.info("Lincoln Alojado")

st.markdown("---")
st.caption("🌟 Thanks for visiting! Let's create something amazing together!")