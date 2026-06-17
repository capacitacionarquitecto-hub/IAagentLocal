from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode,tools_condition
from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chat_models import init_chat_model

def multiply (a: int, b: int) -> int:
    """ Multiply a asnd b and return the result. 
    args:
        a: the first number to multiply 
        b: the second number to multiply
    returns:     the result of multiplying a and b
     example:
        >>> multiply(2, 3)
        6
    
    """
    return a * b

def add (a: int, b: int) -> int:
    """ Add a and b and return the result.
    args:
        a: the first number to add
        b: the second number to add
    returns:     the result of adding a and b
     example:
        >>> add(2, 3)
        5
    
    """
    return a + b

tools = [multiply, add]

class State(MessagesState):
    response: str = ""

# Initialize the Ollama model
model = init_chat_model(
    model="nemotron-3-super:cloud",          # Replace with any model you have downloaded in Ollama
    model_provider="ollama"       # Directs LangChain to use the Ollama integration
)
model.bind_tools(tools, parallel_tools_calls=False)

def _normalize_messages(messages):
    if isinstance(messages, str):
        return [HumanMessage(content=messages)]
    if isinstance(messages, list) and messages and isinstance(messages[0], str):
        return [HumanMessage(content=m) for m in messages]
    return messages


def assistan(state: State) -> State:
    system_message = SystemMessage(content="Eres un experto en matemáticas y debe ayudar a resolver los problemas.")
    messages = _normalize_messages(state["messages"])
    response = model.invoke([system_message] + messages)
    return {
        "messages": [*(m.content if hasattr(m, "content") else str(m) for m in messages), response.content],
        "response": response.content,
    }

#define graph
builder = StateGraph(State)
builder.add_node('assistan', assistan)
builder.add_node('tools', ToolNode(tools))

builder.add_edge(START, 'assistan')
builder.add_conditional_edges('assistan',tools_condition)
builder.add_edge('tools', 'assistan')

graph = builder.compile()
