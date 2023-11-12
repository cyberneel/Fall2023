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

def task_page():

    

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

    userJson = requests.get("https://" + API_URL + API_EXT + "users/self?access_token="+ACCESS_TOKEN).json()
    st.title("Task Dashboard")
    st.divider() 
    selected2 = option_menu(None, ["Due today", "Next 7 days", "Next 30 Days"],
    default_index = 0, orientation = "horizontal",
    styles = {
        "nav-link": {"--hover-color": "#75340e"}
    })

    dayso = 0

    if selected2 == "Next 7 days":
        dayso = 7
    elif selected2 == "Next 30 Days":
        dayso = 30

    yesterday = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.min).strftime('%Y-%m-%d')
    today = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=dayso)), datetime.time.max).strftime('%Y-%m-%d')
       
    #st.write("Assignments Due TODAY:" + today)
    response = requests.get("https://"+API_URL+API_EXT+"courses?access_token="+ACCESS_TOKEN)
    
    for elem in response.json():
        assignments = requests.get("https://"+API_URL+API_EXT+"calendar_events?access_token=" + ACCESS_TOKEN + "&type=assignment&context_codes%5B%5D=user_" + str(userJson["id"]) + "&context_codes%5B%5D=course_" + str(elem["id"]) + "&start_date=" + yesterday + "&end_date=" + today + "&per_page=50").json()
        drop = st.expander(rf"""{elem["name"]}""")
        if len(assignments) > 0:
            with drop:
                st.write("\n")
                count = len(assignments)
                cnt = 1
                for ass in assignments:
                    st.write(rf"""**{str(cnt)+". "+ass["title"]}**""")
                    cnt = cnt + 1

st.set_page_config(
        page_title="OnTime",
        page_icon="img/ontimefav.png",
        layout="wide",
        initial_sidebar_state="expanded"
    )

task_page()