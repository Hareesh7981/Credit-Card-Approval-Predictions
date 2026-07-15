# Dataset

## Overview

This folder contains the datasets used for developing and evaluating the **Credit Card Approval Prediction** system. These datasets provide applicant details and historical credit records required for training and testing the machine learning models.

---

## Dataset Files

### 1. application_record.csv

This dataset contains personal and financial information about credit card applicants.

**Sample Attributes:**
- ID
- Gender
- Car Ownership
- Property Ownership
- Number of Children
- Annual Income
- Income Type
- Education Type
- Family Status
- Housing Type
- Employment Days
- Occupation Type
- Family Members

---

### 2. credit_record.csv

This dataset contains the historical credit repayment records of applicants.

**Sample Attributes:**
- ID
- Month Balance
- Credit Status

The credit status values indicate whether an applicant has a good or poor repayment history and are used to generate the target variable for model training.

---

## Dataset Usage

The datasets are used for:

- Data preprocessing
- Data cleaning
- Feature engineering
- Exploratory Data Analysis (EDA)
- Model training
- Model evaluation
- Credit card approval prediction

---

## Preprocessing Steps

Before model training, the following preprocessing operations are performed:

- Remove duplicate records
- Handle missing values
- Merge application and credit datasets
- Encode categorical variables
- Scale numerical features
- Generate the target variable

---

## Machine Learning Purpose

The processed dataset is used to train and evaluate multiple classification algorithms, including:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The best-performing model is selected based on evaluation metrics and saved for deployment.

---

## Note

The datasets are intended for educational and research purposes. They are used to demonstrate the application of Machine Learning techniques in predicting credit card approval decisions.
