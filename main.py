import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Load trained model
# ------------------------------
model = joblib.load("thyroid_model.pkl")

# ------------------------------
# Page Title
# ------------------------------
st.set_page_config(page_title="Thyroid Recurrence Prediction", page_icon="🧬")
st.title("🧬 Thyroid Recurrence Prediction")
st.write("This app predicts the likelihood of **thyroid cancer recurrence** based on pre-treatment clinical data.")

# ------------------------------
# Input Fields
# ------------------------------
age = st.number_input("Age", min_value=1, max_value=120, value=35)

gender = st.selectbox("Gender", ["Female", "Male"])
smoking = st.selectbox("Smoking", ["No", "Yes"])
hx_smoking = st.selectbox("History of Smoking (Hx Smoking)", ["No", "Yes"])
hx_radiotherapy = st.selectbox("History of Radiotherapy (Hx Radiotherapy)", ["No", "Yes"])

thyroid_function = st.selectbox("Thyroid Function", [
    "Clinical Hyperthyroidism",
    "Clinical Hypothyroidism",
    "Euthyroid",
    "Subclinical Hyperthyroidism",
    "Subclinical Hypothyroidism"
])

physical_exam = st.selectbox("Physical Examination", [
    "Diffuse goiter",
    "Multinodular goiter",
    "Normal",
    "Single nodular goiter-left",
    "Single nodular goiter-right"
])

adenopathy = st.selectbox("Adenopathy", [
    "Bilateral",
    "Extensive",
    "Left",
    "No",
    "Posterior",
    "Right"
])

pathology = st.selectbox("Pathology", [
    "Follicular",
    "Hurthel cell",
    "Micropapillary",
    "Papillary"
])

focality = st.selectbox("Focality", [
    "Multi-Focal",
    "Uni-Focal"
])

T = st.selectbox("Tumor (T)", ["T1a", "T1b", "T2", "T3", "T4"])
N = st.selectbox("Node (N)", ["N0", "N1a", "N1b"])
M = st.selectbox("Metastasis (M)", ["M0", "M1"])

# ------------------------------
# Encode Inputs (alphabetical LabelEncoder logic)
# ------------------------------
def encode_input():
    return pd.DataFrame([{
        "Age": age,
        "Gender": ["Female", "Male"].index(gender),
        "Smoking": ["No", "Yes"].index(smoking),
        "Hx Smoking": ["No", "Yes"].index(hx_smoking),
        "Hx Radiotherapy": ["No", "Yes"].index(hx_radiotherapy),
        "Thyroid Function": [
            "Clinical Hyperthyroidism",
            "Clinical Hypothyroidism",
            "Euthyroid",
            "Subclinical Hyperthyroidism",
            "Subclinical Hypothyroidism"
        ].index(thyroid_function),
        "Physical Examination": [
            "Diffuse goiter",
            "Multinodular goiter",
            "Normal",
            "Single nodular goiter-left",
            "Single nodular goiter-right"
        ].index(physical_exam),
        "Adenopathy": [
            "Bilateral",
            "Extensive",
            "Left",
            "No",
            "Posterior",
            "Right"
        ].index(adenopathy),
        "Pathology": [
            "Follicular",
            "Hurthel cell",
            "Micropapillary",
            "Papillary"
        ].index(pathology),
        "Focality": [
            "Multi-Focal",
            "Uni-Focal"
        ].index(focality),
        "T": ["T1a", "T1b", "T2", "T3", "T4"].index(T),
        "N": ["N0", "N1a", "N1b"].index(N),
        "M": ["M0", "M1"].index(M)
    }])

# ------------------------------
# Prediction Button
# ------------------------------
if st.button("Predict"):
    input_df = encode_input()
    prediction = model.predict(input_df)[0]
    confidence = model.predict_proba(input_df)[0][prediction] * 100

    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error(f"""
        🔴 **High Chance of Recurrence**

        Based on the provided clinical information, the model predicts a **high likelihood of thyroid cancer recurrence**.  
        **Confidence:** {confidence:.2f}%

        _Note: This prediction is based on statistical patterns from historical data and should support, not replace, clinical judgment._
        """)
    else:
        st.success(f"""
        🟢 **Low Chance of Recurrence**

        Based on the provided clinical information, the model predicts a **low likelihood of recurrence**.  
        **Confidence:** {confidence:.2f}%

        _Note: This prediction is based on statistical patterns from historical data and should support, not replace, clinical judgment._
        """)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("Developed for thyroid cancer recurrence prediction using pre-treatment clinical features.")
