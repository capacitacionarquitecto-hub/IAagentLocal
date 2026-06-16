from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize the Ollama model
model = init_chat_model(
    model="nemotron-3-super:cloud",          # Replace with any model you have downloaded in Ollama
    model_provider="ollama"       # Directs LangChain to use the Ollama integration
)


class State(BaseModel):
    question: str = ""
    name: str = ""
    value: str = ""
    system_message: str = "You are a helpful assistant and you politely answer the user's questions."

system_message = SystemMessage(content="You are a helpful assistant and you poliytely answer the user's questions, I am {name}, and I ask {question}")

def node_llm(state:State) -> State:
    # Here you would call your LLM and return the response
    # Format system message with state values
    formatted_system = state.system_message.format(name=state.name, question=state.question) if '{' in state.system_message else state.system_message
    sys_msg = SystemMessage(content=formatted_system)
    user_msg = HumanMessage(content=state.question)
    response = model.invoke([sys_msg, user_msg])
    return State(question=state.question, name=state.name, value=response.content, system_message=state.system_message)

#Define edge class

builder = StateGraph(State)

builder.add_node('node_llm', node_llm)

builder.add_edge(START, 'node_llm')
builder.add_edge('node_llm', END)

graph = builder.compile()
