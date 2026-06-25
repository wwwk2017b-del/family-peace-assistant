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
        "emoji": "😤",
        "breathing": "Breathe IN for 4 seconds. Hold 4 seconds. Breathe OUT for 6 seconds. Repeat 5 times.",
        "kind": "It is okay to feel angry. Every person feels angry sometimes. Your feelings are valid. You are not a bad person. This feeling will pass.",
        "tip": "Wait 10 minutes before speaking when angry. Try saying: I feel hurt - instead of blaming someone.",
        "activity": "Go for a 10 minute walk\nDrink cold water slowly\nListen to your favorite song\nWrite what you feel then tear the paper"
    },
    "sad": {
        "emoji": "😢",
        "breathing": "Breathe IN through nose. Hold 3 seconds. Breathe OUT through mouth. Repeat 6 times.",
        "kind": "Feeling sad means you have a heart that cares deeply. You are not alone. Better days are coming. Hold on.",
        "tip": "Say to someone: I just need you to listen to me. Talking always helps more than staying silent.",
        "activity": "Call a close friend\nWatch something funny for 15 minutes\nEat something you like\nSit in sunlight for 10 minutes"
    },
    "anxious": {
        "emoji": "😰",
        "breathing": "Put hand on stomach. Breathe IN so stomach rises. Hold 2 seconds. Breathe OUT slowly for 8 seconds. Repeat 7 times.",
        "kind": "Most things we worry about never happen the way we imagine. Take one step at a time. You can handle this.",
        "tip": "Say to family: I am feeling overwhelmed. Can we talk? Sharing your stress makes it feel lighter.",
        "activity": "Write your 3 biggest worries on paper\nDrink warm tea slowly\nClose eyes and breathe for 5 minutes"
    },
    "frustrated": {
        "emoji": "😠",
        "breathing": "Breathe IN fast for 2 seconds. Breathe OUT very slowly for 8 seconds. Imagine stress leaving. Repeat 5 times.",
        "kind": "You have been trying very hard. It is okay if things are not working right now. Rest and try again. You are not a failure.",
        "tip": "Say: I feel like we are not understanding each other. Can we start this conversation fresh?",
        "activity": "Do 20 jumping jacks\nSqueeze a pillow and release\nTake a 15 minute break from the situation"
    },
    "calm": {
        "emoji": "😊",
        "breathing": "Breathe IN for 4 seconds. Breathe OUT for 4 seconds. Do this every morning for a good day.",
        "kind": "You are doing great! Protect this calm feeling. Share your positive energy with your family today.",
        "tip": "This is the best time to talk to family. When you are calm others listen better. Say one kind word today.",
        "activity": "Tell a family member you appreciate them\nHave a meal together without phones\nAsk someone: How are you feeling today?"
    }
}

def detect(text):
    lower = text.lower()
    scores = {e: 0 for e in KEYWORDS}
    for emotion, words in KEYWORDS.items():
        for word in words:
            if word in lower:
                scores[emotion] += 1
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        best = "calm"
    return best

text = st.text_area("", height=120,
    placeholder="Example: I am very angry... I feel sad... I am stressed and worried...")

col1, col2, col3, col4, col5 = st.columns(5)
if col1.button("😤 Angry"):
    text = "I am very angry"
if col2.button("😢 Sad"):
    text = "I feel very sad and alone"
if col3.button("😰 Stressed"):
    text = "I am very stressed and worried"
if col4.button("😠 Frustrated"):
    text = "I am frustrated nothing works"
if col5.button("😊 Calm"):
    text = "I feel calm and okay today"

if st.button("Get My Advice", use_container_width=True, type="primary"):
    if text.strip():
        emotion = detect(text)
        adv = ADVICE[emotion]
        st.markdown("---")
        st.markdown(f"## {adv['emoji']} Emotion detected: {emotion.upper()}")
        st.markdown("### 💨 Breathing Exercise - Do this right now")
        st.info(adv["breathing"])
        st.markdown("### 💙 Kind Words For You")
        st.success(adv["kind"])
        st.markdown("### 🗣️ Communication Tip")
        st.warning(adv["tip"])
        st.markdown("### 🏃 Do This Now")
        for line in adv["activity"].split("\n"):
            st.write("• " + line)
        st.markdown("---")
        st.caption("Made with love 💙 - Family Peace Assistant")
    else:
        st.warning("Please type how you are feeling first!")
