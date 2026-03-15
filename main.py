import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Conversation memory
messages = []

print("AI Chatbot started. Type 'exit' to quit.")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended")
        break

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Send conversation to model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    # Get response
    reply = response.choices[0].message.content

    # Save assistant reply
    messages.append({
        "role": "assistant",
        "content": reply
    })

    print("Bot:", reply)
