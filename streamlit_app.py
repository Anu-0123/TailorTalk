
import streamlit as st
import requests

st.set_page_config(page_title="TailorTalk - Booking Assistant")
st.title("📅 TailorTalk")
st.subheader("Book your appointments through conversation!")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.chat.append(("You", user_input))
    res = requests.post("http://localhost:8000/chat", json={"message": user_input})
    agent_reply = res.json()["response"]
    st.session_state.chat.append(("Agent", agent_reply))

for sender, msg in st.session_state.chat:
    st.markdown(f"**{sender}:** {msg}")

