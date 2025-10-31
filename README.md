# 🧬 Thyroid Cancer Recurrence Prediction

📘 Project Overview

This project focuses on developing a machine learning model to predict the likelihood of thyroid cancer recurrence based on clinical, demographic, and pathological features.
It demonstrates an end-to-end medical AI workflow — from data preprocessing and feature encoding to model training, evaluation, and web app deployment using Streamlit.

Objective:
To estimate whether a patient is likely to experience recurrence of thyroid cancer based on pre-treatment features.

# 📊 Dataset Summary
Binary Classification
Target Variable	Type: Recurred (Yes / No)	

Features Used:
Age
Gender
Smoking
Hx Smoking
Hx Radiotherapy
Thyroid Function
Physical Examination
Adenopathy
Pathology
Focality
T (Tumor stage)
N (Lymph node involvement)
M (Metastasis status)

Dropped Columns:
Risk, Stage, and Response — removed to prevent data leakage, since they are derived post-diagnosis and not available at prediction time

# Data Preprocessing & Exploration
Verified data integrity and handled any missing or inconsistent entries.
Renamed typo column Hx Radiothreapy → Hx Radiotherapy.
Dropped derived columns: Risk, Stage, Response.
Applied Label Encoding to categorical features (alphabetical encoding).
Split dataset into 80% training and 20% testing using train_test_split.
Exploration Steps:
Visualized distributions of categorical variables.
Checked recurrence ratios to ensure class balance.
Assessed relationships between variables using correlation and feature inspection

# Model Training & Evaluation
Trained and compared five supervised learning algorithms:

Logistic Regression
Gaussian Naive Bayes
K-Nearest Neighbors (KNN)
Support Vector Machine (SVM)
Random Forest Classifier

Data Split:
80% Training
20% Testing

# Selected Model:
Random Forest Classifier — chosen for its robustness, interpretability, and ability to handle non-linear interactions between features

# Evaluation Metrics:
Accuracy Score
Confusion Matrix
Classification Report (Precision, Recall, F1-Score)
ROC-AUC Curve for performance visualization

AUC Score: 0.88 (Excellent discrimination)
Interpretation: The model achieves an AUC of 0.88, indicating strong ability to distinguish between recurrence and non-recurrence cases.

# Streamlit App Development
Developed a Streamlit web interface (app.py) for interactive predictions.

# Key Features
User-friendly dropdowns for clinical input 
Automatic label encoding matching the training logic
Displays prediction and model confidence (%)
Clean, modern UI with clear clinical explanations

# 📈 Key Takeaways
Built an end-to-end ML pipeline for a real-world medical problem.
Learned to identify and prevent data leakage (dropping post-diagnosis features).
Implemented consistent label encoding across training and inference.
Created an interactive AI-driven clinical decision-support app using Streamlit.
Gained insight into feature importance and interpretability for healthcare ML.

Tools / Libraries Used
pandas, numpy, matplotlib, seaborn, scikit-learn, joblib, Streamlit, Google Colab, Streamlit Cloud 


Dropped Columns:
Risk, Stage, and Response — removed to prevent data leakage, since they are derived post-diagnosis and not available at prediction time.
