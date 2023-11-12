import streamlit as st

API_URL = 'unt.instructure.com'
ACCESS_TOKEN = 'find this in profile settings'

st.session_state["API_URL"] = st.text_input('Please enter your organization\'s Canvas Instructure URL: ', st.session_state["API_URL"])
st.session_state["ACCESS_TOKEN"] = st.text_input('Please enter your Access Token: ', st.session_state["ACCESS_TOKEN"])