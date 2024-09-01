import streamlit as st
import joblib
import pandas as pd
import os
from datetime import datetime
import imblearn
import app



# st.set_page_config(
#     page_title='Predict',
#     page_icon='📉',
#     layout='wide'
# )

# st.title ('Prediction Page')


def main():
    print("Main function called")
    st.title('Make a Prediction')
    print("Title displayed")

    # st.title('Make a Prediction')

    

    # Decorators
    @st.cache_resource(show_spinner='Models Loading')
    def load_randomforest_pipeline():
        pipeline = joblib.load('models\\rf_pipeline.joblib')
        return pipeline
    @st.cache_resource(show_spinner='Models Loading')
    def load_svc_pipeline():
        pipeline = joblib.load('models\\svc_pipeline.joblib')
        return pipeline
    def select_model():
        col1,col2 = st.columns(2)
        
        with col1:
            st.selectbox ('Select a Model', options=[ 'Random Forest', 'SVC'], key = 'selected_model')
            
            with col2:
                pass
            
            if st.session_state['selected_model'] =='Random Forest':
                pipeline = load_randomforest_pipeline()
            else:
                pipeline = load_svc_pipeline()
                
                encoder = joblib.load('models\label_encoder.joblib')
                
                return pipeline, encoder
            
            if 'prediction' not in st.session_state:
                st.session_state['prediction'] = None
                if 'probability' not in st.session_state:
                    st.session_state['probability'] = None
                    
                    def make_prediction (pipeline, encoder):
                        
                        Gender = st.session_state['Gender']
                        seniorcitizen = 1 if st.session_state['seniorcitizen'] == 'True' else 0
                        partner = 1 if st.session_state['partner'] == 'True' else 0
                        dependents = 1 if st.session_state['dependents'] == 'True' else 0
                        Tenure = st.session_state['Tenure']
                        monthlycharges = st.session_state['monthlycharges']
                        totalcharges = st.session_state['totalcharges']
                        contract = st.session_state['contract']
                        paymentmethod = st.session_state['paymentmethod']
                        paperlessbilling = 1 if st.session_state['paperlessbilling'] == 'True' else 0
                        multiplelines = st.session_state['multiplelines']
                        internetservice = st.session_state['internetservice']
                        onlinesecurity = st.session_state['onlinesecurity']
                        onlinebackup = st.session_state['onlinebackup']
                        deviceprotection = st.session_state['deviceprotection']
                        techsupport = st.session_state['techsupport']
                        streamingtv = st.session_state['streamingtv']
                        streamingmovies = st.session_state['streamingmovies']
                        phoneservice = 1 if st.session_state['phoneservice'] == 'True' else 0
                        
                        columns = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents',
        'tenure', 'MonthlyCharges', 'TotalCharges', 'Contract',
        'PaymentMethod', 'PaperlessBilling', 'MultipleLines',
        'InternetService', 'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport', 'StreamingTV',
        'StreamingMovies', 'PhoneService'
    ]
                        data = [[
        Gender, seniorcitizen, partner, dependents, Tenure, monthlycharges, 
        totalcharges, contract, paymentmethod, paperlessbilling, multiplelines, 
        internetservice, onlinesecurity, onlinebackup, deviceprotection, techsupport,
        streamingtv, streamingmovies, phoneservice
    ]]
                        
                       # Create a DataFrame 
                        df = pd.DataFrame(data, columns=columns)
                        
                        categorical_columns = ['gender', 'MultipleLines', 'InternetService', 
                       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                       'TechSupport', 'StreamingTV', 'StreamingMovies', 
                       'Contract', 'PaymentMethod']
                        
                        # Convert categorical columns to the appropriate type
                        for col in categorical_columns:
                            df[col] = df[col].astype(str)
                            
                            df['Prediction Time'] = datetime.now()  
                            
                            df['Model Used'] = st.session_state.get('selected_model', 'Unknown Model')  # Fallback in case it's not set
                            
# df['Prediction Time'] = datetime.datetoday()
    # df['Model Used'] = st.session_state['selected_model']
    
    # Save the DataFrame to a CSV file

                            csv_path = './data/history.csv'
                            mode = 'a' if os.path.exists(csv_path) else 'w'
                            header = not os.path.exists(csv_path)
                            df.to_csv(csv_path, mode=mode, header=header, index=False)
    # df.to_csv('./data/history.csv', mode = 'a', header=not os.path.exists('./data/history.csv'), index=False)
    
    # Make prediction
                            pred = pipeline.predict(df)
                            pred = int(pred[0])
                            prediction = encoder.inverse_transform([pred])

    # Get probabilities
                            probability = pipeline.predict_proba(df)


    # Updating state
                            st.session_state['prediction'] = prediction[0]
                            st.session_state['probability'] = probability
                            
                            return prediction, probability 
                        
                        
                        def display_form():
                            
                            pipeline, encoder = select_model ()
                            
                            with st.form ('input-feature'):
                                col1,col2,col3 = st.columns(3)
                                
                                with col1:
                                    
                                    st.write ('### Personal Information')
                                    st.selectbox ('Enter gender',[
                                                 'Female', 'Male' ], key = 'Gender')
                                    st.selectbox ('Senior Citizens', [
                                                 'False', 'True'], key = 'seniorcitizen')
                                    st.selectbox ('Partners',[
                                                 'False', 'True'], key = 'partner')
                                    st.selectbox ('Dependents', [
                                                 'False', 'True'], key = 'dependents')
                                
                                with col2:
                                    
                                    st.write ('### Account Information')
                                    st.number_input ('Enter Tenure', min_value = 0, 
                                                     max_value = 100, step = 1, key = 'Tenure')   
                                    st.number_input ('Monthly Charges', min_value =0.0,
                                                     max_value = 1e+12, value = 0.0, step = 0.1, key = 'monthlycharges' )
                                    st.number_input ('Total Charges', min_value =0.0,
                                                     max_value = 1e+12, value = 0.0, step = 0.1, key = 'totalcharges' )
                                    st.selectbox ('Contract Type', [
                                                 'Month to month', 'One year', 'Two year'], key = 'contract')
                                    st.selectbox ('Payment Method', [
                                                 'Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)' ], key = 'paymentmethod')
                                    st.selectbox ('Paperless Billing', [
                                                 'True', 'False'], key = 'paperlessbilling')
        
                                with col3:
                                    
                                    st.write ('### Service Information')
                                    st.selectbox ('Multiple Lines', [
                                                 'None','False','True'], key = 'multiplelines')
                                    st.selectbox ('Internet Service', [
                                                 'DSL','Fiber', 'optic', 'No'], key = 'internetservice')
                                    st.selectbox ('Online Security', [
                                                 'False', 'True' ,'None'], key = 'onlinesecurity')
                                    st.selectbox ('Online Backup', [
                                                 'True', 'False' ,'None'], key = 'onlinebackup')
                                    st.selectbox ('Device Protection', [
                                                 'False' ,'True' ,'None'], key = 'deviceprotection')
                                    st.selectbox ('Tech Support', [
                                                 'False' ,'True' ,'None'], key = 'techsupport')
                                    st.selectbox ('Streaming TV', [
                                                 'False' ,'True' ,'None'], key = 'streamingtv')
                                    st.selectbox ('Streaming Movies', [
                                                 'False' ,'True' ,'None'], key = 'streamingmovies')
                                    st.selectbox ('Phone Service', [
                                                 'False' ,'True' ], key = 'phoneservice')

        #                         st.form_submit_button('Make Prediction', on_click = make_prediction, kwargs=dict(
        # pipeline=pipeline, encoder=encoder))
                                
                                st.form_submit_button('Make Prediction', on_click=lambda: make_prediction(pipeline, encoder))



                                if __name__ == '__main__':
                                    print("Script executed directly")
                                    print("Title displayed from if block")
                                    st.title('Make a Prediction')
                                    print("Form displayed from if block")
                                    display_form()
                                    main()

                                    # st.title('Make a Prediction')
                                    # display_form()
                                    
                                    
                                    prediction = st.session_state['prediction']
                                    probability = st.session_state['probability']
                                    
                                    if not prediction:
                                        st.markdown('### Prediction will show here')
                                    elif prediction == 'Yes':
                                        probability_of_yes = probability [0][1] * 100
                                        st.markdown(f'### The customer will churn with a probability of {round(probability_of_yes, 2)}%')
                                    else:
                                        probability_of_no = probability[0][0] * 100
                                        st.markdown(f'### The customer will not churn with a probability of {round(probability_of_no, 2)}%')
    
                                    st.write(st.session_state)
                                    