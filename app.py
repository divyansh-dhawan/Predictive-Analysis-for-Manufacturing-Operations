from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("logistic_regression_model.pkl")  
label_encoder = joblib.load("label_encoder.pkl")      

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON
        input_data = request.json
        temperature = input_data.get("Temperature")
        run_time = input_data.get("Run_Time")

        if temperature is None or run_time is None:
            return jsonify({"error": "Temperature and Run_Time are required fields."}), 400

        # Use the average Machine_ID if not provided
        machine_id_encoded = np.mean(label_encoder.transform(label_encoder.classes_))

        # Create input array for prediction
        features = np.array([[machine_id_encoded, temperature, run_time]])

        # Make prediction
        probabilities = model.predict_proba(features)[0]
        predicted_class = model.predict(features)[0]

        # Prepare response
        downtime = "Yes" if predicted_class == 1 else "No"
        confidence = round(max(probabilities), 2)

        return jsonify({"Downtime": downtime, "Confidence": confidence})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
