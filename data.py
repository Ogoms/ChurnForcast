import streamlit as st

import pandas as pd

# st.set_page_config(
#     page_title='Data',
#     page_icon='📊',
#     layout='wide'
# )

def show_data_page():
    st.title('Data Page')

# Load data

    @st.cache_data(persist=True)

    def load_data():

      data = pd.read_csv ('data\output.csv')
      return data

    st.dataframe(load_data())

