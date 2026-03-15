import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

# create groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Chatbot 🤖")

# conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# user input
prompt = st.chat_input("Ask something...")

if prompt:

    # add user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # call groq API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # store response
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)