from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    name: str
    value: str
    custom_name: str

#Define node class
def node_1(state: State) -> State:
    state["value"] ="Hello World, New Agent"
    state["custom_name"] = "Node 1"
    return state


def node_2(state: State) -> State:
    customer_name = state["custom_name"]
    state["value"] = f"{customer_name} says Hello World, New Agent"
    return state


def node_3(state: State) -> State:
   
    return state


#Define edge class

builder = StateGraph(State)

builder.add_node('node_1', node_1)
builder.add_node('node_2', node_2)
builder.add_node('node_3', node_3)

builder.add_edge(START, 'node_1')
builder.add_edge('node_1', 'node_2')
builder.add_edge('node_2', 'node_3')
builder.add_edge('node_3', END)

graph = builder.compile()