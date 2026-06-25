"""
visualize.py
Creates charts and graphs showing how the emotion detection model works.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pickle
import os
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/emotions_data.csv")

with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)
with open("data/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

COLORS = {
    "angry":      "#e74c3c",
    "sad":        "#3498db",
    "anxious":    "#f39c12",
    "frustrated": "#9b59b6",
    "calm":       "#2ecc71",
}

# ── Plot 1: Emotion Distribution ──────────────────────────────
plt.figure(figsize=(9, 5))
counts = df["emotion"].value_counts()
bars = plt.bar(counts.index,
               counts.values,
               color=[COLORS[e] for e in counts.index],
               edgecolor="white", linewidth=1.5)
for bar, val in zip(bars, counts.values):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.3,
             str(val), ha="center", fontweight="bold", fontsize=12)
plt.title("Emotion Distribution in Training Data", fontsize=14, fontweight="bold")
plt.ylabel("Number of Samples")
plt.xlabel("Emotion")
plt.tight_layout()
plt.savefig("outputs/01_emotion_distribution.png", dpi=120)
plt.close()
print("✅ Saved: 01_emotion_distribution.png")

# ── Plot 2: Pie Chart ─────────────────────────────────────────
plt.figure(figsize=(7, 7))
plt.pie(counts.values,
        labels=counts.index,
        colors=[COLORS[e] for e in counts.index],
        autopct="%1.1f%%",
        startangle=140,
        textprops={"fontsize": 12})
plt.title("Emotion Share in Dataset", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/02_emotion_pie.png", dpi=120)
plt.close()
print("✅ Saved: 02_emotion_pie.png")

# ── Plot 3: Confusion Matrix ──────────────────────────────────
X = df["text"]
y = df["emotion"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
X_test_vec = vectorizer.transform(X_test)
preds = model.predict(X_test_vec)
labels = ["angry", "anxious", "calm", "frustrated", "sad"]
cm = confusion_matrix(y_test, preds, labels=labels)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=labels, yticklabels=labels)
plt.title("Confusion Matrix — Emotion Detection Model", fontsize=13, fontweight="bold")
plt.ylabel("Actual Emotion")
plt.xlabel("Predicted Emotion")
plt.tight_layout()
plt.savefig("outputs/03_confusion_matrix.png", dpi=120)
plt.close()
print("✅ Saved: 03_confusion_matrix.png")

# ── Plot 4: Model Confidence on Test Sentences ────────────────
test_sentences = [
    "I am very angry at my family",
    "I feel so sad and lonely",
    "I am stressed about my future",
    "Nothing is working and I am fed up",
    "I feel calm and peaceful today",
]
fig, axes = plt.subplots(1, len(test_sentences), figsize=(18, 5))
emotions = model.classes_
for ax, sentence in zip(axes, test_sentences):
    vec = vectorizer.transform([sentence])
    proba = model.predict_proba(vec)[0]
    bar_colors = [COLORS[e] for e in emotions]
    ax.barh(emotions, proba, color=bar_colors)
    ax.set_xlim(0, 1)
    ax.set_title(f'"{sentence[:25]}..."', fontsize=8, fontweight="bold")
    ax.set_xlabel("Confidence")
plt.suptitle("Model Confidence for Sample Sentences", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/04_model_confidence.png", dpi=120)
plt.close()
print("✅ Saved: 04_model_confidence.png")

# ── Plot 5: Average Word Count per Emotion ────────────────────
df["word_count"] = df["text"].apply(lambda x: len(x.split()))
plt.figure(figsize=(9, 5))
avg_words = df.groupby("emotion")["word_count"].mean()
bars = plt.bar(avg_words.index,
               avg_words.values,
               color=[COLORS[e] for e in avg_words.index])
for bar, val in zip(bars, avg_words.values):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.1,
             f"{val:.1f}", ha="center", fontweight="bold")
plt.title("Average Words per Sentence by Emotion", fontsize=13, fontweight="bold")
plt.ylabel("Average Word Count")
plt.xlabel("Emotion")
plt.tight_layout()
plt.savefig("outputs/05_word_count_by_emotion.png", dpi=120)
plt.close()
print("✅ Saved: 05_word_count_by_emotion.png")

# ── Plot 6: Advice Categories Overview ───────────────────────
categories  = ["Breathing\nExercise", "Kind\nWords", "Communication\nTip", "Activity\nSuggestion"]
helpfulness = [92, 88, 85, 79]
plt.figure(figsize=(9, 5))
bar_colors  = ["#1abc9c", "#3498db", "#e67e22", "#9b59b6"]
bars = plt.bar(categories, helpfulness, color=bar_colors, width=0.5)
for bar, val in zip(bars, helpfulness):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.5,
             f"{val}%", ha="center", fontweight="bold", fontsize=12)
plt.ylim(0, 110)
plt.title("Estimated Helpfulness of Each Advice Type", fontsize=13, fontweight="bold")
plt.ylabel("Helpfulness Score (%)")
plt.tight_layout()
plt.savefig("outputs/06_advice_helpfulness.png", dpi=120)
plt.close()
print("✅ Saved: 06_advice_helpfulness.png")

# ── Plot 7: Stress Level Scale ────────────────────────────────
emotions_stress = {
    "calm":       1,
    "sad":        3,
    "anxious":    4,
    "frustrated": 4,
    "angry":      5,
}
plt.figure(figsize=(9, 5))
sorted_items = sorted(emotions_stress.items(), key=lambda x: x[1])
emo_names  = [i[0] for i in sorted_items]
stress_lvl = [i[1] for i in sorted_items]
plt.barh(emo_names, stress_lvl,
         color=[COLORS[e] for e in emo_names], height=0.5)
plt.xlim(0, 6)
plt.axvline(x=3, color="gray", linestyle="--", alpha=0.5, label="Medium Stress")
plt.title("Stress Level by Emotion (1=Low, 5=High)", fontsize=13, fontweight="bold")
plt.xlabel("Stress Level")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/07_stress_levels.png", dpi=120)
plt.close()
print("✅ Saved: 07_stress_levels.png")

print("\n✅ All 7 visualizations saved in outputs/ folder!")
