import streamlit as st
import random
import requests
from datetime import datetime

# 🌙 Title and intro
st.title("Witchy Oracle 8 Ball")
st.subheader("Summon the wisdom of the unseen...")

# ✨ User input
name = st.text_input("Your name, seeker of hidden truths:")
question = st.text_input("Ask your yes-or-no question:")

# 🌞 Light Oracle responses (hopeful, wise, whimsical)
light_responses = [
    "The stars align in your favor.",
    "The spirits whisper yes.",
    "Ask again when the moon is full.",
    "The cauldron bubbles with a yes.",
    "Yes—if you trust your intuition.",
    "Absolutely. Trust the signs.",
    "A message will come in a dream.",
    "Even the runes nod in approval.",
    "The energy feels promising.",
    "Yes—but be patient with the process."
]

# 🌑 Dark Oracle responses (sassy, ominous, shadowy)
dark_responses = [
    "You already know that. Why are you even asking?",
    "No. The answer has always been no.",
    "You will not like what happens if you ask again.",
    "The spirits laugh… not with you.",
    "Do you want the truth, or something pretty?",
    "The mirror shatters. Ask no more.",
    "Even the darkness recoils from that path.",
    "Do you *really* want me to say it out loud?",
    "You asked... you shouldn’t have.",
    "No. And next time, bring an offering.",
    "This is beneath you, and me.",
    "Try again when you’re not being so desperate.",
    "Don't waste the Oracle's breath on foolishness.",
    "Oh darling... absolutely not.",
    "You already made your choice. The rest is consequence."
]

# 🧙‍♀️ Oracle button + answer + Google Form log
if st.button("Consult the Oracle"):
    if name and question:
        st.write("The incense swirls... the shadows gather...")
        answer = random.choice(responses)
        st.success(f"{name}, the Oracle reveals: *{answer}*")

        # 💌 Send to Google Form (finally working 🖤)
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdEYgJt63t5-xrMBWNASkWKYoZ1UzXwakZX_zyMIe7oD12vbw/formResponse"
        form_data = {
            "entry.749958729": name,
            "entry.2088019051": question,
            "entry.340729774": answer
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(form_url, data=form_data, headers=headers)

        if response.status_code != 200:
            st.warning("Something went wrong sending to the Oracle Log.")
    else:
        st.warning("You must offer both your name and a question.")
