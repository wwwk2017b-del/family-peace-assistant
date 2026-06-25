"""
predict.py
Takes user input text, detects emotion, and gives kind helpful advice.
Simple enough for anyone to understand and use.
"""
import pickle

# Load trained model
with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)
with open("data/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Advice for each emotion — simple words, easy to understand
ADVICE = {
    "angry": {
        "emoji": "😤",
        "feeling": "You are feeling ANGRY right now.",
        "breathing": (
            "💨 BREATHING EXERCISE (do this right now):\n"
            "   → Breathe IN slowly for 4 seconds\n"
            "   → Hold your breath for 4 seconds\n"
            "   → Breathe OUT slowly for 6 seconds\n"
            "   → Repeat this 5 times. You will feel better."
        ),
        "kind_words": (
            "💙 KIND WORDS FOR YOU:\n"
            "   It is okay to feel angry. Every person feels angry sometimes.\n"
            "   Your feelings are valid. You are not a bad person.\n"
            "   This feeling will pass. You are stronger than your anger."
        ),
        "tip": (
            "🗣️ COMMUNICATION TIP:\n"
            "   Before speaking when angry — wait 10 minutes.\n"
            "   Anger makes us say things we later regret.\n"
            "   Try saying: 'I feel hurt when this happens'\n"
            "   instead of: 'You always do this to me!'"
        ),
        "activity": (
            "🏃 DIVERT YOUR ENERGY:\n"
            "   → Go for a 10 minute walk outside\n"
            "   → Drink a full glass of cold water slowly\n"
            "   → Write what you feel on paper, then tear it\n"
            "   → Listen to your favorite song"
        ),
    },

    "sad": {
        "emoji": "😢",
        "feeling": "You are feeling SAD right now.",
        "breathing": (
            "💨 BREATHING EXERCISE (do this right now):\n"
            "   → Take a deep breath IN through your nose\n"
            "   → Hold for 3 seconds\n"
            "   → Slowly breathe OUT through your mouth\n"
            "   → Repeat 6 times. Feel your body relax."
        ),
        "kind_words": (
            "💙 KIND WORDS FOR YOU:\n"
            "   Feeling sad does not mean you are weak.\n"
            "   It means you have a heart that cares deeply.\n"
            "   You are not alone. Many people feel this way.\n"
            "   Better days are coming. Hold on."
        ),
        "tip": (
            "🗣️ COMMUNICATION TIP:\n"
            "   Share your feelings with someone you trust.\n"
            "   You can say: 'I need someone to just listen to me'\n"
            "   Sometimes we just need to be heard, not advised.\n"
            "   Talking helps more than staying silent."
        ),
        "activity": (
            "🌟 FEEL BETTER ACTIVITY:\n"
            "   → Call or message a close friend\n"
            "   → Watch a funny video for 15 minutes\n"
            "   → Eat something you like\n"
            "   → Sit in sunlight for 10 minutes"
        ),
    },

    "anxious": {
        "emoji": "😰",
        "feeling": "You are feeling ANXIOUS / STRESSED right now.",
        "breathing": (
            "💨 BREATHING EXERCISE (do this right now):\n"
            "   → Put one hand on your stomach\n"
            "   → Breathe IN deeply so your stomach rises\n"
            "   → Hold for 2 seconds\n"
            "   → Breathe OUT slowly — 8 seconds\n"
            "   → Do this 7 times. Your body will calm down."
        ),
        "kind_words": (
            "💙 KIND WORDS FOR YOU:\n"
            "   Worrying about things shows you care.\n"
            "   But remember — most things we worry about\n"
            "   never actually happen the way we imagine.\n"
            "   Take one step at a time. You can handle this."
        ),
        "tip": (
            "🗣️ COMMUNICATION TIP:\n"
            "   When feeling anxious, talk to your family.\n"
            "   Say: 'I am feeling overwhelmed. Can we talk?'\n"
            "   Sharing your stress makes it feel lighter.\n"
            "   You do not have to carry everything alone."
        ),
        "activity": (
            "🧘 CALM YOUR MIND:\n"
            "   → Write down your 3 biggest worries on paper\n"
            "   → Next to each, write ONE small step you can take\n"
            "   → Drink warm water or tea slowly\n"
            "   → Close your eyes for 5 minutes — just breathe"
        ),
    },

    "frustrated": {
        "emoji": "😠",
        "feeling": "You are feeling FRUSTRATED right now.",
        "breathing": (
            "💨 BREATHING EXERCISE (do this right now):\n"
            "   → Breathe in fast for 2 seconds\n"
            "   → Breathe out VERY slowly for 8 seconds\n"
            "   → Imagine your frustration leaving with each breath out\n"
            "   → Repeat 5 times."
        ),
        "kind_words": (
            "💙 KIND WORDS FOR YOU:\n"
            "   You have been trying very hard.\n"
            "   It is okay if things are not working right now.\n"
            "   Frustration means you care about doing well.\n"
            "   Rest, and try again. You are not a failure."
        ),
        "tip": (
            "🗣️ COMMUNICATION TIP:\n"
            "   Instead of repeating the same argument,\n"
            "   try changing the approach.\n"
            "   Say: 'I feel like we are not understanding each other.\n"
            "   Can we start this conversation fresh?'"
        ),
        "activity": (
            "💪 RELEASE YOUR FRUSTRATION:\n"
            "   → Do 20 jumping jacks right now\n"
            "   → Squeeze a pillow tightly then release\n"
            "   → Take a 15 minute break from the situation\n"
            "   → Write what is frustrating you — seeing it on paper helps"
        ),
    },

    "calm": {
        "emoji": "😊",
        "feeling": "You are feeling CALM and okay right now.",
        "breathing": (
            "💨 BREATHING EXERCISE (maintain this calm):\n"
            "   → Breathe in for 4 seconds\n"
            "   → Breathe out for 4 seconds\n"
            "   → This keeps you calm and balanced\n"
            "   → Do this every morning for a good day."
        ),
        "kind_words": (
            "💙 KIND WORDS FOR YOU:\n"
            "   You are doing great!\n"
            "   This calm feeling — protect it.\n"
            "   Share your positive energy with your family today.\n"
            "   A calm person makes every room feel better."
        ),
        "tip": (
            "🗣️ COMMUNICATION TIP:\n"
            "   This is the best time to talk to your family.\n"
            "   When you are calm, others listen better.\n"
            "   Share something positive with a family member today.\n"
            "   Even one kind word can change someone's whole day."
        ),
        "activity": (
            "🌸 SPREAD THE PEACE:\n"
            "   → Tell one family member something you appreciate about them\n"
            "   → Have a meal together without phones\n"
            "   → Ask someone at home 'How are you feeling today?'\n"
            "   → Plan something fun to do together this week"
        ),
    },
}


def predict_and_advise(user_text):
    """Takes text input and returns emotion + full advice."""
    vec   = vectorizer.transform([user_text])
    emotion = model.predict(vec)[0]
    proba   = model.predict_proba(vec)[0]
    confidence = max(proba) * 100

    advice = ADVICE[emotion]

    print("\n" + "="*55)
    print(f" {advice['emoji']}  EMOTION DETECTED: {emotion.upper()}")
    print(f"    Confidence: {confidence:.1f}%")
    print("="*55)
    print(f"\n {advice['feeling']}\n")
    print(advice["breathing"])
    print()
    print(advice["kind_words"])
    print()
    print(advice["tip"])
    print()
    print(advice["activity"])
    print("\n" + "="*55)

    return emotion


def run_interactive():
    """Simple interactive mode — anyone can use this."""
    print("\n" + "="*55)
    print("   🕊️  FAMILY PEACE ASSISTANT")
    print("   CodTech ML Internship — Abhishek Prasad")
    print("="*55)
    print("\n  Type how you are feeling right now.")
    print("  I will understand and help you.\n")
    print("  (Type 'quit' to exit)\n")

    while True:
        user_input = input("  👤 How are you feeling? : ").strip()
        if user_input.lower() in ["quit", "exit", "bye", "q"]:
            print("\n  💙 Take care. Peace begins with you. Goodbye!\n")
            break
        if not user_input:
            print("  Please type something.\n")
            continue
        predict_and_advise(user_input)
        print()


if __name__ == "__main__":
    run_interactive()
