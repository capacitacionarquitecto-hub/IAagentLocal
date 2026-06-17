from fastapi import FastAPI
from agent import graph as agent_graph
from llm import graph as llm_graph
from tools import graph as tools_graph

app = FastAPI()

@app.get("/agent")
def agent():
    return agent_graph.invoke({"value": "Hola Agentes", "custom_name": "Cliente", "name": "Cliente"})

@app.get("/llm_agent")
def llm_agent():
    return llm_graph.invoke({"question": "Give me a list of 5 countries.", "name": "Andres"})

@app.get("/tools")
def tools():
    return tools_graph.invoke({"messages":"5 veces 32"})