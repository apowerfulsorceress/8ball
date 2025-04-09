import streamlit as st
import random
import requests
from datetime import datetime


if st.button("Consult the Oracle"):
    if name and question:
        st.write("The incense swirls... the shadows gather...")
        answer = random.choice(responses)
        st.success(f"{name}, the Oracle reveals: *{answer}*")

        # 💌 Send to Google Form
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdEYgJt63t5-xrMBWNASkWKYoZ1UzXwakZX_zyMIe7oD12vbw/formResponse"
        form_data = {
            "entry.1171538699": name,
            "entry.1310975289": question,
            "entry.1930830611": answer
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(form_url, data=form_data, headers=headers)

        if response.status_code != 200:
            st.warning("Something went wrong sending to the Oracle Log.")
    else:
        st.warning("You must offer both your name and a question.")
