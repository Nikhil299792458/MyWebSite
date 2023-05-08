#______________________Import Libraries_____________________________________#
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px

#______________________Set Page Config______________________________________#
st.set_page_config(page_title="Streamlit App", page_icon=":fire:",layout="wide")




def SideBar():


    st.markdown(
        """
    <style>
    span[data-baseweb="tag"] {
    background-color: blue !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


    # Create a container for the sidebar
    menu = st.sidebar.container()
    st.sidebar.title('Contents')


    # Add a menu item to the container
    with menu:
        st.sidebar.header('Main Menu')
        selection = st.sidebar.radio('Select an option', ['Option 1', 'Option 2'])
        
        # Create a submenu for Option 1
        if selection == 'Option 1':
            submenu = st.expander('Submenu')
            with submenu:
                st.write('This is a submenu for Option 1')
        
        # Create a submenu for Option 2
        elif selection == 'Option 2':
            submenu = st.expander('Submenu')
            with submenu:
                st.write('This is a submenu for Option 2')






def Hide_Streamlit_Logo():
    # Hide Streamlit Logo
    hide_streamlit_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                sidebar .sidebar-content {background-image: linear-gradient(#2e7bcf,#2e7bcf);}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.markdown("""
    <h1 style='text-align: center;'>
        My Streamlit App
    </h1>
    
    <p style='text-align: center;'>
        <a href='https://www.example.com'>Link 1</a> |
        <a href='https://www.example.com'>Link 2</a> |
        <a href='https://www.example.com'>Link 3</a>
    </p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

   

with st.expander('Click to expand'):
    st.write('This is some hidden content that can be expanded.')




SideBar()

Hide_Streamlit_Logo()