import streamlit as st

def settings_page():
    API_URL = 'unt.instructure.com'
    ACCESS_TOKEN = 'find this in profile settings'

    st.session_state["API_URL"] = st.text_input('Please enter your organization\'s Canvas Instructure URL: ', API_URL)
    st.session_state["ACCESS_TOKEN"] = st.text_input('Please enter your Access Token: ', ACCESS_TOKEN)

    API_URL = st.session_state["API_URL"]
    ACCESS_TOKEN = st.session_state["ACCESS_TOKEN"]

settings_page()