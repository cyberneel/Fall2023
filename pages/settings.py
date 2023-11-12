import streamlit as st

def settings_page():

    API_URL = st.text_input('Please enter your organization\'s Canvas Instructure URL: ')
    ACCESS_TOKEN = st.text_input('Please enter your Access Token: ')

    if st.button('SAVE'):
        st.session_state["API_URL"]  = API_URL
        st.session_state["ACCESS_TOKEN"] = ACCESS_TOKEN