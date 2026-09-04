import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import os
from pathlib import Path
from dotenv import load_dotenv

# =========================
# LOAD ENVIRONMENT VARIABLES
# =========================

script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"

load_dotenv(dotenv_path=env_path)

print("GROQ_API_KEY found:", bool(os.getenv("GROQ_API_KEY")))


# =========================
# INITIALIZE GROQ MODEL
# =========================

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)

response = model.invoke(
    "What is LangChain in one sentence?"
)

print("=== Model Response ===")
print(response.content)
print()


# =========================
# PROMPT TEMPLATE
# =========================

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)

simple_template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} to a complete beginner in 2-3 sentences."
)

formatted = simple_template.format(topic="AI agents")

print("=== Formatted Prompt ===")
print(formatted)
print()


# =========================
# CHAT PROMPT TEMPLATE
# =========================

chat_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful coding tutor. Keep answers short and clear."
    ),
    (
        "human",
        "Explain {concept} with a simple Python example."
    ),
])

messages = chat_template.format_messages(
    concept="list comprehension"
)

print("=== Chat Messages ===")

for msg in messages:
    print(f"[{msg.type}]: {msg.content[:80]}...")

print()


# =========================
# CHAINS
# =========================

from langchain_core.output_parsers import StrOutputParser

# Prompt → Model → Parser
chain = chat_template | model | StrOutputParser()

result = chain.invoke({
    "concept": "for loops"
})

print("=== Chain Output ===")
print(result)
print()


# =========================
# MEMORY
# =========================

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

memory = InMemoryChatMessageHistory()

memory.add_message(
    HumanMessage(
        content="My name is Mansiz and I'm learning LangChain"
    )
)

memory.add_message(
    AIMessage(
        content="Nice to meet you, Mansiz! LangChain is a great choice."
    )
)

memory.add_message(
    HumanMessage(
        content="What tools should I learn first?"
    )
)

memory.add_message(
    AIMessage(
        content="Start with PromptTemplates and simple chains, then move to tools and agents."
    )
)

print("=== Memory Contents ===")

for msg in memory.messages:
    print(f"[{msg.type}]: {msg.content[:80]}...")

print()


# =========================
# MEMORY-AWARE PROMPT
# =========================

chat_with_memory = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful tutor. Use the conversation history "
        "to personalize your responses."
    ),

    MessagesPlaceholder(variable_name="history"),

    ("human", "{question}"),
])

chain_with_memory = (
    chat_with_memory
    | model
    | StrOutputParser()
)

result = chain_with_memory.invoke({
    "history": memory.messages,
    "question": "What was my name again?"
})

print("=== Memory-Aware Response ===")
print(result)
print()