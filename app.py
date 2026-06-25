import streamlit as st

st.set_page_config(page_title="Family Peace Assistant", page_icon="🕊️")
st.title("🕊️ Family Peace Assistant")
st.markdown("### Type how you are feeling. Get calm advice instantly.")

KEYWORDS = {
    "angry": ["angry","anger","furious","rage","shout","scold","yell","hate","mad","boiling","blame","harsh","temper","fight"],
    "sad": ["sad","cry","crying","alone","lonely","hopeless","broken","low","empty","miss","hurt","nobody cares","tears"],
    "anxious": ["stress","stressed","anxious","worry","worrying","nervous","scared","panic","pressure","tense","cannot sleep","overthink"],
    "frustrated": ["frustrated","fed up","stuck","irritated","annoyed","nothing works","tired of","exhausted","misunderstood","not enough"],
    "calm": ["calm","okay","fine","good","happy","peace","better","positive","grateful","relaxed","hopeful","loved","great"]
}

ADVICE = {
    "angry": {
        "emoji": "😤", "color": "red",
        "breathing": "Breathe IN for 4 seconds → Hold 4 seconds → Breathe OUT for 6 seconds → Repeat 5 times",
        "kind": "It is okay to feel angry. Every person feels angry sometimes. Your feelings are valid. You are not a bad person. This feeling will pass.",
        "tip": "Wait 10 minutes before speaking when angry. Try saying: 'I feel hurt' instead of blaming someone.",
        "activity": "• Go for a 10 minute walk\n• Drink cold water slowly\n• Listen to your favorite song\n• Write what you feel then tear the paper"
    },
    "sad": {
        "emoji": "😢", "color": "blue",
        "breathing": "Breathe IN through nose → Hold 3 seconds → Breathe OUT through mouth → Repeat 6 times",
        "kind": "Feeling sad means you have a heart that cares deeply. You are not alone. Better days are coming. Hold on.",
        "tip": "Say to someone: 'I just need you to listen to me.' Talking always helps more than staying silent.",
        "activity": "• Call a close friend\n• Watch something funny for 15 minutes\n• Eat something you like\n• Sit in sunlight for 10 minutes"
    },
    "anxious": {
        "emoji": "😰", "color": "orange",
        "breathing": "Hand on stomach → Breathe IN so stomach rises → Hold 2
