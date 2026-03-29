from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset
messages = [
    "Win money now!!!",
    "Claim your free prize",
    "Hello how are you",
    "Let's meet tomorrow",
    "Free entry in contest",
    "Call me later",
    "Do you wanna get rich in a click",
    "please share your OTP"
]

labels = [
    "spam",
    "spam",
    "ham",
    "ham",
    "spam",
    "ham",
    "spam",
    "spam"
]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test loop
while True:
    msg = input("Enter message: ")
    if msg.lower() == "exit":
        break

    msg_vec = vectorizer.transform([msg])
    prediction = model.predict(msg_vec)[0]

    print("Prediction:", prediction)