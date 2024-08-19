import streamlit as st
import joblib
import pandas as pd
import os
import datetime



st.set_page_config(
    page_title='Predict',
    page_icon='📉',
    layout='wide'
)

st.title ('Prediction Page')

# Decorators
@st.cache_resource(show_spinner='Models Loading')
def load_randomforest_pipeline():
    pipeline = joblib.load('models\rf_pipeline.joblib')
    return pipeline

@st.cache_resource(show_spinner='Models Loading')
def load_svc_pipeline():
    pipeline = joblib.load('models\svc_pipeline.joblib')
    return pipeline

def select_model():
    col1,col2 = st.columns(2)

    with col1:
        st.selectbox ('Select a Model', options=[ 
        'Random Forest', 'SVC'], key = 'selected_model')

    with col2:
        pass

    if st.session_state['selected_model'] =='Random Forest':
        pipeline = load_randomforest_pipeline()

    else:
        pipeline = load_svc_pipeline()

    encoder = joblib.load('models\label_encoder.joblib')

    return pipeline, encoder



def display_form():

    pipeline, encoder = select_model ()

    with st.form ('input-feature'):
        col1,col2,col3 = st.columns(3)

        with col1:
            st.write ('### Personal Information')
            st.selectbox ('Enter gender',[
                         'Female', 'Male' ], key = 'gender')
            st.selectbox ('Senior Citizens', [
                         'False', 'True'], key = 'SeniorCitizen')
            st.selectbox ('Partners',[
                         'False', 'True'], key = 'Partner')
            st.selectbox ('Dependents', [
                         'False', 'True'], key = 'Dependents')

        with col2:
            st.write ('### Account Information')
            st.number_input ('Enter Tenure', min_value = 0, 
                             max_value = 100, step = 1, key = 'Tenure')   
            st.number_input ('Monthly Charges', min_value =0,
                             max_value = float('inf'), value = 0.0, step = 0.1, key = 'MonthlyCharges' )
            st.number_input ('Total Charges', min_value =0,
                             max_value = float('inf'), value = 0.0, step = 0.1, key = 'TotalCharges' )
            st.selectbox ('Contract Type', [
                         'Month to month', 'One year', 'Two year'], key = 'Contract')
            st.selectbox ('Payment Method', [
                         'Electronic check', 'Mailed check' 'Bank transfer (automatic)''Credit card (automatic)' ], key = 'PaymentMethod')
            st.selectbox ('Paperless Billing', [
                         'True', 'False'], key = 'PaperlessBilling')
        
        with col3:
            st.write ('### Service Information')
            st.selectbox ('Multiple Lines', [
                         'None' 'False' 'True'], key = 'MultipleLines')
            st.selectbox ('Internet Service', [
                         'DSL' 'Fiber optic' 'No'], key = 'InternetService')
            st.selectbox ('Online Security', [
                         'False' 'True' 'None'], key = 'OnlineSecurity')
            st.selectbox ('Online Backup', [
                         'True' 'False' 'None'], key = 'OnlineBackup')
            st.selectbox ('Device Protection', [
                         'False' 'True' 'None'], key = 'DeviceProtection')
            st.selectbox ('Tech Support', [
                         'False' 'True' 'None'], key = 'TechSupport')
            st.selectbox ('Streaming TV', [
                         'False' 'True' 'None'], key = 'StreamingTV')
            st.selectbox ('Streaming Movies', [
                         'False' 'True' 'None'], key = 'StreamingMovies')
            st.selectbox ('Phone Service', [
                         'False' 'True' ], key = 'PhoneService')

        st.form_submit_button('Make Prediction', on_click=make_prediction, kwargs=dict(
        pipeline=pipeline, encoder=encoder))




