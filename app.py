import streamlit as st
import random
from datetime import datetime

st.title("Witchy Oracle 8 Ball")
st.subheader("Summon the wisdom of the unseen...")

name = st.text_input("Your name, seeker of hidden truths:")
question = st.text_input("Ask your yes-or-no question:")

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

if st.button("Consult the Oracle"):
    if name and question:
        st.write("The incense swirls... the shadows gather...")
        answer = random.choice(responses)
        st.success(f"{name}, the Oracle reveals: *{answer}*")

        # Log the question and answer to a file
        with open("questions_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - {name} asked: \"{question}\" | Oracle answered: \"{answer}\"\n")
    else:
        st.warning("You must offer both your name and a question.")
with st.expander("🔐 View Oracle Log (Private Eyes Only)"):
    try:
        with open("questions_log.txt", "r") as f:
            log_data = f.read()
            st.text(log_data)
    except FileNotFoundError:
        st.info("No questions have been asked yet.")
