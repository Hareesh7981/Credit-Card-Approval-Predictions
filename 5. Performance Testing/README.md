# Performance Testing

## Overview

The Performance Testing phase evaluates the effectiveness, reliability, and accuracy of the Credit Card Approval Prediction System. Multiple machine learning models were trained and compared using standard classification evaluation metrics to identify the best-performing model.

---

## Purpose

The objectives of this phase are to:

- Evaluate the performance of different machine learning models.
- Compare model accuracy and other evaluation metrics.
- Analyze prediction results using visualizations.
- Select the best model for deployment.

---

## Performance Metrics

The following evaluation metrics were used:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

These metrics help assess the prediction quality and overall performance of the trained models.

---

## Machine Learning Models Evaluated

The following classification algorithms were implemented and tested:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The **Random Forest Classifier** achieved the best performance and was selected as the final model for deployment.

---

## Testing Artifacts

This folder contains:

- **Accuracy Report** – Overall model accuracy and evaluation metrics.
- **Model Comparison** – Comparison of all trained machine learning models.
- **Testing Summary** – Summary of testing results and observations.
- **Confusion Matrix** – Visual representation of correct and incorrect classifications.
- **ROC Curve** – Performance visualization showing the trade-off between True Positive Rate and False Positive Rate.

---

## Testing Results

The trained Random Forest model demonstrated high prediction accuracy and reliable classification performance on the test dataset. The confusion matrix and ROC curve confirmed the effectiveness of the model in distinguishing approved and rejected credit card applications.

---

## Conclusion

Performance testing confirmed that the Random Forest Classifier is the most suitable model for this project. Based on the evaluation metrics and visual analysis, it was selected for integration into the Flask web application for real-time credit card approval prediction.
