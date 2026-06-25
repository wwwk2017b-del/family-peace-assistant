"""
generate_data.py
Creates a dataset of emotion-labeled sentences for training the ML model.
"""
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

data = [
    # ANGRY
    ("I am very angry right now", "angry"),
    ("I feel like shouting at everyone", "angry"),
    ("Nobody listens to me at home", "angry"),
    ("I hate when people scold me for no reason", "angry"),
    ("I am so frustrated with my family", "angry"),
    ("Why does everyone blame me always", "angry"),
    ("I cannot control my anger", "angry"),
    ("I am boiling with rage inside", "angry"),
    ("My father shouts at me every night", "angry"),
    ("I feel like breaking things when I get angry", "angry"),
    ("People at home never understand me", "angry"),
    ("I am tired of being yelled at", "angry"),
    ("No one respects me in this house", "angry"),
    ("I want to scream and run away", "angry"),
    ("I am furious and I dont know what to do", "angry"),
    ("Everyone is so harsh with me", "angry"),
    ("I lost my temper again today", "angry"),
    ("My blood is boiling", "angry"),
    ("I feel disrespected by my family", "angry"),
    ("I am so done with all this fighting", "angry"),

    # SAD
    ("I feel very sad today", "sad"),
    ("I am crying inside but showing nothing", "sad"),
    ("Nobody cares about how I feel", "sad"),
    ("I feel alone even at home", "sad"),
    ("I miss the happy times with my family", "sad"),
    ("I feel like I am not valued", "sad"),
    ("Everything feels hopeless today", "sad"),
    ("I feel broken from inside", "sad"),
    ("I have no motivation to do anything", "sad"),
    ("I feel like crying all the time", "sad"),
    ("My heart feels heavy", "sad"),
    ("I feel low and empty", "sad"),
    ("Nothing makes me happy anymore", "sad"),
    ("I feel like I am failing at everything", "sad"),
    ("I just want someone to understand me", "sad"),
    ("I feel so lonely even in a crowd", "sad"),
    ("Today was a really bad day", "sad"),
    ("I feel like giving up", "sad"),
    ("I am deeply hurt by what happened", "sad"),
    ("Nobody asked me if I was okay", "sad"),

    # ANXIOUS
    ("I am very stressed about everything", "anxious"),
    ("I keep worrying about my future", "anxious"),
    ("I cannot sleep because of tension", "anxious"),
    ("My mind is always running with worries", "anxious"),
    ("I feel nervous all the time", "anxious"),
    ("I have too much pressure on me", "anxious"),
    ("I am scared of what will happen next", "anxious"),
    ("I feel restless and cannot sit still", "anxious"),
    ("Everything is uncertain and I am scared", "anxious"),
    ("I have so many responsibilities and I feel crushed", "anxious"),
    ("My heart beats fast when I think about problems", "anxious"),
    ("I am always overthinking everything", "anxious"),
    ("I cannot focus because of stress", "anxious"),
    ("I feel like something bad is going to happen", "anxious"),
    ("I am panicking inside", "anxious"),
    ("Too many things to handle at once", "anxious"),
    ("I feel like I am going to break down", "anxious"),
    ("I cannot breathe properly when I am tense", "anxious"),
    ("Everything feels out of control", "anxious"),
    ("I feel trapped and suffocated", "anxious"),

    # FRUSTRATED
    ("I am very frustrated with how things are", "frustrated"),
    ("No matter what I do it is never enough", "frustrated"),
    ("I try so hard but nothing works out", "frustrated"),
    ("I am fed up with the same problems every day", "frustrated"),
    ("Why does this keep happening to me", "frustrated"),
    ("I feel stuck and cannot move forward", "frustrated"),
    ("Nothing is going the way I want", "frustrated"),
    ("I put so much effort but get no result", "frustrated"),
    ("I am irritated with everything around me", "frustrated"),
    ("I cannot take this anymore", "frustrated"),
    ("I feel like nobody appreciates my efforts", "frustrated"),
    ("Same arguments happen every single day", "frustrated"),
    ("I am tired of trying to explain myself", "frustrated"),
    ("I feel misunderstood all the time", "frustrated"),
    ("Things never change no matter what I do", "frustrated"),
    ("I am annoyed and have no patience left", "frustrated"),
    ("I feel like my efforts are wasted", "frustrated"),
    ("I hate this situation I am in", "frustrated"),
    ("Nothing is working in my favor", "frustrated"),
    ("I am completely exhausted from trying", "frustrated"),

    # CALM
    ("I am feeling okay today", "calm"),
    ("I want to find peace in my life", "calm"),
    ("I am trying to stay positive", "calm"),
    ("I want to improve my relationship with my family", "calm"),
    ("I am learning to control my emotions", "calm"),
    ("Today I feel a little better", "calm"),
    ("I am grateful for small things in life", "calm"),
    ("I want to communicate better with everyone", "calm"),
    ("I am taking deep breaths to stay calm", "calm"),
    ("I feel relaxed and at ease", "calm"),
    ("Things will get better slowly", "calm"),
    ("I am at peace with myself today", "calm"),
    ("I want to spread happiness around me", "calm"),
    ("I am hopeful about the future", "calm"),
    ("I feel balanced and in control", "calm"),
    ("I am doing well and feeling good", "calm"),
    ("I am happy with my family today", "calm"),
    ("Life is good and I am thankful", "calm"),
    ("I feel loved and supported", "calm"),
    ("Everything is fine and I am okay", "calm"),
]

df = pd.DataFrame(data, columns=["text", "emotion"])
df.to_csv("data/emotions_data.csv", index=False)
print(f"✅ Dataset created: {len(df)} samples")
print(df["emotion"].value_counts())
