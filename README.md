Soil Quality Predictor
Project Overview
This project is a web-based application that uses a machine learning model to predict the most suitable crop for a given set of soil and environmental conditions. The application provides a user-friendly interface where a user can input various parameters such as Nitrogen, Phosphorus, and Potassium levels, as well as temperature, humidity, pH, and rainfall.

The web interface is built with HTML and styled using Tailwind CSS. The backend is a Flask application that serves the HTML pages, processes user input, and interacts with the trained machine learning model to provide a crop recommendation and a soil quality score.

Features
Interactive Interface: A simple and intuitive user interface with smooth scrolling between sections.

Data-Driven Predictions: A machine learning model, trained on the Crop_recommendation.csv dataset, provides accurate crop recommendations.

Soil Quality Score: The application provides a confidence score (from 1 to 100) for the prediction, indicating the quality of the soil for the recommended crop.

Dynamic Visuals: Displays an image of the recommended crop on the results page.

Team Showcase: A dedicated section to highlight the project's development team.

Getting Started
To get this application up and running on your local machine, follow these steps.

Prerequisites
You will need the following installed on your system:

Python 3.x

Pip (Python's package installer)

File Structure
Ensure your project directory is organized as follows:

soil_predictor/
├── app.py
├── crop_model.pkl
├── scaler.pkl
├── Crop_recommendation.csv
├── templates/
│   └── index.html
└── static/
    └── images/
        ├── ameya.jpeg
        ├── anu.jpeg
        ├── cherian.jpeg
        ├── gowri.jpeg
        ├── apple.jpeg
        ├── banana.jpeg
        ├── blackgram.jpeg
        ├── carrot.png
        ├── chickpea.jpeg
        ├── chickpea.png
        ├── coconut.jpeg
        ├── coffee.jpeg
        ├── corn.png
        ├── cotton.jpeg
        ├── grapes.jpeg
        ├── jute.jpeg
        ├── kidneybeans.jpg
        ├── lentil.jpeg
        ├── maize.jpeg
        ├── mango.jpg
        ├── mothbeans.jpeg
        ├── mungbean.jpeg
        ├── muskmelon.jpeg
        ├── orange.jpeg
        ├── papaya.jpeg
        ├── pigeonpeas.jpeg
        ├── pomegranate.jpeg
        ├── rice.jpeg
        ├── soyabean.png
        ├── tomato.png
        ├── watermelon.jpeg
        └── wheat.png

Installation
Clone the repository or create the project structure manually.

Install the required Python packages.
Create a requirements.txt file and add the following:

Flask
numpy
scikit-learn
pandas

Then, run the following command in your terminal:

pip install -r requirements.txt

Ensure the Model and Scaler are in place.
The app.py file loads crop_model.pkl and scaler.pkl. These files should be placed in the main directory alongside app.py. The model was trained on the provided Crop_recommendation.csv dataset.

Running the Application
To start the web server, navigate to your project's root directory in the terminal and run:

python app.py

The application will start running on your local machine, typically at http://127.0.0.1:5000. Open this URL in your web browser to use the application.

Usage
Open the application in your browser. The landing page provides a brief overview of the tool.

Click "BEGIN ANALYSIS" to navigate to the input page.

Enter the soil and environmental data in the provided fields. The input fields have clear labels and expected value ranges.

Click "ANALYZE SOIL DATA". The page will scroll to the results section, displaying the recommended crop and a soil quality score.

Click "RESTART ANALYSIS" to clear the form and return to the main page for a new prediction.

Dataset and Model
The model is a RandomForestClassifier trained on the Crop_recommendation.csv dataset. The features used for training are N, P, K, temperature, humidity, pH, and rainfall. A StandardScaler was used to preprocess the data before training.