# -*- coding: utf-8 -*-
"""
Created on Sun July 26 2020

@author: Zhaopu Teng
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def nominal_1(data):
    new_data = []
    for d in data:
        if d == 'Yes':
            temp = 1
        else:
            temp = 0
        new_data.append(temp)
    return new_data

def preprocess_data(discretize_num, ):
    df = pd.read_csv('data_brain10-16.csv')

    # preprocess data

    survival_month = df['Survival months'].values


    survival_month_normalize = []
    if discretize_num == 2:
        for m in survival_month:
            temp = ''
            if m <= 18:
                temp = 0
            else:
                temp = 18
            survival_month_normalize.append(temp)
    if discretize_num == 3:
        for m in survival_month:
            temp = ''
            if m <= 6:
                temp = 0
            elif 6 < m <= 18:
                temp = 6
            else:
                temp = 18
            survival_month_normalize.append(temp)


    y = np.array(survival_month_normalize).reshape(-1, 1).ravel()
    # print(np.unique(survival_month_normalize, return_counts=True))

    age_at_diagnosis = df['Age at diagnosis'].values  # numeric
    sex = df['Sex'].values  # nominal
    year_of_diagnosis = df['Year of diagnosis'].values
    primary_site = df['Primary Site - labeled'].values  # nominal
    laterality = df['Laterality'].values  # nominal
    radiation = df['Radiation recode'].values  # nominal
    chemotherapy = df['Chemotherapy recode (yes, no/unk)'].values  # nominal
    tumor_size = df['CS tumor size (2004-2015)'].values  # nominal
    sequence_number = df['Sequence number'].values  # nominal
    first_galignant = df['First malignant primary indicator'].values  # nominal
    bone = df['SEER Combined Mets at DX-bone (2010+)'].values  # nominal
    brain = df['SEER Combined Mets at DX-brain (2010+)'].values  # nominal
    liver = df['SEER Combined Mets at DX-liver (2010+)'].values  # nominal
    lung = df['SEER Combined Mets at DX-lung (2010+)'].values  # nominal
    bone = np.array(nominal_1(bone))
    brain = np.array(nominal_1(brain))
    liver = np.array(nominal_1(liver))
    lung = np.array(nominal_1(lung))

    tumor_size_normalize = []
    for s in tumor_size:
        temp = 0
        if s < 10:
            temp = 10
        elif s < 20 and s >= 10:
            temp = 20
        elif s < 30 and s >= 20:
            temp = 30
        elif s < 40 and s >= 30:
            temp = 40
        elif s < 50 and s >= 40:
            temp = 50
        elif s < 60 and s >= 50:
            temp = 60
        elif s < 70 and s >= 60:
            temp = 70
        elif s < 80 and s >= 70:
            temp = 80
        elif s < 90 and s >= 80:
            temp = 90
        elif s < 100 and s >= 90:
            temp = 100
        elif s < 150 and s >= 100:
            temp = 150
        elif s < 300 and s >= 150:
            temp = 300
        elif s < 500 and s >= 300:
            temp = 500
        elif s < 800 and s >= 500:
            temp = 800
        elif s == 990:
            temp = 0
        elif s == 991:
            temp = 10
        elif s == 992:
            temp = 20
        elif s == 993:
            temp = 30
        elif s == 994:
            temp = 40
        elif s == 995:
            temp = 50
        elif s == 994:
            temp = 40
        elif s == 999 or s == 'Blanc(s)':
            temp = 'unknown'
        else:
            temp = 1000
        tumor_size_normalize.append(temp)
    tumor_size_normalize = np.array(tumor_size_normalize)

    x = np.hstack((tumor_size_normalize.reshape(-1, 1), age_at_diagnosis.reshape(-1, 1), sex.reshape(-1, 1),
                   year_of_diagnosis.reshape(-1, 1),
                   primary_site.reshape(-1, 1), laterality.reshape(-1, 1), radiation.reshape(-1, 1),
                   chemotherapy.reshape(-1, 1),
                   sequence_number.reshape(-1, 1), first_galignant.reshape(-1, 1), bone.reshape(-1, 1),
                   brain.reshape(-1, 1),
                   liver.reshape(-1, 1), lung.reshape(-1, 1)))

    enc = preprocessing.OrdinalEncoder()
    enc.fit(x)
    x = enc.transform(x)
    scaler = preprocessing.StandardScaler()
    scaler.fit(x)
    x = scaler.transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5, random_state=0)
    return x_train, x_test, y_train, y_test