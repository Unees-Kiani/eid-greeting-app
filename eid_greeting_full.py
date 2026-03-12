# eid_greeting_full.py
import streamlit as st
import time

# Page setup
st.set_page_config(
    page_title="Eid Mubarak 🌙✨",
    page_icon="🌙",
    layout="wide"
)

# ======= HEADER =======
st.markdown("""
<div style="text-align:center;">
    <h1 style="color: darkgreen; font-size:60px;">🌙✨ EID MUBARAK! ✨🌙</h1>
    <h2 style="color: darkblue;">From UNEES UR REHMAN KIANI 💖</h2>
</div>
""", unsafe_allow_html=True)

# ======= ANIMATED GREETING =======
message = "May your Eid be filled with joy, blessings, peace, and endless happiness! 🎉🌙"
animated_text = st.empty()

for i in range(len(message)+1):
    animated_text.markdown(f"<h3 style='text-align:center; color:darkorange;'>{message[:i]}</h3>", unsafe_allow_html=True)
    time.sleep(0.03)

# ======= MOVING MOON =======
st.markdown("""
<div style="text-align:center; font-size:80px; color:gold; animation: moveMoon 3s infinite alternate;">
    🌙
</div>

<style>
@keyframes moveMoon {
    0% { transform: translateY(0px);}
    100% { transform: translateY(-20px);}
}
</style>
""", unsafe_allow_html=True)

# ======= DECORATIVE STARS =======
st.markdown("""
<div style='text-align:center; font-size:40px; color:gold;'>
    🌟 ✨ 🌙 ✨ 🌟
</div>
""", unsafe_allow_html=True)

# ======= SCROLLING EID WISHES =======
st.markdown("""
<marquee behavior="scroll" direction="left" style="color:violet; font-size:28px;">
    Eid Mubarak! May Allah bless you with happiness, health, and endless joy! 🎉💖🌙✨
</marquee>
""", unsafe_allow_html=True)

# ======= SURPRISE BUTTON WITH FIREWORKS =======
if st.button("Click for Eid Surprise 🎊"):
    st.balloons()
    st.success("🎆 Eid Mubarak! May this Eid bring peace and prosperity to you and your family! 🌙✨")
    st.markdown("""
    <div style="text-align:center; font-size:60px; color:gold; animation: fireworks 2s infinite;">
        🎇 🎆 🎇 🎆 🎇
    </div>
    <style>
    @keyframes fireworks {
        0% {transform: scale(1);}
        50% {transform: scale(1.5);}
        100% {transform: scale(1);}
    }
    </style>
    """, unsafe_allow_html=True)

# ======= OPTIONAL BACKGROUND MUSIC =======
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
""", unsafe_allow_html=True)

# ======= FOOTER =======
st.markdown("""
<p style='text-align:center; color:purple; font-size:20px; margin-top:20px;'>
Share this link with your friends & family and spread Eid happiness! 💖🌙✨
</p>
""", unsafe_allow_html=True)
