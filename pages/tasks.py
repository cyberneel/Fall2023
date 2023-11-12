import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
import requests
from streamlit_option_menu import option_menu
import datetime

API_URL = "https://unt.instructure.com"
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"
API_KEYM = "9082~PoqZCFiKGh0YegeAT4EBxzgUbdwuQcn8SIE1EAOTC07btruXEpbWQCNAmY8pdaz0"

API_EXT = "/api/v1/"

yesterday = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.min).strftime('%Y-%m-%d')
today = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.max).strftime('%Y-%m-%d')

def task_page(API_URL, ACCESS_TOKEN):
    userJson = requests.get("https://" + API_URL + API_EXT + "users/self?access_token="+ACCESS_TOKEN).json()
    st.title("Task Dashboard")
    st.divider() 
    selected2 = option_menu(None, ["Due today", "Next 7 days", "Next 30 Days"],
    default_index = 0, orientation = "horizontal",
    styles = {
        "nav-link": {"--hover-color": "#75340e"}
    })
    
    #selected2   
    st.write("Assignments Due TODAY:" + today)
    response = requests.get("https://"+API_URL+API_EXT+"courses?access_token="+ACCESS_TOKEN)
    for elem in response.json():
        assignments = requests.get("https://"+API_URL+API_EXT+"calendar_events?access_token=" + ACCESS_TOKEN + "&type=assignment&context_codes%5B%5D=user_" + str(userJson["id"]) + "&context_codes%5B%5D=course_" + str(elem["id"]) + "&start_date=" + yesterday + "&end_date=" + today + "&per_page=50").json()
        for ass in assignments:
            st.write(ass["title"])