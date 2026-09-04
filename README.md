# 🤖 Agentic AI — LangChain & MCP Learning

A hands-on repository for learning and implementing the core building blocks of **Agentic AI** using Python, LangChain, Groq, and Model Context Protocol (MCP).

The repository focuses on understanding how LLMs, prompts, chains, memory, agents, and tools work together to build AI-powered applications.

## 📁 Project Structure

| File | Description |
|---|---|
| `core_building_blocks.py` | Demonstrates fundamental LangChain concepts including LLM integration with Groq, prompt templates, chat prompts, LCEL chains, output parsing, and conversational memory. |
| `first_AI_Agent.py` | Introduces the basic architecture and implementation of an AI agent capable of reasoning and interacting with tools. |
| `mcp.py` | Implements a basic **MCP (Model Context Protocol) server** using Python and FastMCP, exposing custom functions as tools that AI applications can interact with. |
| `responses_api.py` | Explores API-based interaction with language models and demonstrates how model responses can be generated and processed programmatically. |
| `.gitignore` | Prevents sensitive configuration files such as `.env` and generated Python files from being committed to the repository. |

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Groq**
- **MCP (Model Context Protocol)**
- **FastMCP**
- **LLMs**
- **Prompt Engineering**

## 🧠 Concepts Covered

- LLM & Chat Model Integration
- Prompt Engineering
- Prompt Templates
- LCEL & Chains
- Output Parsers
- Conversational Memory
- AI Agents
- Tool Calling
- Model Context Protocol (MCP)

## 🔐 Environment Variables

API credentials are stored locally in a `.env` file and are intentionally excluded from version control.

Example:

```env
GROQ_API_KEY=your_api_key_here

Never commit API keys or other secrets to GitHub.

🚧 Status

This repository is actively evolving as I continue learning and experimenting with LangChain, Agentic AI, AI Agents, and MCP.

🎯 Learning Goal

To build a strong practical understanding of how modern LLM-powered agents are designed, connected to tools, and developed into reliable Agentic AI systems.
