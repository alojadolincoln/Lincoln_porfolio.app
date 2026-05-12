import streamlit as st

st.markdown("# 👤 About Me")

st.markdown("""
## 🎯 Who Am I?

**Lincoln** - A curious student exploring the intersections of **Science, Technology, and Entertainment**.

### 🧠 My Interests:
- **Technology**: Coding, AI, Web Development
- **Astrology**: Zodiac insights, cosmic patterns
- **Medicine**: Human anatomy, healthcare innovation
- **Gaming**: Strategy games, competitive play
- **Anime**: Epic stories, character development

### ⚡ Personality:
- **Observant**: Notice details others miss
- **Adaptive**: Quick learner, flexible thinker
- **Collaborative**: Love working with teams

### 🎮 Current Status:
**Level: Student Explorer** | **Next Quest: Master Developer**
""")

st.subheader("✨ Your Zodiac Compatibility")
zodiac = st.selectbox("Select your zodiac sign:", 
                     ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
                      "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

compatibility = {
    "Aries": "🔥 Great energy match! Let's game together!",
    "Taurus": "🪨 Stable vibes - perfect for team projects!",
    "Gemini": "💨 Dynamic duo for tech adventures!",
    "Cancer": "🦀 Caring connection - medical discussions?",
    "Leo": "🦁 Epic collaboration potential!",
    "Virgo": "🔬 Perfect for science experiments!",
    "Libra": "⚖️ Balanced teamwork superstar!",
    "Scorpio": "🦂 Intense focus - coding marathons!",
    "Sagittarius": "🏹 Adventure buddies!",
    "Capricorn": "🗻 Ambitious goals align perfectly!",
    "Aquarius": "🌌 Cosmic tech innovators!",
    "Pisces": "🐟 Creative anime brainstorming!"
}

st.success(f"**{zodiac}**: {compatibility[zodiac]}")