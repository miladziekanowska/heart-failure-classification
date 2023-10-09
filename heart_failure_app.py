import pickle
import re
import numpy as np
import pandas as pd
import streamlit as st

with open('data/model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('data/labeler.pkl', 'rb') as file:
    labeler = pickle.load(file)


def group_age(age):
    if age <= 30:
        return 1
    elif age <= 40:
        return 2
    elif age <= 50:
        return 3
    elif age <= 60:
        return 4
    elif age <= 70:
        return 5
    elif age < 80:
        return 6
    
# Streamlit app
st.title("Heart Failure Predictions")

left_column, right_column = st.columns(2)

with left_column:
    st.header('Description')
    st.header("Welcome to the heart failure prediction app!")
    st.write("In this app you can predict the outcome of a heart failure.")
    st.write("Please input your data and check the outcome.")
    st.write("\n")
    st.write("Age:  input your age;")
    st.write("WBC: input quantity of white blood cells;")
    st.write("Oldpeak: input measure of ST segment depression in ECG post-exercise;")
    st.write("FollowUp: input the number of doctor appointemnt regarding heart health;")
    st.write("Ca: input number of major blood vessels colored in fluoroscopy")
    st.write("Others: choose if you have any other issues;")
    st.write("SKReakt: choose if one of these are true;")
    st.write("Gender: choose your gender;")
    st.write("Smoking: choose if you are smoking;")
    st.write("HTN: choose if you have hipertension;")
    st.write("FHistory: choose if you have family history of heart failures;")
    st.write("Reaction: choose if any reaction occurred.")
    st.write("\n")
    st.write("\n")
    st.write("This model and app are not a diagnosis.")
    st.write("If you receive a bad result, please contact your doctor.")

with right_column:
    st.header('Input Values')
    age = st.number_input("Age", min_value=0, value=30)
    wbc = st.number_input("WBC", min_value=0, value=30)
    oldpeak = st.number_input("oldpeak", min_value=0, value=30)
    followup = st.number_input("FollowUp", min_value=0, value=30)
    ca = st.number_input("ca", min_value=0, value=30)


    others = st.radio("Others", labeler['Others'].values())
    others = labeler['Others'].get(others, others)

    skreact = st.radio("SKReact", labeler['SKReact'].values())
    skreact = labeler['SKReact'].get(skreact, skreact)


    gender = st.radio("Gender", ["Female", "Male"])

    # Checkbox for binary features
    smoking = st.checkbox("Smoking")
    htn = st.checkbox("HTN")
    fhistory = st.checkbox("FHistory")
    diabetes = st.checkbox("Diabetes")
    reaction = st.checkbox("Reaction")

    others = re.sub(r',\s*|,', ', ', others)
    skreact = skreact.lower().strip()

    if st.button("Predict"):

        data = {
            "AgeGroup": [group_age(int(age))],
            "Gender": [0 if gender == 'Female' else 1],
            "Smoking": 1 if smoking else 0,
            "HTN": 1 if htn else 0,
            "Others": others,
            "SKReact": skreact,
            "Age": int(age),
            "FHistory": 1 if fhistory else 0,
            "Diabetes": 1 if diabetes else 0,
            "WBC": int(wbc),
            "oldpeak": float(oldpeak),
            "ca": int(ca),
            "Reaction": 1 if reaction else 0,
            "FollowUp": int(followup)
        }



        df = pd.DataFrame(data)
        df['Others'] = df['Others'].map(labeler['Others']).astype(float)
        df['SKReact'] = df['SKReact'].map(labeler['SKReact']).astype(float)

        pred = model.predict(df)
        if pred == 1:
            prediction = 'You should survive a heart failure!\n Keep up your good health!'
        else:
            prediction = 'You might not survive a heart failure.\n Take care of your health!'

        st.write(prediction)
