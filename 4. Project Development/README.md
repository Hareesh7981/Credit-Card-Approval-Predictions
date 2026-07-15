# Project Development

## Overview

The Project Development phase focuses on implementing the Credit Card Approval Prediction System using Machine Learning techniques. This phase includes data preprocessing, feature engineering, model training, model evaluation, and the development of a Flask-based web application for predicting credit card approval.

---

## Project Components

The Project Development folder contains the following components:

### Dataset
Contains the datasets used for training and testing the machine learning models.

- application_record.csv
- credit_record.csv

---

### Jupyter Notebook

**credit_approval_pipeline.ipynb**

This notebook includes:

- Importing required libraries
- Data loading
- Data cleaning
- Data preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Model training
- Model evaluation
- Feature importance analysis
- Model saving

---

### Machine Learning Model

**credit_card_model.pkl**

The trained Random Forest model is saved using Joblib and is used by the Flask application to make predictions.

---

### Flask Application

**app.py**

The Flask application provides a simple web interface that allows users to enter applicant details and receive an instant credit card approval prediction.

---

### Templates

The **templates** folder contains:

- index.html

This HTML page provides the user interface for entering applicant information and displaying prediction results.

---

### Static Files

The **static** folder contains:

- style.css

This file is responsible for the styling and appearance of the web application.

---

### Requirements

**requirements.txt**

Lists all Python libraries required to run the project.

Example packages include:

- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- XGBoost

---

## Machine Learning Workflow

The project follows these steps:

1. Load the datasets
2. Merge applicant and credit records
3. Clean and preprocess the data
4. Perform feature engineering
5. Train multiple machine learning models
6. Compare model performance
7. Select the best-performing model
8. Save the trained model
9. Deploy the model using Flask

---

## Models Used

The following classification algorithms were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Among these, the **Random Forest Classifier** achieved the best performance and was selected for deployment.

---

## Output

The system predicts whether a credit card application should be:

- ✅ Approved
- ❌ Rejected

based on the applicant's financial and personal information.

---

## Expected Outcome

The developed system automates the credit card approval process, reduces manual effort, improves prediction accuracy, and provides quick decision support for financial institutions.
