# Project Design & Planning

## Overview

The Project Design & Planning phase defines the overall architecture, workflow, and implementation strategy of the Credit Card Approval Prediction System. This phase focuses on designing the system structure, planning project activities, and preparing the development roadmap.

A well-planned design ensures that the project is scalable, maintainable, and easy to understand while meeting all functional and non-functional requirements.

---

## Purpose

The objectives of this phase are to:

- Design the overall system architecture.
- Define the project workflow.
- Create UML and ER diagrams.
- Plan project milestones and development activities.
- Prepare the implementation strategy.
- Identify system modules and their interactions.

---

## Contents

This folder contains the following documents:

- Project Architecture
- Workflow Diagram
- ER Diagram
- Use Case Diagram
- Project Milestones
- Implementation Plan

---

## System Design

The Credit Card Approval Prediction System consists of the following major modules:

### 1. Data Collection Module
- Loads applicant and credit history datasets.
- Validates input data.

### 2. Data Preprocessing Module
- Removes duplicate records.
- Handles missing values.
- Encodes categorical variables.
- Performs feature engineering.

### 3. Machine Learning Module
- Trains multiple classification algorithms.
- Compares model performance.
- Selects the best-performing model.

### 4. Prediction Module
- Accepts applicant details.
- Uses the trained model to predict credit card approval.
- Displays the prediction result.

### 5. Web Application Module
- Provides a user-friendly interface using Flask.
- Accepts user input.
- Displays prediction results instantly.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- Joblib
- Google Colab
- Git & GitHub

---

## Expected Outcome

At the end of this phase, the complete system architecture, workflow, implementation strategy, and project plan are finalized, providing a clear roadmap for project development and deployment.
