from fastapi import FastAPI
from agent import graph


app = FastAPI()


@app.get("/")
def agent():
    return graph.invoke({"value":"Hola Agentes", "custom_name": "Cliente"})