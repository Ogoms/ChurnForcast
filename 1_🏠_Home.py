import streamlit as st
from PIL import Image

# Set the page configuration
im = Image.open('churn_predictor.ico.png')

try:
    st.set_page_config(
        page_title='Customer Churn Prediction App',
        page_icon=im,
        layout='wide'
    )
except FileNotFoundError:
    st.error("Icon file not found. Please check the file path.")

# Page Image
st.image("churn_predictor..png", width=900)

# Page description
st.title('Customer Churn Predictor')
st.write('Customer Churn Predictor is a model that predicts the likelihood of a customer leaving the organization')

# Key Features 
st.subheader ('*Key Features*')
st.markdown("""
- **DataPage** : Access the data.
- **DashBoard**: Explore interactive data visualization for insights.
- **Predition**: See customer churn prediction instantly.
- **History**: See past predictions made.  

""")

# how to run the application
st.subheader ('*How to run the application*')
st.markdown('''

To activate your virtual environment, use the following command:

```bash
venv\\Scripts\\activate
streamlit run 1_🏠_HomePage.py
''')

# Need help
st.subheader('*Need help?*')
st.markdown('''
For collaborations, contact me at ogoegbulemaugstina@gmail.com
''')

# link to the GitHub repository

github_repo_url = "https://github.com/Ogoms/ChurnPredictor"

if st.button("Repository on GitHub", key="github_button"):
    st.markdown(f'<a href="{github_repo_url}" target="_blank" style="text-decoration: none;"><div style="background-color: white; color: red; padding: 10px; border-radius: 5px; text-align: center;">Repository on GitHub</div></a>', unsafe_allow_html=True)

