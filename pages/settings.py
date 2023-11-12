import streamlit as st

API_URL = 'unt.instructure.com'
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"
API_KEYM = "9082~PoqZCFiKGh0YegeAT4EBxzgUbdwuQcn8SIE1EAOTC07btruXEpbWQCNAmY8pdaz0"

ACCESS_TOKEN = 'find this in profile settings'
API_URL = st.session_state["API_URL"]
st.session_state["API_URL"] = st.text_input('Please enter your organization\'s Canvas Instructure URL: ', st.session_state["API_URL"])
st.session_state["ACCESS_TOKEN"] = st.text_input('Please enter your Access Token: ', st.session_state["ACCESS_TOKEN"])