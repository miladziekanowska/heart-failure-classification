# Heart Failure Prediction ![page](https://img.shields.io/badge/Data%20Analytics-8A2BE2) ![page](https://img.shields.io/badge/Data%20Cleaning-DBC4F0) ![page](https://img.shields.io/badge/Classification-FCAEAE) ![page](https://img.shields.io/badge/Imbalanced%20Data-A1CCD1) ![page](https://img.shields.io/badge/Hypothesis%Testing-D8B4F8)

## Contents
- [About the project](#about_the_project)
- [Wymagania](#requirements)
- [Instalation](#instalation)
- [Usage](#usage)
- [Repositoty structure](#repository_structure)
- [Final model metrics](#final_model_metrics)


## About the project

In this repository, I would like to present my analysis and modeling for a heart failure classification. The main objective in this project is to predict the mortality of a given heart attack in Pakistan realities. The data comes from [this](https://www.kaggle.com/datasets/asgharalikhan/mortality-rate-heart-patient-pakistan-hospital) dataset of heart failures on Kaggle. However, almost all of the data used in the model (except reaction) are not defining a heart failure. But might lead to one, if ignored. Anyone could use this to check, if they would or wouldn't survive a heart failure.
> **Disclaimer!** I am not medical professional, nor is this model. If you have a bad outcome in the model, please don't take it as definite, but consider talking to your doctor and take better care of your health!

As also mentioned in the notebook, some important features were skipped in the dataset, including patients' past in heart failures, their weight, non-direct reason fo heart failure (such as fatigue, accident, stroke) etc, and exclude all external factors, such as proximity to hospital, lenght of CPR, etc, which might contribute to the outcome of a heart failues and mortality of the patietnts.

In this project I ended up using **XGBoostClassifier** as the main model. I used **K-Fold** cross validation to compare the model outcomes and for hyperparameter tuning I used **OPTUNA**. In addition, I used **SMOTE** to balance out the data, which helped plenty in the final model creation.

I also conducted an analysis of the data and did **hypothesis testing** to define the features, which differentiate the outcomes the most. Thanks to that I was able to reduce the number of features from 58 (excluding Mortality) to 14. I also did the **principal component analysis**, which suggested that I could use only 11 features to describe 95% of the data, but since the difference is not that significant between 11 and 14, I continued the modeling with 14 features.

Additionally, I created a simple app using **tkinter**, in which you can input your data and try the model yourself! 🌟


## Requirements

All the requirements can be found in the `requirements.txt` in the repository.

## Instalation
To run this project on you local machine, please follow the below steps:
1. **Creation of virtual environment** (recommended):
    Creation and activation of virtual environment:

    ```bash
    python -m venv nazwa_srodowiska
    source nazwa_srodowiska/bin/activate   # dla systemu Unix/Linux
    .\nazwa_srodowiska\Scripts\activate    # dla systemu Windows
    ```
2. **Instalation of requirements:**

    Install the needed versionf of the packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```
    Make sure you are using the latest version of pip:

    ```bash
    pip install --upgrade pip
    ```
    The `requirements.txt` contains the list of dependencies and it's versions.

3. **Running the project**:
    After the instalation of dependencies, you should be able to run the project.


## Usage
This project is created for education and entertaining purposes only. You can use it as a small suggestion on your cardiac health to look into if the predictions are not good.

## Repositoty structure
- **data** ➡️ this folder contains the dataset and two pickle files, with the model and the labels for data encoding;
- **Heart_Failure_EDA_Modeling.ipynb**  ➡️ this notebook contains the analysis, hypothesis testing, PCA, data cleaning and model creation;
- **heat_failure_app.py**  ➡️ application for easy usage of the model;

## Final model metrics

