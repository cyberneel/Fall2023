import streamlit as st

API_URL = 'unt.instructure.com'
ACCESS_TOKEN = 'find this in profile settings'

API_URL = st.text_input('Please enter your organization\'s Canvas Instructure URL: ', API_URL)
ACCESS_TOKEN = st.text_input('Please enter your Access Token: ', ACCESS_TOKEN)