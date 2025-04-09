import streamlit as st
import random
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

# 🌟 Google Sheets Setup (Place this block right here!)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("oracle-8-ball-logger-42273e86e0ec.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Oracle Log").sheet1
