# Import necessary classes from langchain_ollama and langchain_core libraries
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define a template for the chatbot's prompt
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Instantiate the language model (OllamaLLM) with a specific model ("llama3")
model = OllamaLLM(model="llama3")

# Create a ChatPromptTemplate using the defined template
prompt = ChatPromptTemplate.from_template(template)

# Create a chain by combining the prompt with the model
chain = prompt | model

def handle_converstation():
    """
    Function to handle the conversation between the user and the AI chatbot.
    """
    context = ""  # Initialize an empty string to keep track of the conversation history
    print("Welcome to the AI Chatbot, Type 'exit' to quit.")  # Display a welcome message to the user
    while True:
        user_input = input("You: ")  # Get input from the user
        if user_input.lower() == "exit":  # Check if the user wants to exit the conversation
            break  # Exit the loop if 'exit' is typed
        # Invoke the chain with the current context and user input, and get the result
        result = chain.invoke({"context": context, "question": user_input})
        print("Kevbot: ", result)  # Print the AI's response
        # Update the context with the new user input and AI response
        context += f"\nUser:{user_input}\nAI: {result}"

# Entry point of the script, ensures the handle_converstation function runs if this script is executed
if __name__ == "__main__":
    handle_converstation()
