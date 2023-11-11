import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt


def home_page():
    st.title('Looking into Iris Dataset')

def dataset_page():
    st.title('Dataset')
    st.header('Statistics')

def graphs_page():
    st.title('Graphs')

    st.header('Seaborn (Matplotlib)')

    st.header('*Can also support Altair, Plotly, and Bokeh')

if __name__ == '__main__':

    selected_page = st.sidebar.selectbox(
        'Select Page',
        ('Home', 'Dataset', 'Graphs')
    )

    if selected_page == 'Home':
        home_page()
    elif selected_page == 'Dataset':
        dataset_page()
    else:
        graphs_page()