import streamlit as st
from send_email import send_email

st.header("Contact me!")

with st.form(key="email_form"):
    user_email = st.text_input(label="Enter your email:")
    raw_message = st.text_area(label="Enter your message:", height=350)
    user_message = (f"Subject: New email from {user_email}\n"
                    f"\nFrom: {user_email}\n"
                    f"\n{raw_message}")
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_message)
        st.info("Your email was sent successfully")