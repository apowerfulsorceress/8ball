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

# 🔮 Oracle responses
responses = [
    "The stars align in your favor.",
    "The spirits whisper yes.",
    "Ask again when the moon is full.",
    "The veil is too thick right now.",
    "Dark omens... not likely.",
    "The cauldron bubbles with a yes.",
    "Not even the runes can tell.",
    "Yes—if you trust your intuition.",
    "Absolutely. Trust the signs.",
    "No. The fates say otherwise.",
    "A message will come in a dream."
]

# 🧙‍♀️ Oracle button + answer + Google Form log
if st.button("Consult the Oracle"):
    if name and question:
        st.write("The incense swirls... the shadows gather...")
        answer = random.choice(responses)
        st.success(f"{name}, the Oracle reveals: *{answer}*")

        # 💌 Send to Google Form (logging)
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdEYgJt63t5-xrMBWNASkWKYoZ1UzXwakZX_zyMIe7oD12vbw/formResponse"
        form_data = {
            "entry
