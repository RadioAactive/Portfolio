import streamlit as st

st.set_page_config(layout="wide")
col1 , col2 = st.columns(2)

with col1:
    st.image("images/pika is surprised.jpg", width=450)

with col2:
    st.title("About Me")
    content = """
Hello. This is Hashir aka RadioAactive. I am a student developer currently learning Python.
 My dream is to be an AI programmer so since right now Python is the demanding language for AI, 
 I will be studying it into detail. My goal is to learn other languages such as Julia in a span of 3 years. 
 I also have interest in web development so I will learn it bit by bit. Other useful languages such as javascript
 are also in my bucket list 

 Lastly I like pikachu :)
"""
    st.info(content)

st.write("Below you can find some of my apps have build in Python. You can also contact me (Check below for more details)")