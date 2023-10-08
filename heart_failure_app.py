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



# def predict(data):
#     data['Others'] = data['Others'].replace(r',\s*|,', ', ', regex=True)
#     data['Others'] = data['Others'].map(labeler['Others'])
#     data['SKReact'] = data['SKReact'].str.lower().str.strip()
#     data['SKReact'] = data['SKReact'].map(labeler['Others'])
    

#     df = pd.DataFrame({'AgeGroup': [group_age(int(data['Age']))],
#                        'Gender': [0 if data['Gender'] == 'Female' else 1],
#                        'Smoking': [0 if data.get('Smoking') == 'No' else 1],
#                        'HTN': [0 if data.get('HTN') == 'No' else 1],
#                        'Others': [data.get('Others')],
#                        'SKReact': [data.get('SKReact')],
#                        'Age': [int(data.get('Age'))],
#                        'FHistory': [0 if data.get('FHistory') == 'No' else 1],
#                        'Diabetes': [0 if data.get('Diabetes') == 'No' else 1],
#                        'WBC': [int(data.get('WBC'))],
#                        'oldpeak': [float(data.get('oldpeak'))],
#                        'ca': [int(data.get('ca'))],
#                        'Reaction': [0 if data.get('Reaction') == 'No' else 1],
#                        'FollowUp': [int(data.get('FollowUp', 0))]})

#     pred = model.predict(df)
#     if pred == 1:
#         prediction = 'You should survive a heart failure!\n Keep up your good health!'
#     else:
#         prediction = 'You might not survive a heart failure.\n Take care of your health!'

#     return prediction


# Streamlit app
st.title("Heart Failure Predictions")

# Get user inputs
age = st.number_input("Age", min_value=0, value=30)
wbc = st.number_input("WBC", min_value=0, value=30)
oldpeak = st.number_input("oldpeak", min_value=0, value=30)
followup = st.number_input("FollowUp", min_value=0, value=30)
ca = st.number_input("ca", min_value=0, value=30)
others = st.text_input("Others", "wartość")
skreact = st.text_input("SKReact", "wartość")

# Add other input fields similarly

gender = st.radio("Gender", ["Female", "Male"])

# Checkbox for binary features
smoking = st.checkbox("Smoking")
htn = st.checkbox("HTN")
fhistory = st.checkbox("FHistory")
diabetes = st.checkbox("Diabetes")
reaction = st.checkbox("Reaction")

others = re.sub(r',\s*|,', ', ', others)


skreact = skreact.lower().strip()


    
# Call the predict function on button click
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
