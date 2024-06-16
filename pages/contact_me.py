import streamlit as st 
from email_automation import email_auto

st.header("Contact Me")
with st.form(key="contact"):
    email = st.text_input("Enter your email address")
    msg = st.text_area("Your message")
    completed_msg = f"""\
Subject: Email from {email}
{msg}
--This message was sent by {email}--
"""
    button = st.form_submit_button
    if button:
        email_auto(msg)