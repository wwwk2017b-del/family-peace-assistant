import streamlit as st

st.set_page_config(page_title="Family Peace Assistant", page_icon="🕊️")
st.title("🕊️ Family Peace Assistant")
st.markdown("### Type anything you are feeling. I will understand and help you.")

# ── Smarter keyword scoring with weights ──────────────────────
KEYWORDS = {
    "angry": {
        "strong":  ["very angry","so angry","extremely angry","furious","rage","boiling","lost my temper","want to scream","hate everyone","scold","yell","shout","beaten","hit","violent","burst","explode"],
        "medium":  ["angry","anger","mad","irritated","frustrated with people","harsh","disrespect","blame","fight","argument","aggressive"],
        "weak":    ["annoyed","bothered","upset with","not happy with"]
    },
    "sad": {
        "strong":  ["very sad","so sad","deeply sad","heartbroken","crying","sobbing","feel like crying","depressed","hopeless","no reason to live","broken inside","empty inside","nobody cares","feel worthless","feel useless"],
        "medium":  ["sad","unhappy","miss","lonely","alone","low","hurt","pain","grief","sorrow","tears","gloomy","down"],
        "weak":    ["not okay","not well","not great","feeling off","little sad","bit sad"]
    },
    "anxious": {
        "strong":  ["very stressed","extremely stressed","panic attack","cannot breathe","heart racing","overthinking everything","cannot sleep at all","too much pressure","breaking down","falling apart"],
        "medium":  ["stressed","anxious","worry","worried","nervous","scared","fear","pressure","tense","tension","restless","overwhelmed","cannot focus","overthinking"],
        "weak":    ["little worried","slightly nervous","bit stressed","not sure about","uncertain"]
    },
    "frustrated": {
        "strong":  ["fed up","completely done","nothing ever works","same problem every day","no matter what I do","tired of trying","given up","cannot take it anymore","why does this always happen"],
        "medium":  ["frustrated","stuck","irritated","annoyed","nothing works","wasted effort","not working","no result","not appreciated","misunderstood","ignored"],
        "weak":    ["things not going well","not going as planned","little stuck","bit annoyed"]
    },
    "calm": {
        "strong":  ["very happy","extremely happy","feeling great","feeling wonderful","so peaceful","very relaxed","totally fine","perfectly okay","feeling blessed","feeling loved"],
        "medium":  ["calm","happy","okay","fine","good","peace","relaxed","positive","grateful","hopeful","better","loved","content","satisfied","balanced"],
        "weak":    ["alright","not bad","managing","getting by","surviving"]
    }
}

NEGATIONS = ["not","no","never","don't","dont","can't","cant","won't","wont","neither","nor"]

ADVICE = {
    "angry": {
        "emoji": "😤",
        "heading": "You are feeling ANGRY",
        "breathing": "Breathe IN slowly for 4 seconds. Hold for 4 seconds. Breathe OUT slowly for 6 seconds. Repeat this 5 times right now.",
        "kind": "It is completely okay to feel angry. Every human being feels angry sometimes. Your feelings are real and valid. You are not a bad person for feeling this way. This feeling will pass — it always does.",
        "tip": "Before you speak when angry — wait at least 10 minutes. Anger makes us say things we later regret deeply. When you are ready, try saying: 'I feel hurt when this happens' instead of 'You always do this to me!' This small change makes a huge difference.",
        "activity": "Go for a 10 minute walk outside\nDrink a full glass of cold water very slowly\nListen to your favorite calming song\nWrite exactly what you feel on paper — then tear it up\nDo 20 jumping jacks to release the energy"
    },
    "sad": {
        "emoji": "😢",
        "heading": "You are feeling SAD",
        "breathing": "Take a deep breath IN through your nose. Hold for 3 seconds. Slowly breathe OUT through your mouth. Feel your body relax. Repeat 6 times.",
        "kind": "Feeling sad does not mean you are weak. It means you have a heart that feels deeply and cares. You are not alone in this feeling — millions of people feel exactly this way. Please be gentle with yourself today. Better days are definitely coming. Hold on.",
        "tip": "Reach out to someone you trust today. You can simply say: 'I am not feeling okay. I just need someone to listen to me.' You do not need to explain everything. Just being heard makes a huge difference. Do not suffer in silence.",
        "activity": "Call or message one close friend right now\nWatch something funny or light for 15 minutes\nEat something you really like\nSit in sunlight for 10 minutes\nWrite 3 things you are grateful for today"
    },
    "anxious": {
        "emoji": "😰",
        "heading": "You are feeling STRESSED and ANXIOUS",
        "breathing": "Put one hand on your stomach. Breathe IN deeply so your stomach rises — not your chest. Hold for 2 seconds. Now breathe OUT very slowly for 8 full seconds. Do this 7 times. Your body will calm down automatically.",
        "kind": "You are carrying a lot right now and that takes real strength. Remember — most things we worry about never actually happen the way we imagine them. Your mind is trying to protect you but it is overdoing it. Take one small step at a time. You do not have to solve everything today.",
        "tip": "Tell someone in your family: 'I am feeling overwhelmed right now. Can we just talk for a few minutes?' Sharing your stress out loud makes it feel 50 percent lighter immediately. You do not have to carry everything alone.",
        "activity": "Write your 3 biggest worries on paper — then next to each write ONE small step you can take\nDrink warm water or tea very slowly\nClose your eyes for 5 minutes and just focus on breathing\nStep outside for fresh air for 10 minutes"
    },
    "frustrated": {
        "emoji": "😠",
        "heading": "You are feeling FRUSTRATED",
        "breathing": "Breathe IN quickly for 2 seconds. Now breathe OUT very very slowly for 8 seconds. Imagine all your frustration leaving your body with that breath. Repeat 5 times.",
        "kind": "You have been working so hard and trying so much. It is okay if things are not clicking right now — that is not a reflection of your worth or ability. Frustration means you genuinely care about doing well. Rest is not giving up. Rest is preparing to try again stronger.",
        "tip": "Instead of repeating the same argument that never goes anywhere, try changing your approach completely. Say: 'I feel like we keep having the same conversation and neither of us feels heard. Can we try talking about this differently?' This breaks the cycle.",
        "activity": "Do 20 jumping jacks right now to release tension\nSqueeze a pillow very tight then slowly release\nTake a complete 15 minute break — away from the situation\nWrite down exactly what is frustrating you — seeing it clearly on paper helps a lot"
    },
    "calm": {
        "emoji": "😊",
        "heading": "You are feeling CALM and OKAY",
        "breathing": "Breathe IN gently for 4 seconds. Breathe OUT slowly for 4 seconds. This simple rhythm keeps you centered and calm. Try doing this every morning for just 2 minutes.",
        "kind": "You are doing really well. This feeling of calm is precious — protect it and nurture it. The fact that you are checking in with your feelings shows real emotional maturity. Keep going. You are doing better than you think.",
        "tip": "This calm state is actually the perfect time to have any important conversations with your family. When you speak from a place of calm, people listen more openly and respond more kindly. Use this energy wisely today.",
        "activity": "Tell one family member something specific you appreciate about them today\nHave a meal together with no phones — just conversation\nAsk someone at home: How are you feeling today?\nPlan one small fun thing to do together this week"
    }
}

def detect_emotion(text):
    lower = text.lower()
    words = lower.split()

    scores = {"angry": 0, "sad": 0, "anxious": 0, "frustrated": 0, "calm": 0}

    for emotion, levels in KEYWORDS.items():
        for phrase in levels["strong"]:
            if phrase in lower:
                # check if negated
                phrase_words = phrase.split()
                idx = lower.find(phrase)
                before = lower[max(0, idx-20):idx]
                negated = any(neg in before.split() for neg in NEGATIONS)
                if not negated:
                    scores[emotion] += 3
                else:
                    # negation flips to opposite
                    if emotion == "calm":
                        scores["sad"] += 2
                    elif emotion in ["angry","frustrated"]:
                        scores["calm"] += 1

        for phrase in levels["medium"]:
            if phrase in lower:
                before = lower[max(0, lower.find(phrase)-20):lower.find(phrase)]
                negated = any(neg in before.split() for neg in NEGATIONS)
                if not negated:
                    scores[emotion] += 2
                else:
                    if emotion == "calm":
                        scores["sad"] += 1

        for phrase in levels["weak"]:
            if phrase in lower:
                scores[emotion] += 1

    # Handle mixed feelings — pick highest score
    max_score = max(scores.values())

    # If everything is zero — ask for more info
    if max_score == 0:
        return "unknown"

    # If there is a clear winner
    best = max(scores, key=scores.get)
    return best


# ── UI ────────────────────────────────────────────────────────

st.markdown("##### Just type naturally — like you are talking to a friend")

text = st.text_area("",
    height=130,
    placeholder="Type anything... Example:\n'I had a very bad day and I am so angry at my father'\n'I feel like nobody understands me'\n'Everything is fine today I am happy'")

st.markdown("##### Or quickly tap how you feel:")
col1, col2, col3, col4, col5 = st.columns(5)
if col1.button("😤\nAngry", use_container_width=True):
    text = "I am very angry and furious right now"
if col2.button("😢\nSad", use_container_width=True):
    text = "I feel very sad and lonely and nobody cares"
if col3.button("😰\nStressed", use_container_width=True):
    text = "I am very stressed and anxious and worried about everything"
if col4.button("😠\nFrustrated", use_container_width=True):
    text = "I am so frustrated nothing is working no matter what I do"
if col5.button("😊\nCalm", use_container_width=True):
    text = "I feel calm and okay and happy today"

st.markdown("")

if st.button("Understand my feeling and help me", use_container_width=True, type="primary"):
    if text.strip():
        emotion = detect_emotion(text)

        if emotion == "unknown":
            st.info("I could not fully understand your feeling from what you wrote. Could you tell me a little more? For example — are you feeling angry, sad, stressed, frustrated, or okay?")
        else:
            adv = ADVICE[emotion]
            st.markdown("---")
            st.markdown(f"## {adv['emoji']} {adv['heading']}")
            st.markdown("---")

            st.markdown("### 💨 Breathing Exercise — Do this right now")
            st.info(adv["breathing"])

            st.markdown("### 💙 Kind Words For You")
            st.success(adv["kind"])

            st.markdown("### 🗣️ How To Communicate Better")
            st.warning(adv["tip"])

            st.markdown("### 🏃 Things To Do Right Now")
            for line in adv["activity"].split("\n"):
                if line.strip():
                    st.write("• " + line.strip())

            st.markdown("---")
            st.markdown("*Remember — it is okay to not be okay. Every feeling is temporary. You are stronger than you think.* 💙")
    else:
        st.warning("Please type how you are feeling or tap one of the buttons above.")
