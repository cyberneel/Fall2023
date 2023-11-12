import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
from streamlit_calendar import calendar
import requests
from streamlit_option_menu import option_menu
import datetime
from pages.settings import settings_page
from pages.classes import classes_page
from pages.tasks import task_page

API_URL = "unt.instructure.com"
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"
API_KEYM = "9082~PoqZCFiKGh0YegeAT4EBxzgUbdwuQcn8SIE1EAOTC07btruXEpbWQCNAmY8pdaz0"

API_EXT = '/api/v1/'

yesterday = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.min).strftime('%Y-%m-%d')
today = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.max).strftime('%Y-%m-%d')


def home_page():
    title_logo()
    response = requests.get("https://"+API_URL+API_EXT+"courses?access_token="+ACCESS_TOKEN)
    if not response.ok:
        st.write("GO TO SETTINGS AND ENTER INFO!")
        st.stop()
    #st.write(response.json()[0]["name"])
    for elem in response.json():
        st.write(elem["name"])

def title_logo():
    col1, mid, col2 = st.columns([1,1.62,20])
    with col1:
        st.image('img/ontime.png', width=108)
    with col2:
        st.title('Welcome to OnTime!')

if __name__ == '__main__':

    st.set_page_config(
        page_title="OnTime",
        page_icon="img/ontimefav.png",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    with st.sidebar:
        selected = option_menu(None, ["Home","Calendar", "Settings", "Classes", "Tasks"],
        icons = ['house',  'calendar', 'gear', "book", "pencil"], default_index = 0,
        styles={"container": {"padding": "0!important", "background-color": "#120101"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#a6874b"},
        "nav-link-selected": {"background-color": "green"},
                }
                               )
        selected
    
    if "API_URL" not in st.session_state:
        API_URL = ""
    else:
        API_URL = st.session_state["API_URL"]
    if "ACCESS_TOKEN" not in st.session_state:
        ACCESS_TOKEN = ""
    else:
        ACCESS_TOKEN = st.session_state["ACCESS_TOKEN"]

    if API_URL == "" or ACCESS_TOKEN == "":
        st.write("GO TO SETTINGS AND ENTER INFO!")
        st.stop()

    #selected_page = st.sidebar.selectbox(
     #   'Select Page',
    #    ('Home', 'Calendar', 'Settings')
    #)
    

    if selected == 'Home':
        home_page()
    elif selected == 'Tasks':
        task_page()
    elif selected == 'Calendar':
        task_page()
    elif selected == 'Settings':
        settings_page()
    elif selected == 'Classes':
        classes_page()
