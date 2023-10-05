import pickle
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox, simpledialog

with open('data/model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('data/labeler.pkl', 'rb') as file:
    labeler = pickle.load(file)


def group_age(age):
    '''
    Simple function for age grouping
    '''
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

def predict(data):
    '''
    This function predicts the mortality of the heart failure given the data from the app.
    It transforms the data into desired format and then puts them through the model.
    The results are given as a string information.
    '''
    data['Others'] = data['Others'].replace(r',\s*|,', ', ', regex=True)
    data['Others'] = data['Others'].map(labeler['Others'])
    data['SKReact'] = data['SKReact'].map(labeler['Others'])
    
    df = pd.Dataframe({'AgeGroup': group_age(int(data['Age'])),
                       'Gender': [0 if data['Gender'] == 'Female' else 1],
                       'Smoking': [0 if data['Smoking'] == 'No' else 1],
                       'HTN': [0 if data['HTN'] == 'No' else 1],
                       'Others': data['Others'],
                       'SKReact': data['SKReact'],
                       'Age': int(data['Age']),
                       'FHistory': [0 if data['FHistory'] == 'No' else 1],
                       'Diabetes': [0 if data['Diabetes'] == 'No' else 1],
                       'WBC': int(data['WBC']),
                       'oldpeak': float(data['oldpeak']),
                       'ca':int(data['ca']),
                       'Reaction': [0 if data['Reaction'] == 'No' else 1],
                       'FollowUp': int(data['FollowUp'])})
    
    pred = model.predict(df)
    if pred == 1:
        prediction = 'You should survive a heart failure!\n Keep up your good health!'
    else:
        prediction = 'You might not survive a heart failure.\n Take care of your health!'

    return prediction


# Funkcja przewidzenia
def predict_button_click():
    '''
    This function collect the data from all the fields in the app into a dictionary.
    It also uses the predict() function and returns the result to the end user.
    '''
    data = {}

    features_with_input = ["Age", "WBC", "oldpeak", "FollowUp", "Others", "SKReact", "ca"]

    for feature in features_with_input:
        entry = second_column.children[feature]
        if entry:
            user_input = entry.get()
            if not user_input:
                error_label.config(text=f"Please input all values")
                return
            data[feature] = user_input

    data["Gender"] = gender_var.get()

    features_binary = ["Smoking", "HTN", "FHistory", "Diabetes"]

    for feature in features_binary:
        checkbox = third_column.children[feature]
        if checkbox:
            data[feature] = checkbox.var.get()

    
    prediction = predict(data)
    messagebox.showinfo("Prediction", prediction)

# Main window
root = tk.Tk()
root.title("Heart Failure Predictions")

# First container - title and description
first_column = tk.Frame(root, width=200)
first_column.pack(side="left", padx=10, pady=10)

# Title
title_label = tk.Label(first_column, text="Fatality of Heart Failure", font=("Helvetica", 14, "bold"))
title_label.pack(pady=(0, 10), anchor="w")

# Description
text_content = "jjdhsfsgs\n" + "ogrdfkjgskjg\n" + "blablabla\n" * 20  
text_label = tk.Label(first_column, text=text_content)
text_label.pack(anchor="w")

# Second containter - input data
second_column = tk.Frame(root)
second_column.pack(side="left", padx=10, pady=10)

# Features to be used
features_with_input = ["Age", "WBC", "oldpeak", "followup", "other", "skreact", "ca"]

# Creation of labels and fields
for idx, feature in enumerate(features_with_input):
    label = tk.Label(second_column, text=f"{feature}:", font=("Helvetica", 10, "bold"))
    label.grid(row=idx*2, column=0, sticky="w", pady=(5, 0))
    entry = tk.Entry(second_column)
    entry.grid(row=idx*2+1, column=0, sticky="e", pady=(0, 5))

# Third container - binary fields
third_column = tk.Frame(root)
third_column.pack(side="left", padx=10, pady=10)

# Gender 
label_gender = tk.Label(third_column, text="Gender:", font=("Helvetica", 10, "bold"))
label_gender.grid(row=0, column=0, sticky="w", pady=(5, 0))

gender_var = tk.StringVar(value="Female")  # Początkowa wartość to "Female"
gender_radio_female = tk.Radiobutton(third_column, text="Female", variable=gender_var, value="Female", font=("Helvetica", 10))
gender_radio_female.grid(row=1, column=0, sticky="w")

gender_radio_male = tk.Radiobutton(third_column, text="Female", variable=gender_var, value="Male", font=("Helvetica", 10, "bold"))
gender_radio_male.grid(row=2, column=0, sticky="w")

# Other binary features
features_binary = ["Smoking", "HTN", "FHistory", "Diabetes"]

# Creation of labels and fields
for idx, feature in enumerate(features_binary):
    label = tk.Label(third_column, text=f"{feature}:", font=("Helvetica", 10))
    label.grid(row=(idx+3)*2, column=0, sticky="w", pady=(5, 0))
    var = tk.IntVar(value=0)  # Zmienna przechowująca wybór (0 lub 1)
    checkbox_yes = tk.Radiobutton(third_column, text="Yes", variable=var, value=1, font=("Helvetica", 10, "bold"))
    checkbox_yes.grid(row=(idx+3)*2+1, column=0, sticky="w")

    checkbox_no = tk.Radiobutton(third_column, text="No", variable=var, value=0, font=("Helvetica", 10, "bold"))
    checkbox_no.grid(row=(idx+3)*2+1, column=1, sticky="w")

# Potential error label
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=(10, 0))

# Prediction call
predict_button = tk.Button(root, text="Predict", font=("Helvetica", 12, "bold"), command=predict_button_click)
predict_button.pack(pady=20)

# Main loop
root.mainloop()
