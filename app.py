import streamlit as st
from groq import Groq
import os

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 MC STAN")

# Sidebar personality selector
st.sidebar.title("Bot Personality")

personality = st.sidebar.selectbox(
    "Choose personality",
    [
        "Friendly Assistant",
        "Sarcastic Bot",
        "Professor",
        "Coding Mentor",
        "Motivational Coach"
    ]
)

# Personality prompts
if personality == "Friendly Assistant":
    system_prompt = "You are a friendly AI assistant who helps users politely."

elif personality == "Sarcastic Bot":
    system_prompt = "You are a witty and sarcastic AI assistant who replies with clever humor."

elif personality == "Professor":
    system_prompt = "You are a professor who explains topics clearly and step by step."

elif personality == "Coding Mentor":
    system_prompt = "You are a senior software engineer who helps users learn programming."

elif personality == "Motivational Coach":
    system_prompt = "You are a motivational coach who encourages users positively."


# API key from Streamlit secrets
api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# Show chat history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Call Groq API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)