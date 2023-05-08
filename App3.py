#______________________Import Libraries_____________________________________#
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
from PIL import Image
import base64

#______________________Set Page Config______________________________________#








def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             opacity: 1;
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover

         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack("Capture2.PNG")

def Hide_Streamlit_Logo():
    # Hide Streamlit Logo
    hide_streamlit_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {background-color:rgba(0,0,0,0);}
                sidebar .sidebar-content {background-image: linear-gradient(#2e7bcf,#2e7bcf);}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

Hide_Streamlit_Logo()   




html = """
<!DOCTYPE html>
<html>
    <head>
		<title>Parallax Scrolling Website | Vanilla Javascipt</title>
		<link rel="stylesheet" type="text/css" href="assets/styles.css">
	</head>
    <body>
        <header>
            <a href="#" class="logo">Nikhil Verma</a>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Work</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </header>
    </body>

</html>
"""



st.write(html, unsafe_allow_html=True)
st.write('<style>' + open('assets/styles.css').read() + '</style>', unsafe_allow_html=True)




# Set the page title color
page_title = f"""
<style>
    h1 {{
        color: blue;
    }}
</style>
"""
st.markdown(page_title, unsafe_allow_html=True)

# Add columns to the app
col1, col2 = st.columns(2)

with col1:
    st.title("")


with col2:
    page_title = f"""
    <style>
        h1 {{
            color: blue;
        }}
    </style>
    """
    st.markdown(page_title, unsafe_allow_html=True)

    # Add the title to the app with a new line
    st.title("Hello!")
    st.write("\n") # Add a new line
    st.title("I am Nikhil Verma")







# Set the page title color
page_title = f"""
<style>
    h1 {{
        color: black;
    }}
</style>
"""
st.markdown(page_title, unsafe_allow_html=True)




def SideBar():

    st.markdown(
        """
    <style>

    span[data-baseweb="tag"] {
    background-color: black !important;
    }

    [data-testid="stHeader"]{
    background-color: rgba(0, 0, 0, 0.0);
    }

    [data-testid="stSidebar"]{
    background-color: #000000;
    }

    [data-testid="stHeader"]{
    background-color: #000000;
    }

    </style>
    """,
        unsafe_allow_html=True,
    )


    # Create a container for the sidebar
    menu = st.sidebar.container()

    st.markdown(
        """
        <style>
        /* Sidebar styling */
        .css-1cypcdb {
            background-color: #000000;
            padding-top: 2rem;
            padding-bottom: 2rem;
            width: 20rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )








        # # Add a menu item to the container
        # with menu:
        #     # Add buttons with links to the sidebar

        #     st.sidebar.write("## Links")
        #     if st.sidebar.button("Google"):
        #         st.sidebar.markdown("[Google](https://www.google.com/)")
        #     if st.sidebar.button("Streamlit"):
        #         st.sidebar.markdown("[Streamlit](https://www.streamlit.io/)")
            
        #     selection = st.sidebar.radio('Select an option', ['Option 1', 'Option 2'])
            
        #     # Create a submenu for Option 1
        #     if selection == 'Option 1':
        #         submenu = st.expander('Submenu')
        #         with submenu:
        #             st.write('This is a submenu for Option 1')
            
        #     # Create a submenu for Option 2
        #     elif selection == 'Option 2':
        #         submenu = st.expander('Submenu')
        #         with submenu:
        #             st.write('This is a submenu for Option 2')


        # # Add link buttons with logos to the sidebar
    st.sidebar.markdown("<h2 style='font-size: 24px'>Contents</h2>", unsafe_allow_html=True)
        # # Import the image in base64 format




    def Encode_Image(image_file):
        with open(image_file, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        return encoded_image


    # Create the HTML code for the image
    Resume_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/Resume.png")}" height="25" title="Profile">'
    resume_icon = f"<a href='https://www.facebook.com/nikhil.verma.161'>{Resume_Icon}</a>"

    Blog_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/Blog.png")}" height="25" title="Blogs">'
    blog_icon = f"<a href='https://www.facebook.com/nikhil.verma.161'>{Blog_Icon}</a>"

    Facebook_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/Facebook.png")}" height="25" title="Facebook">'
    facebook_icon = f"<a href='https://www.facebook.com/nikhil.verma.161'>{Facebook_Icon}</a>"

    st.sidebar.markdown("<h2 style='font-size: 14px;'>"+ resume_icon   + "  Profile <br> "+ blog_icon+ "     Blogs <br>  "+"  </h2>", unsafe_allow_html=True)





    # Add link buttons with logos to the sidebar
    st.sidebar.markdown("<h2 style='text-align: center;font-size=24;'>Connect with me</h2>", unsafe_allow_html=True)
    # Import the image in base64 format




    def Contact_Icons():

        # Create the HTML code for the image
        Gmail_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/Gmail.png")}" height="30" title="Gmail">'
        Facebook_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/Facebook.png")}" height="30" title="Facebook">'
        LinkedIn_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/LinkedIn.png")}" height="30" title="LinkedIn">'
        Github_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/Github.png")}" height="30" title="Github">'
        Scholar_Icon = f'<img src="data:image/png;base64,{Encode_Image("Logo/Scholar.png")}" height="30" title="Google Scholar">'

        facebook_icon = f"<a href='https://www.facebook.com/nikhil.verma.161'>{Facebook_Icon}</a>"
        linkedin_icon = f"<a href='https://www.linkedin.com/in/nikhil-verma-28ab03148'>{LinkedIn_Icon}</a>"
        scholar_icon = f"<a href='https://scholar.google.com/citations?user=QF6b184AAAAJ&hl=en'>{Scholar_Icon}</a>"
        github_icon = f"<a href='https://github.com/Nikhil299792458'>{Github_Icon}</a>"
        gmail_icon = f"<a href='mailto:Nikhil299792458@gmail.com'>{Gmail_Icon}</a>"

        st.sidebar.markdown("<p style='text-align: center;'>" + facebook_icon + " " + linkedin_icon + " " + scholar_icon + " " + github_icon + " " + gmail_icon + "</p>", unsafe_allow_html=True)

    Contact_Icons()

st.write('<style>' + open('assets/styles.css').read() + '</style>', unsafe_allow_html=True)

SideBar()




