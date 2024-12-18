from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

# Example dataset with URL length and HTTPS presence
data = {
    "url_length": [20, 35, 60, 15, 75],
    "has_https": [1, 1, 0, 0, 0],
    "label": [0, 0, 1, 0, 1],  # 0 = Legitimate, 1 = Phishing
}
df = pd.DataFrame(data)

# Split dataset
X = df[["url_length", "has_https"]]
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save model
joblib.dump(model, "phishing_model.pkl")
print("Model saved as phishing_model.pkl")
