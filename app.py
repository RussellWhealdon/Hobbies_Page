import streamlit as st

st.set_page_config(page_title= f"More about me...",page_icon="🧑‍🚀")
st.markdown(f"<h1 style='text-align: center; color: white;'>More about me...</h1>", unsafe_allow_html=True)

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

st.markdown(f"<p style='text-align: left; color: white;'>    Outside my professional work as a Data professional. I love to stay active and engage with the great city of New York. Some of my favorite activies include playing basketball and recently pickleball in the park. I'm also part of the North Brooklyn Chess club where I play weekly as well as in some competive tournaments from time to time. I love to problem solve and Chess is a great way to scratch that urge for me! Recently I have started volunteer coaching youth basketball clinics through the VOLO foundation. I am hoping to start coaching my own team soon!</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<h3 style='text-align: center ; color: white;'>Basketball</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>    I was lucky enough to play basketball my freshman year at Occidental College before transferring to Gonzaga University to finish my studies. I love engaging with the incredible basketball culture in New York City. It has been a great way to stay active as well as make connections in a new city! I play in a very competitive league here which you can see in the pic to the right. (The headband helps me focus)</p>", unsafe_allow_html=True)

with col2:
    st.image("Basketball_Photo.jpg")


col3, col4 = st.columns(2)

with col3:
    st.markdown(f"<h3 style='text-align: center ; color: white;'>Basketball</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: white;'>Chess is another passion of mine. I played competitivley when I was younger and have recently picked it back up more casually but will play in tournaments as the club hosts them. The analytical aspact of the game is something I love and interact with the same way I approach problems in my career. Here you can see my playing in Washington Square Park!</p>", unsafe_allow_html=True)

with col4:
    st.image("Chess_Photo_RW.png")

    
