from flask import Flask, render_template, request
import numpy as np
import joblib


app = Flask(__name__)

# Load your trained model
model = joblib.load("my_model.pkl")


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['Electricity_Consumed']),
            float(request.form['Temperature']),
            float(request.form['Humidity']),
            float(request.form['Wind_Speed']),
            float(request.form['Avg_Past_Consumption'])
        ]
        prediction = model.predict([features])[0]
        label = "Anomaly Detected" if prediction == 0 else "Normal Consumption"
        return render_template("index.html", result=label, input_data=features)
    except Exception as e:
        return render_template("index.html", result="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
