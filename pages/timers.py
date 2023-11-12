import streamlit as st
import datetime
import time


#def stopwatch():

#def countdown():

def update_time():
    timer = datetime.datetime.now()
    st.write(timer.strftime("%M"), ':', timer.strftime("%S"))






st.title("Timer/Stopwatch")

result = st.selectbox('Please select a timer:', ('Stopwatch', 'Timer'))

st.write('Selected: ', result)

while(True):
    update_time()
    st.write("\u0008\u0008\u0008\u0008\u0008")
    time.sleep(2)

#if(result == "Stopwatch"):
    
#elif (result == "Timer")
    
