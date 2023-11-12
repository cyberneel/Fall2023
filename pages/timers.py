import streamlit as st
import datetime
import time


#def stopwatch():

#def countdown():


st.title("Timer/Stopwatch")

result = st.selectbox('Please select a timer:', ('Stopwatch', 'Timer'))

st.write('Selected: ', result)

placeholder = st.empty()

def update_time():
    timer = datetime.datetime.now() 
    with placeholder.container():
        st.write(timer.strftime("%M"), ':', timer.strftime("%S"))

while(True):
    update_time()
    time.sleep(1)
    placeholder.empty()


def update_time():
    timer = datetime.datetime.now() 
    with placeholder.container():
        st.write(timer.strftime("%M"), ':', timer.strftime("%S"))


#if(result == "Stopwatch"):
    
#elif (result == "Timer")
    
