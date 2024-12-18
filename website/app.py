from flask import Flask, request, render_template
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "phishing_model.pkl")
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return render_template("index.html", result="Error: Model not loaded.")

    # Get URL from form input
    url = request.form.get("url")
    if url:
        # Feature extraction (example: URL length and HTTPS presence)
        url_length = len(url)
        has_https = 1 if "https" in url else 0
        features = [[url_length, has_https]]

        # Predict using the model
        try:
            prediction = model.predict(features)
            result = "Phishing" if prediction[0] == 1 else "Legitimate"
        except Exception as e:
            result = f"Error during prediction: {e}"
        return render_template("index.html", result=f"The URL is: {result}")

    return render_template("index.html", result="Please enter a valid URL.")

if __name__ == "__main__":
    app.run(debug=True)
