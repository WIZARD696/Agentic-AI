import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

print("API key found:", bool(os.getenv("GROQ_API_KEY")))

# Create Groq client
client = Groq()

# Make a request
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain what an AI agent is in one paragraph."
        }
    ]
)

print(response.choices[0].message.content)