# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:01:24 2026

@author: Lab
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

Riding_model = pickle.load(open("C:/Users/Lab/Desktop/ML/Riding_model.sav",'rb'))
loan_model = pickle.load(open("C:/Users/Lab/Desktop/ML/loan_model.sav",'rb'))

with st.sidebar:
    selected = option_menu(
        'Classification',['Loan','Riding']
        )
    gender_map = {
       'Male':1,
       'Female':0,
       }
    education_map = {
        'High School': 0,
        'Associate': 1,
        'Bachelor': 2,
        'Master': 3,
        'Doctorate': 4
    }
    experience_map = {
        'Entry': 0,
        'Mid': 1,
        'Senior': 2,
        'Executive': 3
    }
    role_map = {
        'Business Analyst': 0,
        'Data Scientist': 1,
        'Data Analyst': 2,
        'Machine Learning Engineer': 3,
        'Software Engineer': 4,
        'Manager': 5
    }
    status_map = {
        'No': 0,
        'Yes': 1
    }
    
if(selected == 'Loan'):
    st.title('loan Classification')
    person_age = st.text_input('person_age')
    person_gender = st.selectbox('person_gender', gender_map)
    person_education = st.selectbox('person_education', education_map)
    person_income = st.text_input('person_income')
    person_emp_exp = st.text_input('person_emp_exp')
    person_home_ownership = st.selectbox('person_home_ownership', experience_map)
    loan_amnt = st.text_input('loan_amnt')
    loan_intent = st.selectbox('loan_intent', role_map)
    loan_int_rate = st.text_input('loan_int_rate')
    loan_percent_income = st.text_input('loan_percent_income')
    cb_person_cred_hist_length = st.text_input('cb_person_cred_hist_length')
    credit_score = st.text_input('credit_score')
    previous_loan_defaults_on_file = st.selectbox(
        'previous_loan_defaults_on_file',
        status_map
    )
 
 
    loan_prediction = ''
    if st.button('Predict'):
        loan_prediction = loan_model.predict([
        [
            float(person_age),
 
            gender_map[person_gender],
 
            education_map[person_education],
 
            float(person_income),
 
            float(person_emp_exp),
 
            experience_map[person_home_ownership],
 
            float(loan_amnt),
 
            role_map[loan_intent],
 
            float(loan_int_rate),
 
            float(loan_percent_income),
 
            float(cb_person_cred_hist_length),
 
            float(credit_score),
 
            status_map[previous_loan_defaults_on_file]
        ]])
        if(loan_prediction[0] == 0):
            loan_prediction = 'Non-Owner'
        else:
            loan_prediction = 'Owner'
    st.success(loan_prediction)
    
if(selected == 'Riding'):
    st.title('Riding Mower Classification')
    income = st.text_input('รายได้')
    Lotsize = st.text_input('พื้นที่บ้าน')
    Riding_prediction = ''

    if st.button('Predict'):
        Riding_prediction = Riding_model.predict([
        [float(income),float(Lotsize)]
         ])
        if(Riding_prediction[0] == 0):
            Riding_prediction = 'Non-Owner'
        else:
            Riding_prediction = 'Owner'
    st.success(Riding_prediction)