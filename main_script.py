import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
from streamlit_calendar import calendar
import requests
import datetime

#API_URL = "https://unt.instructure.com/api/v1/"
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"
API_KEYM = "9082~PoqZCFiKGh0YegeAT4EBxzgUbdwuQcn8SIE1EAOTC07btruXEpbWQCNAmY8pdaz0"
API_EXT = '/api/v1/'

API_URL = ""
ACCESS_TOKEN = "" 

yesterday = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.min).strftime('%Y-%m-%d')
today = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.max).strftime('%Y-%m-%d')

st.set_page_config(
    page_title="OnTime",
    page_icon="ontime.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


def home_page():
    col1, mid, col2 = st.columns([1,1.62,20])
    with col1:
        st.image('img/ontime.png', width=108)
    with col2:
        st.title('Welcome to OnTime!')

#def logo():
    #image = Image.open("ontime.png")
    #st.image(image,width=50)

def classes_page():
    userJson = requests.get("https://unt.instructure.com/api/v1/users/self?access_token="+ACCESS_TOKEN).json()
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
            assignments = requests.get("https://unt.instructure.com/api/v1/calendar_events?access_token=" + ACCESS_TOKEN + "&type=assignment&context_codes%5B%5D=user_" + str(userJson["id"]) + "&context_codes%5B%5D=course_" + str(elem["id"]) + "&start_date=" + yesterday + "&end_date=" + today + "&per_page=50").json()
            for ass in assignments:
                st.write(ass["title"])

if __name__ == '__main__':

    selected_page = st.sidebar.selectbox(
        'Select Page',
        ('Home', 'Calendar', 'Classes')
    )

    if "API_URL" not in st.session_state:
        st.session_state["API_URL"] = ""

    if "ACCESS_TOKEN" not in st.session_state:
        st.session_state["ACCESS_TOKEN"] = ""

    API_URL = st.session_state["API_URL"]
    ACCESS_TOKEN = st.session_state["ACCESS_TOKEN"]

    if selected_page == 'Home':
        home_page()
        #logo()
    elif selected_page == 'Classes':
        classes_page()
