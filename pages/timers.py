import streamlit as st
import datetime
import time


#def stopwatch():

#def countdown():


st.title("Timer/Stopwatch")

result = st.selectbox('Please select a timer:', ('Stopwatch', 'Timer'))

st.write('Selected: ', result)

placeholder = st.empty()

timer = 0 

def update_stopwatch():
    global timer
    timer += 1
    with placeholder.container():
        st.write(timer)

def update_time():
    timer = datetime.datetime.now() 
    with placeholder.container():
        st.write(timer.strftime("%M"), ':', timer.strftime("%S"))

#while(True):
    #update_time()
    #time.sleep(1)
    #placeholder.empty()



if(result == 'Stopwatch'):
    col1, col2 = st.columns([0.3,3])
    with col1:
        if 'sta' not in st.session_state:
            st.session_state.sta = False
        strt = st.button('Start',disabled=st.session_state.sta)
    with col2:
        if 'sto' not in st.session_state:
            st.session_state.sto = True
        stop = st.button('Stop', disabled=st.session_state.sto)
    #with col3:
        #if 'lap' not in st.session_state:
            #st.session_state.lap = 0
        #lap = st.button('Lap')
    

    
    if(strt):
        st.session_state.sta = True
        st.session_state.sto = False
        while(True):
            update_stopwatch()
            time.sleep(1)
            placeholder.empty()
            if (stop):
                break
            
    if(stop):
        st.session_state.sta = False
        st.session_state.sto = True
    
    #if(lap):
        #st.session_state.lap += 1
        #st.write('Lap: ', timer)

    
#elif (result == "Timer")
    
