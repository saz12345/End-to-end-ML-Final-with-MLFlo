from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import traceback
from src.mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    try:
        os.system("python main.py")  # Consider replacing with direct function call
        return "Training successful"
    except Exception as e:
        return f"Training failed: {str(e)}", 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Assuming 'quality' is what we're predicting, remove it from inputs
        expected_fields = [
            'id',
            'fixedAcidity',
            'volatileAcidity',
            'citricAcid',
            'residualSugar',
            'chlorides',
            'freeSO2',
            'totalSO2',
            'density',
            'pH',
            'sulphates',
            'alcohol'
        ]

        input_data = []
        for field in expected_fields:
            value = request.form.get(field)
            if value is None or value.strip() == "":
                return jsonify({'error': f'Missing value for: {field}'}), 400
            try:
                input_data.append(float(value))
            except ValueError:
                return jsonify({'error': f'Invalid number for: {field}'}), 400

        data_array = np.array(input_data).reshape(1, -1)

        pipeline = PredictionPipeline()
        prediction = pipeline.predict(data_array)

        return jsonify({'prediction': f'Predicted wine quality score: {prediction}'})

    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
