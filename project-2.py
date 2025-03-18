import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample data (replace with real data)
data = {'url': ['https://bank-secure-login.com', 'https://google.com', 'https://secure-update.net'],
        'label': [1, 0, 1]}  # 1 = phishing, 0 = safe

df = pd.DataFrame(data)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df['url'], df['label'], test_size=0.2, random_state=42)

# Convert URLs into feature vectors
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Predict on test set
y_pred = model.predict(X_test_vectorized)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Test example
test_url = ['https://login-secure-bank.com']
test_vector = vectorizer.transform(test_url)
prediction = model.predict(test_vector)[0]

if prediction == 1:
    print(f"{test_url[0]} is a phishing site! 🚨")
else:
    print(f"{test_url[0]} is safe ✅")
