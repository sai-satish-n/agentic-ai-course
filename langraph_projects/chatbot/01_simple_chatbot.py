from typing import List, Dict

# StateGraph is the statemachine that will be used to define the flow of the chatbot. 
# It will have states and transitions between states.

#Start and End are special states that represent the start and end of the chatbot flow.

from langgraph.graph import StateGraph, START, END
from langchain_ollama.llms import OllamaLLM

# we will Ollama 3.1 module


# Step 1: Define State
class State (Dict):
    messages: List [Dict [str, str]]

#Step 2: Initialize StateGraph
graph_builder = StateGraph(State)

# Initialize the LLM
llm = OllamaLLM(model="llama3.2:3b")
# Define chatbot function
def chatbot (state: State):
    response = llm.invoke (state ["messages"])
    state ["messages"].append({"role": "assistant", "content": response})
    return {"messages": state ["messages"]}


# Step 3: Define the flow of the chatbot using states and transitions
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


#compile the graph
graph = graph_builder.compile()

#stream updates: to show the assitants output in the screen
def stream_graph_updates (user_input: str):
    # Initialize the state with the user's input
    state = {"messages": [{"role": "user", "content": user_input}]}
    for event in graph.stream(state):
        for value in event.values():
            # Print the assistant's response
            print("Assistant:", value ["messages"] [-1] ["content"])


# Run chatbot in a loop
if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ("quit", "exit", "goodbye"):
                print("Goodbye!")
                break
            stream_graph_updates(user_input)
        except Exception as e:
            print(f"An error occurred: {e}")
            break
