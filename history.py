import streamlit as st
import pandas as pd


# st.set_page_config(
#     page_title='History',
#     page_icon='⏳',
#     layout='wide'
# )

def main():
    st.title('History Page')
    st.write('This is where you can view past predictions.')
    
    # Load data
    
    @st.cache_data(persist=True)
    
    def load_data():
        
        data = pd.read_csv ('data\history.csv')
        
        return data
    
    st.dataframe(load_data())
