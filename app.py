import streamlit as st

st.set_page_config(page_title= f"More about me...",page_icon="🧑‍🚀",layout="wide")
st.markdown(f"<h1 style='text-align: center; color: white;'>Russell Whealdon Data Portfolio</h1>", unsafe_allow_html=True)

#Set background image for page
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://source.unsplash.com/blue-sky-and-white-clouds-b8dA3eY5VrY");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Page navigation
st.sidebar.markdown(f"<h4 style='text-align: center; color: white;'>Navigation</h4>", unsafe_allow_html=True)
url_home = "https://russellwhealdonportfolio.streamlit.app/"
url_resume = "https://russellwhealdonportfolio-resume.streamlit.app/"
url_hobbies = "https://russellwhealdonportfolio-hobbies.streamlit.app/"
st.sidebar.markdown(f"<h4><a href='{url_home}' target='_blank'>Home</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown(f"<h4><a href='{url_resume}' target='_blank'>Resume</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown(f"<h4><a href='{url_hobbies}' target='_blank'>Hobbies</a></h4>", unsafe_allow_html=True)

### Set sidebar background ###
sidebar_bg_img = """
<style>
[data-testid="stSidebar"] {
    background-image: url("https://source.unsplash.com/blue-sky-and-white-clouds-b8dA3eY5VrY");
    background-size: cover;
}
</style>
"""

# Inject CSS with Markdown
st.markdown(sidebar_bg_img, unsafe_allow_html=True)

st.markdown(f"<p style='text-align: center; color: white;'>Hi! I'm Russell Whealdon</p>", unsafe_allow_html=True)
