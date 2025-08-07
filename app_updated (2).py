from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
import sklearn

print(sklearn.__version__)

# Load trained model and preprocessor
dtr = pickle.load(open('dtr_updated.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor_updated.pkl', 'rb'))

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Retrieve form inputs
            Year = float(request.form['Year'])
            average_rain_fall_mm_per_year = float(request.form['average_rain_fall_mm_per_year'])
            pesticides_tonnes = float(request.form['pesticides_tonnes'])
            avg_temp = float(request.form['avg_temp'])
            carbon_footprint = float(request.form['carbon_footprint'])  # New feature
            Area = request.form['Area']
            Item = request.form['Item']

            # Create DataFrame for transformation
            feature_names = ['Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp', 'carbon_footprint_kg_CO2_ha', 'Area', 'Item']
            features = pd.DataFrame([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, carbon_footprint, Area, Item]], columns=feature_names)
            
            # Transform features using preprocessor
            transformed_features = preprocessor.transform(features)

            # Make prediction
            prediction = dtr.predict(transformed_features).reshape(-1, 1)

            return render_template('index.html', prediction=prediction[0][0])

        except ValueError as e:
            return render_template('index.html', error=f"Invalid input: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
