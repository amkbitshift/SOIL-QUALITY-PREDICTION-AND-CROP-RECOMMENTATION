🌾 Soil Quality Predictor & Crop Recommendation System
This project is a data science web application that uses machine learning to predict the most suitable crop for a given set of soil and environmental parameters. It showcases a complete end-to-end Machine Learning deployment pipeline.

🚀 Live Application Link (ACTIVE LINK)
The link below is your current, working public URL. Note: This link is temporary and will change if you close your ngrok terminal.

Status

Link

Note

LIVE & Sharable

Launch the Soil Quality Predictor Live 🚀

This link is active only while your Python and ngrok terminal windows are running.

Key Features
Data-Driven Predictions: Uses a Random Forest Classifier trained on the Crop_recommendation.csv dataset.

Soil Quality Score: Provides a confidence score (from 1 to 100) for the prediction, indicating the quality of the soil for the recommended crop.

Scalable Backend: Built with Flask for serving the web interface and handling API requests.

Model Persistence: Uses the joblib library for efficient loading of the trained model and StandardScaler.

Clean Interface: User-friendly web interface (index.html) for easy data input and result visualization.

Data Science Workflow (KTU Syllabus Alignment)
This project demonstrates a full data science lifecycle:

Stage

Process

Artifacts

1. Data Preprocessing

Cleansing checks (Duplicates, Missing Values), Feature Scaling, and Data Transformation.

colab_model_training.ipynb

2. Model Training

Selection, training, and evaluation of a RandomForestClassifier.

crop_model.joblib

3. Deployment

Serving the prediction model using a Flask API and making it publicly accessible via a cloud server.

app.py, requirements.txt, Procfile

💻 Getting Started (Local Setup)
To run this project on your own machine without using the ngrok tunnel:

Prerequisites
Python 3.8+

The index.html file must be inside a folder named templates.

1. Installation
Install all required Python packages using the provided requirements.txt file.

pip install -r requirements.txt


2. File Structure
Ensure your project directory contains these files:

soil_crop_prediction/
├ ── app.py
├ ── requirements.txt
├ ── Procfile  <-- MANDATORY for Permanent Hosting!
├ ── crop_model.joblib
├ ── scaler.joblib
└ ── templates/
    └ ── index.html


3. Run the Application
To run the application locally on your PC (non-sharable):

python app.py


Open your browser to: http://127.0.0.1:5000
