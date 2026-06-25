"""
train_model.py
Trains a TF-IDF + Logistic Regression model to detect emotions from text.
Saves the trained model for use in predict.py
"""
import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

os.makedirs("data", exist_ok=True)

df = pd.read_csv("data/emotions_data.csv")
X = df["text"]
y = df["emotion"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# TF-IDF converts text into numbers the ML model can understand
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=500)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_vec, y_train)

preds = model.predict(X_test_vec)
acc   = accuracy_score(y_test, preds)

print(f"\n✅ Model trained successfully!")
print(f"   Accuracy : {acc*100:.1f}%")
print(f"\n{classification_report(y_test, preds)}")

# Save model and vectorizer
with open("data/model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("data/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model saved to data/model.pkl")
print("✅ Vectorizer saved to data/vectorizer.pkl")
