from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.tools.retriever import create_retriever_tool

from chains.models import Command
from retrievers.retriever import compression_retriever

compression_retriever_tool = create_retriever_tool(
    compression_retriever,
    "compression_retriever",
    "Searches and returns information from vector DB.",
)
tools = [compression_retriever_tool]

memory = ConversationBufferMemory(memory_key="chat_history")

agent_chain = initialize_agent(
    tools,
    Command,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    max_iterations=3,
    early_stopping_method="generate",
    handle_parsing_errors=True,
)
