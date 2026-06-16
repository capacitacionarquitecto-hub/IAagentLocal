from fastapi import FastAPI
from agent import graph as agent_graph
from llm import graph as llm_graph

app = FastAPI()

@app.get("/agent")
def agent():
    return agent_graph.invoke({"value": "Hola Agentes", "custom_name": "Cliente", "name": "Cliente"})

@app.get("/llm_agent")
def llm_agent():
    return llm_graph.invoke({"question": "Give me a list of the most popular programming languages.", "name": "Andres"})