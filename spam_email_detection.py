import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("spam.csv")

# Convert labels
data["label"] = data["label"].map({"ham": 0, "spam": 1})

# Features and target
X = data["message"]
y = data["label"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

# User prediction
print("\n===== SPAM EMAIL DETECTOR =====")

message = input("Enter Email Message: ")

message_vector = vectorizer.transform([message])

prediction = model.predict(message_vector)

if prediction[0] == 1:
    print("\nResult: SPAM EMAIL")
else:
    print("\nResult: HAM (NOT SPAM)")
