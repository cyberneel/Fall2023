import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
from streamlit_calendar import calendar
import requests
import datetime
from io import BytesIO
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


API_URL = "https://unt.instructure.com"
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"
API_KEYM = "9082~PoqZCFiKGh0YegeAT4EBxzgUbdwuQcn8SIE1EAOTC07btruXEpbWQCNAmY8pdaz0"

yesterday = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.min).strftime('%Y-%m-%d')
today = datetime.datetime.combine((datetime.datetime.today() + datetime.timedelta(days=0)), datetime.time.max).strftime('%Y-%m-%d')

API_EXT = "/api/v1/"

def classes_page():

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

    userJson = requests.get("https://"+API_URL+API_EXT + "users/self?access_token="+ACCESS_TOKEN).json()
    st.title("Your Classes:")
    dat = {'include[]': 'total_students'}
    response = requests.get("https://"+API_URL+API_EXT+"courses?access_token="+ACCESS_TOKEN, data=dat)
    #st.write(response.json()[0]["name"])
    if not response.ok:
        st.error("GO TO SETTINGS AND ENTER INFO!")
        st.stop()
    #st.write(response.json())
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    counting = 0
    for elem in response.json():
        #st.write(elem)
        if False:
            img = elem["image_download_url"]
            st.write(img)
            #r = requests.get(img)
            imggg = Image.open(img)
            st.image(imggg, output_format="auto")

            #st.image(BytesIO(r.content))
        with cols[counting]:
            with st.expander(elem["name"]):
                if("original_name" in elem):
                    st.write("Original Name: " + elem["original_name"])

                else:
                    st.write("Original Name: " + elem["name"])

                st.write("Course Code: " + elem["course_code"])
                if 'total_students' in elem:
                    st.write("Total Students Enrolled: " + str(elem["total_students"]))
                counting = counting + 1
                counting = counting % 3
                #st.image(img)

                #calEvents = requests.get("https://"+API_URL+API_EXT+"calendar_events?type=assignment&access_token="+ACCESS_TOKEN+"&context_codes%5B%5D=course_" + str(elem["id"]))
                #calEvents = requests.get("https://"+API_URL+API_EXT+"calendar_events?type=assignment" + "&context_codes%5B%5D=course_" + str(elem["id"]), {"Authorization": f"bearer {ACCESS_TOKEN}"})
                #st.write(calEvents.json())
                #st.write("Assignments Due TODAY:" + today)
                #assignments = requests.get("https://"+API_URL+API_EXT+"calendar_events?access_token=" + ACCESS_TOKEN + "&type=assignment&context_codes%5B%5D=user_" + str(userJson["id"]) + "&context_codes%5B%5D=course_" + str(elem["id"]) + "&start_date=" + yesterday + "&end_date=" + today + "&per_page=50").json()
                #for ass in assignments:
                #    st.write(ass["title"])

classes_page()