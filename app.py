import os
from typing import TypedDict, Annotated

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

# Schemas
class ChatState(TypedDict):
    messages: Annotated[list, add_messages]

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-8b-8192")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

llm = ChatGroq(
    model=GROQ_MODEL,
    groq_api_key=GROQ_API_KEY,
)

# Initialize the graph
def chatbot_node(state: ChatState) -> ChatState:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

builder = StateGraph(ChatState)
builder.add_node("chatbot", chatbot_node)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()

user_text = "can you help me write code for building a simpole chatbot with langgraph from scratch?"
result = graph.invoke({"messages": [HumanMessage(content=user_text)]})

print(result["messages"][-1].content)