import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
from streamlit_calendar import calendar
import requests
from streamlit_option_menu import option_menu
import datetime

API_URL = "unt.instructure.com"
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"
API_KEYM = "9082~PoqZCFiKGh0YegeAT4EBxzgUbdwuQcn8SIE1EAOTC07btruXEpbWQCNAmY8pdaz0"

st.set_page_config(
    page_title="OnTime",
    layout="wide",
    initial_sidebar_state="expanded",
)

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

API_EXT = '/api/v1/'

yesterday = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.min).strftime('%Y-%m-%d')
today = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.max).strftime('%Y-%m-%d')

def settings_page():
    st.session_state["API_URL"] = st.text_input('Please enter your organization\'s Canvas Instructure URL: ', st.session_state["API_URL"])
    st.session_state["ACCESS_TOKEN"] = st.text_input('Please enter your Access Token: ', st.session_state["ACCESS_TOKEN"])
def home_page():
    st.title('Welcome to OnTime!')
    response = requests.get("https://"+API_URL+API_EXT+"courses?access_token="+ACCESS_TOKEN)
    #st.write(response.json()[0]["name"])
    for elem in response.json():
        st.write(elem["name"])
def task_page():
    st.title("Project Dashboard")
    st.divider() 
def classes_page():
    userJson = requests.get("https://"+API_URL+API_EXT + "users/self?access_token="+ACCESS_TOKEN).json()
    st.title("Your Classes:")
    response = requests.get("https://"+API_URL+API_EXT+"courses?access_token="+ACCESS_TOKEN)
    #st.write(response.json()[0]["name"])
    for elem in response.json():
        with st.expander(elem["name"]):
            if("original_name" in elem):
                st.write("Original Name: " + elem["original_name"])

            else:
                st.write("Original Name: " + elem["name"])

            st.write("Course Code: " + elem["course_code"])

            #calEvents = requests.get("https://"+API_URL+API_EXT+"calendar_events?type=assignment&access_token="+ACCESS_TOKEN+"&context_codes%5B%5D=course_" + str(elem["id"]))
            #calEvents = requests.get("https://"+API_URL+API_EXT+"calendar_events?type=assignment" + "&context_codes%5B%5D=course_" + str(elem["id"]), {"Authorization": f"bearer {ACCESS_TOKEN}"})
            #st.write(calEvents.json())
            st.write("Assignments Due TODAY:" + today)
            assignments = requests.get("https://"+API_URL+API_EXT+"calendar_events?access_token=" + ACCESS_TOKEN + "&type=assignment&context_codes%5B%5D=user_" + str(userJson["id"]) + "&context_codes%5B%5D=course_" + str(elem["id"]) + "&start_date=" + yesterday + "&end_date=" + today + "&per_page=50").json()
            for ass in assignments:
                st.write(ass["title"])
if __name__ == '__main__':

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
    #selected_page = st.sidebar.selectbox(
     #   'Select Page',
    #    ('Home', 'Calendar', 'Settings')
    #)
    if "API_URL" not in st.session_state:
        st.session_state["API_URL"] = ""

    if "ACCESS_TOKEN" not in st.session_state:
        st.session_state["ACCESS_TOKEN"] = ""

    API_URL = st.session_state["API_URL"]
    ACCESS_TOKEN = st.session_state["ACCESS_TOKEN"]

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
