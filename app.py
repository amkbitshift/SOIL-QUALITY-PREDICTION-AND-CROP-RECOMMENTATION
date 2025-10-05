from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib # Changed from pickle to joblib
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
app = Flask(__name__)

# Load your model and scaler
model = joblib.load("crop_model.joblib") # Changed to load .joblib file
scaler = joblib.load("scaler.joblib") # Changed to load .joblib file

# Home route to serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Your predict route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        N = float(data["N"])
        P = float(data["P"])
        K = float(data["K"])
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
        ph = float(data["ph"])
        rainfall = float(data["rainfall"])

        # Prepare input
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        input_scaled = scaler.transform(input_data)

        # Predict crop
        prediction = model.predict(input_scaled)[0]

        # Soil quality score = model confidence
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_scaled).max() * 100
            soil_quality = round(proba, 2)
        else:
            soil_quality = "N/A" # or a default value

        return jsonify({
            'prediction': prediction,
            'soil_quality': soil_quality
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
