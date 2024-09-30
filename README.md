# AI Chatbot using Langchain

This Python script implements a simple AI chatbot using the `langchain_ollama` and `langchain_core` libraries. The chatbot utilizes a language model named "llama3" and maintains a conversation history to provide context-aware responses.

## Code Overview

### Imports

First, the necessary classes from the `langchain_ollama` and `langchain_core` libraries are imported:

```python
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

```

### Using the Bot

After starting Ollama, use `ollama run llama3` to interact with the bot.
