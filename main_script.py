import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
from streamlit_calendar import calendar
from canvasapi import Canvas
import requests

API_URL = "https://unt.instructure.com/api/v1/"
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"
API_KEYM = "9082~PoqZCFiKGh0YegeAT4EBxzgUbdwuQcn8SIE1EAOTC07btruXEpbWQCNAmY8pdaz0"

#apiTest = Canvas(API_URL, API_KEY)

#course = apiTest.get_course(90487)
#st.write(course.name)

st.set_page_config(
    page_title="OnTime",
    layout="wide",
    initial_sidebar_state="expanded",
)

def home_page():
    st.title('Welcome to OnTime!')
    response = requests.get(API_URL+"courses?access_token="+API_KEY)
    #st.write(response.json()[0]["name"])
    for elem in response.json():
        st.write(elem["name"])

if __name__ == '__main__':

    selected_page = st.sidebar.selectbox(
        'Select Page',
        ('Home', 'Calendar', 'Settings')
    )

    if selected_page == 'Home':
        home_page()
