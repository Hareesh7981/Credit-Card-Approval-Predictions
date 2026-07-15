# 💳 Credit Card Approval Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![GitHub](https://img.shields.io/badge/GitHub-Project-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Project Overview

The **Credit Card Approval Prediction** project is a Machine Learning application that predicts whether a customer's credit card application is likely to be **Approved** or **Rejected** based on applicant information and credit history.

The system automates the credit approval process by analyzing historical applicant data and applying Machine Learning algorithms to generate accurate predictions. This helps financial institutions reduce manual effort, improve decision-making, and minimize approval risks.

---

# 📑 Table of Contents

- Project Overview
- Features
- Technologies Used
- Dataset
- Project Structure
- Machine Learning Workflow
- Models Used
- Performance Metrics
- Installation
- Project Output
- Future Enhancements
- Author
- License

---

# 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Categorical Feature Encoding
- Random Forest Classification
- Logistic Regression
- Decision Tree Classification
- XGBoost Classification
- Model Comparison
- Performance Evaluation
- Confusion Matrix
- ROC Curve
- Feature Importance Analysis
- Model Saving using Joblib
- Flask Web Application
- GitHub Project Documentation

---

# 🛠 Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Flask
- Git
- GitHub

---

# 📂 Dataset

The project uses two datasets:

### application_record.csv

Contains applicant information such as:

- Gender
- Income
- Employment
- Education
- Family Status
- Housing Type
- Occupation
- Number of Children

### credit_record.csv

Contains applicant credit history including:

- Customer ID
- Credit Status
- Monthly Balance

The datasets are merged and preprocessed before model training.

---

# 📁 Project Structure

```
Credit-Card-Approval-Predictions/

│
├── 1. Brainstorming & Ideation
├── 2. Requirement Analysis
├── 3. Project Design & Planning
├── 4. Project Development
│   ├── Dataset
│   ├── static
│   ├── templates
│   ├── app.py
│   ├── credit_approval_pipeline.ipynb
│   ├── credit_card_model.pkl
│   ├── requirements.txt
│   └── README.md
│
├── 5. Performance Testing
├── 6. Documentation
├── 7. Project Demonstration
│
└── README.md
```

---

# ⚙ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Feature Engineering
5. Data Visualization
6. Model Training
7. Model Evaluation
8. Model Comparison
9. Model Selection
10. Save Best Model
11. Flask Deployment

---

# 🤖 Machine Learning Models Used

The following Machine Learning algorithms were implemented and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

Among all the models, the **Random Forest Classifier** achieved the best performance and was selected as the final deployment model.

---

# 📊 Performance Metrics

The following evaluation metrics were used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- ROC Curve
- Feature Importance

---

# 💻 Installation

## Clone the Repository

```bash
git clone https://github.com/Hareesh7981/Credit-Card-Approval-Predictions.git
```

## Navigate to Project Folder

```bash
cd Credit-Card-Approval-Predictions
```

## Install Required Packages

```bash
pip install -r requirements.txt
```

## Run Flask Application

```bash
python app.py
```

---

# 📈 Project Output

The application predicts whether a customer's credit card application should be:

- ✅ Approved
- ❌ Rejected

based on applicant information and historical credit records.

The trained model is stored as:

```
credit_card_model.pkl
```

---

# 📊 Visual Outputs

The project includes:

- Confusion Matrix
- ROC Curve
- Feature Importance Graph
- Model Comparison Report
- Performance Testing Report

---

# 🌐 Flask Web Application

The Flask web application allows users to:

- Enter applicant details
- Submit information
- Receive instant prediction
- Display approval or rejection result

---

# 🔮 Future Enhancements

- Cloud Deployment (AWS / Azure / IBM Cloud)
- Streamlit Dashboard
- Real-time Prediction API
- Deep Learning Models
- Hyperparameter Optimization
- User Authentication
- Database Integration
- Mobile Application

---

# 👨‍💻 Author

**Hareesh D**

B.Tech – Electrical & Electronics Engineering

Sri Venkateswara College of Engineering

GitHub:

https://github.com/Hareesh7981

LinkedIn:

(Add your LinkedIn profile URL here)

---

# 📜 License

This project was developed for educational purposes as part of the **AI/ML & Generative AI Track**.

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Thank you for visiting this repository!
