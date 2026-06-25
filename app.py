import streamlit as st
import pickle

st.set_page_config(page_title="Family Peace Assistant", page_icon="🕊️")
st.title("🕊️ Family Peace Assistant")
st.markdown("### Type how you are feeling. Get calm advice instantly.")

ADVICE = {
    "angry": {
        "breathing": "Breathe IN for 4 seconds → Hold 4 seconds → Breathe OUT for 6 seconds → Repeat 5 times",
        "kind": "It is okay to feel angry. Every person feels this way sometimes. You are not a bad person. This feeling will pass.",
        "tip": "Wait 10 minutes before speaking when angry. Try saying: I feel hurt — instead of blaming someone.",
        "activity": "Go for a 10 minute walk • Drink cold water slowly • Listen to your favorite song"
    },
    "sad": {
        "breathing": "Breathe IN through nose → Hold 3 seconds → Breathe OUT through mouth → Repeat 6 times",
        "kind": "Feeling sad means you have a heart that cares. You are not alone. Better days are coming. Hold on.",
        "tip": "Say to someone: I just need you to listen to me. Talking always helps more than staying silent.",
        "activity": "Call a close friend • Watch something funny • Sit in sunlight for 10 minutes"
    },
    "anxious": {
        "breathing": "Hand on stomach → Breathe IN so stomach rises → Hold 2 seconds → Breathe OUT for 8 seconds → Repeat 7 times",
        "kind": "Most things we worry about never happen the way we imagine. Take one step at a time. You can handle this.",
        "tip": "Say to family: I am feeling overwhelmed. Can we talk? Sharing your stress makes it feel lighter.",
        "activity": "Write your 3 biggest worries • Drink warm tea slowly • Close eyes and just breathe for 5 minutes"
    },
    "frustrated": {
        "breathing": "Breathe IN fast 2 seconds → Breathe OUT very slowly 8 seconds → Imagine stress leaving → Repeat 5 times",
        "kind": "You have been trying very hard. It is okay if things are not working right now. Rest and try again.",
        "tip": "Say: I feel like we are not understanding each other. Can we start this conversation fresh?",
        "activity": "Do 20 jumping jacks • Squeeze a pillow and release • Take a 15 minute break"
    },
    "calm": {
        "breathing": "Breathe IN 4 seconds → Breathe OUT 4 seconds → Do this every morning for a good day",
        "kind": "You are doing great! Protect this calm feeling. Share your positive energy with your family today.",
        "tip": "This is the best time to talk. When you are calm, others listen better. Say one kind word today.",
        "activity": "Tell a family member you appreciate them • Have a meal together without phones"
    },
}

text = st.text_area("", height=120,
    placeholder="Example: I am very angry... I feel sad... I am stressed...")

col1, col2, col3, col4, col5 = st.columns(5)
if col1.button("😤 Angry"): text = "I am very angry"
if col2.button("😢 Sad"): text = "I feel very sad"
if col3.button("😰 Stressed"): text = "I am very stressed"
if col4.button("😠 Frustrated"): text = "I am frustrated"
if col5.button("😊 Calm"): text = "I feel calm today"

if st.button("Get My Advice", use_container_width=True, type="primary"):
    if text.strip():
        with open("data/model.pkl","rb") as f:
            model = pickle.load(f)
        with open("data/vectorizer.pkl","rb") as f:
            vec = pickle.load(f)
        emotion = model.predict(vec.transform([text]))[0]
        adv = ADVICE[emotion]

        st.markdown("---")
        st.success(f"Emotion detected: **{emotion.upper()}**")

        st.markdown("### 💨 Breathing Exercise")
        st.info(adv["breathing"])

        st.markdown("### 💙 Kind Words For You")
        st.write(adv["kind"])

        st.markdown("### 🗣️ Communication Tip")
        st.warning(adv["tip"])

        st.markdown("### 🏃 Do This Now")
        st.write(adv["activity"])
    else:
        st.warning("Please type how you are feeling first!")
