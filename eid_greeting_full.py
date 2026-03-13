import streamlit as st
import time

# ===== PAGE SETUP =====
st.set_page_config(
    page_title="Eid Mubarak 🌙",
    page_icon="🌙",
    layout="centered"
)

# ===== BACKGROUND + ANIMATIONS =====
st.markdown("""
<style>
.stApp {
background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
url("https://images.unsplash.com/photo-1584551246679-0daf3d275d0f");
background-size: cover;
background-position: center;
background-attachment: fixed;
}

/* Moving Moon */
.moon {
position: absolute;
top: 80px;
left: -100px;
font-size: 60px;
animation: moonmove 15s linear infinite;
}

@keyframes moonmove {
0% {left:-100px;}
100% {left:100%;}
}

/* Twinkling stars */
.star {
color: gold;
font-size: 22px;
animation: twinkle 2s infinite alternate;
}

@keyframes twinkle {
from {opacity:0.3;}
to {opacity:1;}
}

/* Eid card style */
.card {
background: rgba(0,0,0,0.6);
padding: 25px;
border-radius: 15px;
text-align: center;
color: white;
font-size: 22px;
margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===== MOVING MOON =====
st.markdown('<div class="moon">🌙</div>', unsafe_allow_html=True)

# ===== TITLE =====
st.markdown("""
<div style="text-align:center;">
<h1 style="color:gold; font-size:60px;">🌙✨ EID MUBARAK ✨🌙</h1>
<h3 style="color:white;">From UNEES UR REHMAN KIANI</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

# ===== STAR DECORATION =====
st.markdown("""
<div style="text-align:center;">
<span class="star">⭐</span>
<span class="star">✨</span>
<span class="star">⭐</span>
<span class="star">✨</span>
<span class="star">⭐</span>
</div>
""", unsafe_allow_html=True)

# ===== COUNTDOWN =====
st.markdown(
"<h3 style='text-align:center; color:white;'>Your Eid Greeting is Loading...</h3>",
unsafe_allow_html=True
)

counter = st.empty()
for i in range(5,0,-1):
    counter.markdown(f"<h2 style='text-align:center; color:yellow;'>{i}</h2>", unsafe_allow_html=True)
    time.sleep(1)
counter.empty()

# ===== STEP-BY-STEP GREETING =====
messages = [
"🌙 Assalamu Alaikum!",
"✨ Eid Mubarak to you and your family.",
"🕌 May Allah accept your prayers.",
"💖 May your life be filled with happiness.",
"🌟 May your home be full of blessings.",
"🎉 Enjoy this beautiful day with your loved ones!"
]

for msg in messages:
    st.markdown(f"<h3 style='text-align:center; color:white;'>{msg}</h3>", unsafe_allow_html=True)
    time.sleep(1.5)

# ===== MOSQUE DECORATION =====
st.markdown("""
<div style="text-align:center; font-size:60px;">
🕌
</div>
""", unsafe_allow_html=True)

# ===== NASHEED PLAYER (VISIBLE TO USER) =====
st.markdown("<h4 style='text-align:center; color:white;'>🎵 Click Play to Listen to Eid Nasheed</h4>", unsafe_allow_html=True)
audio_url = "https://cdn.pixabay.com/download/audio/2022/03/15/audio_8c7c4e5d8c.mp3"
st.audio(audio_url)  # Always visible → user taps Play → works on mobile/desktop

# ===== EID GIFT BUTTON =====
st.write("")
st.markdown("<h3 style='text-align:center; color:gold;'>🎁 Open Your Eid Gift</h3>", unsafe_allow_html=True)

if st.button("Open Gift 🎁"):
    st.balloons()
    st.markdown("""
    <div class="card">
    🌙✨ <b>Eid Mubarak!</b> ✨🌙 <br><br>
    May Allah fill your life with happiness, peace and success. <br>
    May your home always be full of blessings and smiles. <br><br>
    💖 Best Wishes From <br>
    <b>UNEES UR REHMAN KIANI</b>
    </div>
    """, unsafe_allow_html=True)

# ===== ISLAMIC DECORATION =====
st.markdown("""
<div style='text-align:center; font-size:45px;'>
🌙 ⭐ 🕌 ⭐ 🌙
</div>
""", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
<hr>
<p style='text-align:center; color:white;'>
Share this greeting link with your friends & family ❤️
</p>
""", unsafe_allow_html=True)
