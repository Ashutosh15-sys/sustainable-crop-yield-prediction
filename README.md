✅ About the Project
Accurate forecasting of crop yields is essential for enhancing agricultural efficiency and ensuring food security. This project uses a Decision Tree Regressor to predict crop yield based on:

Average Rainfall

Temperature

Pesticide usage

Carbon Emissions

Crop type

Geographic Area

It combines a trained ML model with a Flask-based web interface for easy access and use.

🧰 Tech Stack
Python

Flask

scikit-learn

Pandas / NumPy

HTML / CSS / Bootstrap

Matplotlib / Seaborn (for EDA)

🚀 Features
Predicts crop yield with high accuracy.

User-friendly web interface.

Feature importance visualization.

Real-time predictions based on user input.

Environment-aware decision-making tool.

📊 Dataset
The dataset includes:

Year

Average Rainfall (mm/year)

Pesticides Used (tonnes)

Average Temperature (°C)

Carbon Footprint (kg CO₂/ha)

Area

Item (Crop Type)

🗂️ Format: CSV

✅ Preprocessing:

Handled missing values and outliers

Encoded categorical features

Normalized numerical features

📈 Model
Model Used: Decision Tree Regressor

Performance Metrics:

R² Score: ~0.87

Mean Squared Error (MSE): Low

Reason for DTR: Offers balance between interpretability and performance.

🌐 Web App Interface
Developed using Flask

Users can input environmental parameters

Displays yield prediction instantly

Can be deployed locally or on cloud (e.g., Heroku/AWS)

🧪 How to Run Locally
# 1. Clone the repository
git clone https://github.com/your-username/crop-yield-predictor.git
cd crop-yield-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app_updated.py

📊 Results
Heatmaps and scatter plots revealed strong correlations between rainfall, pesticide usage, and yield.

The model outperformed linear regression and random forest in tests.

Yield predictions were accurate for various crops: Maize, Rice, Wheat, Potato, etc.

🔮 Future Scope
Use advanced models like XGBoost or Deep Learning (ANNs, CNNs)

Incorporate real-time weather APIs

Add soil data or satellite imagery for higher accuracy

Mobile App integration
