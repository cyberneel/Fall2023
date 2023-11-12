import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
from streamlit_calendar import calendar
import requests
from streamlit_option_menu import option_menu
import datetime
import json
import random
from streamlit_extras.switch_page_button import switch_page

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
        st.error("GO TO SETTINGS AND ENTER INFO!")
        if st.button("Go to SETTINGS"):
            switch_page("settings")
        st.stop()
    #st.write(response.json()[0]["name"])
    #for elem in response.json():
        #st.write(elem["name"])
    calendar_main()

def calendar_main():

    yesterday = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=-45)), datetime.time.min).strftime('%Y-%m-%d')
    today = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=45)), datetime.time.max).strftime('%Y-%m-%d')
    userJson = requests.get("https://" + API_URL + API_EXT + "users/self?access_token="+ACCESS_TOKEN).json()

    cal = requests.get("https://"+API_URL+API_EXT+"courses?access_token="+ACCESS_TOKEN).json()
    taskslist = []
    chars = '0123456789ABCDEF'
    colors = ['#E85865', '#434B7F', '#D3B244', '#40A762', '#63D229', '#2586CB', '#0BB428', '#F69C2A', '#6FCEC2', '#F76E13', '#73DEAE', '#5CFF67', '#BD961E', '#ADA3DC', '#58B4E0', '#DE835D', '#3B3995', '#E29A63', '#E78C8B', '#C1039A']
    colorCnt = 0
    for c in cal:

        res = requests.get("https://"+API_URL+API_EXT+"calendar_events?access_token=" + ACCESS_TOKEN + "&type=assignment&context_codes%5B%5D=user_" + str(userJson["id"]) + "&context_codes%5B%5D=course_" + str(c["id"]) + "&start_date=" + yesterday + "&end_date=" + today + "&per_page=50").json()
        for r in res:
            tasks = {}
            tasks["title"] = r["title"]
            #st.write(r['start_at']+"   "+r['end_at'])
            tasks["start"] = r['start_at']#(datetime.datetime.strptime(r["start_at"],"%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=-6)).strftime("%Y-%m-%dT%H:%M:%SZ")
            tasks["end"] = (datetime.datetime.strptime(r["start_at"],"%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(days=-1)).strftime("%Y-%m-%dT%H:%M:%SZ")
            tasks["color"] = colors[colorCnt]
            taskslist.append(tasks)
            #t.write(tasks)
        colorCnt = colorCnt + 1


    calData = json.dumps(taskslist)

    calendar_options = {
        'timeZone': 'local',
        'initialView': 'dayGridMonth',
        'dayMaxEvents': 3,
        'dayPopeverFormat': {'month': 'long', 'day': 'nemeric', 'year': 'numeric'},
        'editable': 'true',
        'selectable': 'true',
        'fullDay': 'false',
        'nextDayThreshold': '11:11',
    }
    

    calendars = calendar(events=taskslist, options=calendar_options)
    #st.write(calendars)

def title_logo():
    col1, mid, col2 = st.columns([1,1.62,20])
    with col1:
        st.image('img/ontime.png', width=108)
    with mid:
        st.write("    ")
    with col2:
        st.title('Welcome to OnTime!')

if __name__ == '__main__':

    st.set_page_config(
        page_title="OnTime",
        page_icon="img/ontimefav.png",
        layout="wide",
        initial_sidebar_state="expanded"
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
        st.error("GO TO SETTINGS AND ENTER INFO!")
        if st.button("Go to SETTINGS"):
            switch_page("settings")
        st.stop()

    #selected_page = st.sidebar.selectbox(
     #   'Select Page',
    #    ('Home', 'Calendar', 'Settings')
    #)
    home_page()
