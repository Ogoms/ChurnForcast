import streamlit as st
from PIL import Image
import login  # Ensure this is renamed to a valid name
import dashboard
import predict
import history
import data

# Set the page configuration at the top of the script
im = Image.open('churn_predictor.ico.png')

# This must be the first Streamlit command
st.set_page_config(
    page_title='Customer Churn Prediction App',
    page_icon=im,
    layout='wide'
)

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Define a function to handle the login state
def check_authentication():
    return st.session_state.get('authenticated', False)

# Define a function to handle logout
def logout():
    st.session_state['authenticated'] = False
    st.session_state.pop('username', None)
    st.session_state['page'] = 'Login'

# Define the function to show the home page
def show_home_page():
    # Page Image
    st.image("churn_predictor.png", width=900)  # Ensure the image path is correct

    # Page description
    st.title('Customer Churn Predictor')
    st.write('Customer Churn Predictor is a model that predicts the likelihood of a customer leaving the organization')

    # Key Features 
    st.subheader('*Key Features*')
    st.markdown("""
    - **DataPage** : Access the data.
    - **DashBoard**: Explore interactive data visualization for insights.
    - **Prediction**: See customer churn prediction instantly.
    - **History**: See past predictions made.  
    """)

    # How to run the application
    st.subheader('*How to run the application*')
    st.markdown('''
    To activate your virtual environment, use the following command:
    ```bash
    venv\\Scripts\\activate
    streamlit run app.py
    ''')

    # Need help
    st.subheader('*Need help?*')
    st.markdown('''
    For collaborations, contact me at ogoegbulemaugstina@gmail.com
    ''')

    # Link to the GitHub repository
    github_repo_url = "https://github.com/Ogoms/ChurnPredictor"

    if st.button("Repository on GitHub", key="github_button"):
        st.markdown(f'<a href="{github_repo_url}" target="_blank" style="text-decoration: none;"><div style="background-color: white; color: red; padding: 10px; border-radius: 5px; text-align: center;">Repository on GitHub</div></a>', unsafe_allow_html=True)

# def main():
#     # Check if the user is authenticated
#     if not check_authentication():
#         login.show_login()  # Show the login form if not authenticated
#         return  # Exit the main function if not authenticated

#     # If authenticated, continue with the app logic
#     if 'page' not in st.session_state:
#         st.session_state['page'] = 'Home'

#     # Sidebar with login option
#     st.sidebar.title(f'Welcome, {st.session_state["username"]}')
#     if st.sidebar.button('Logout'):
#         logout()

def main():
    if not check_authentication():
        login.show_login()  # Show the login form if not authenticated
        return  # Exit the main function if not authenticated

    # If authenticated, show the navigation menu
    st.sidebar.title(f'Welcome, {st.session_state["username"]}')
    st.sidebar.button('Logout', on_click=logout)


    # Navigation menu
    st.sidebar.title('Navigation') 
    st.session_state['page'] = st.sidebar.selectbox('Select Page', ['Home', 'Dashboard', 'Prediction', 'History', 'Data']) 

    # Render the selected page
    if st.session_state['page'] == 'Home':
        show_home_page()  # Call the function to render the Home page

    elif st.session_state['page'] == 'Dashboard':
        dashboard.show_dashboard()  # Ensure this function is defined

    elif st.session_state['page'] == 'Data':
        data.show_data_page()  # Ensure this function is defined

    elif st.session_state['page'] == 'Prediction':
        predict.main()  # Ensure this function is defined

    elif st.session_state['page'] == 'History':
        history.main()  # Ensure this function is defined

if __name__ == "__main__":
    main()  # Call the main function to run the app
    