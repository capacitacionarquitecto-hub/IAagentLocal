# IAagentLocal

Proyecto de un agente de IA local basado en LangGraph para crear workflows con múltiples nodos, ejecución condicional y APIs para invocar dos grafos distintos.

---

## 🚀 Qué hace este proyecto

- Ejecuta grafos de LangGraph definidos en `app/agent.py` y `app/llm.py`
- Expone dos endpoints HTTP:
  - `/agent` → grafo clásico de nodos con flujo de estado
  - `/llm_agent` → grafo con un nodo LLM que recibe `system_message`, `question` y `name`
- Permite probar agentes desde una API local sin necesidad de abrir notebooks

---

## 📋 Requisitos Previos

- Python 3.11+
- Conda (Anaconda o Miniconda)
- Poetry
- `uvicorn` para correr la API FastAPI

---

## 🧩 Estructura del Proyecto

```
IAagentLocal/
├── app/
│   ├── agent.py              # Grafo nodes_OG
│   ├── llm.py                # Grafo llm_agent con LLM
│   ├── api.py                # Endpoints FastAPI
│   └── langgraph.json        # Configuración de LangGraph
├── notebooks/
│   └── 01_conditional.ipynb  # Notebook de ejemplo
├── pyproject.toml
├── poetry.lock
├── environment.yml
├── docker-compose.yml
├── open-webui_docker-compose.yml
└── README.md
```

---

## 🔧 Instalación y dependencias

### 1) Crear el entorno Conda

```bash
conda create -n iaagentlocal python=3.11 -y
conda activate iaagentlocal
```

### 2) Instalar Poetry

```bash
conda install -c conda-forge poetry -y
```

### 3) Instalar dependencias del proyecto

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry install
```

### 4) Instalar FastAPI / Uvicorn (si no están instalados)

```bash
poetry add fastapi uvicorn
```

> Si no usas Poetry, puedes instalar con `pip install fastapi uvicorn`.

---

## 🏃‍♂️ Ejecutar los agentes desde las APIs

### Opción A: Iniciar la API local

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry run uvicorn app.api:app --reload --port 8000
```

### Endpoints disponibles

- `http://127.0.0.1:8000/agent` → ejecuta `app/agent.py`
- `http://127.0.0.1:8000/llm_agent` → ejecuta `app/llm.py`

### Ejemplos de uso

```bash
curl http://127.0.0.1:8000/agent
curl http://127.0.0.1:8000/llm_agent
```

### Ejemplos de uso con `/llm_agent` y payload JSON

```bash
curl -X POST http://127.0.0.1:8000/llm_agent \
  -H "Content-Type: application/json" \
  -d '{"question": "¿Cuál es 2 + 2?", "name": "Andrés"}'

curl -X POST http://127.0.0.1:8000/llm_agent \
  -H "Content-Type: application/json" \
  -d '{"question": "Escribe un saludo corto.", "name": "María", "system_message": "Eres una asistente amable que responde en español."}'
```

### Opción B: Ejecutar LangGraph Dev Server

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry run langgraph dev --config app/langgraph.json
```

Esto inicia el servidor LangGraph:
- **API**: http://127.0.0.1:2024
- **Studio UI**: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

---

## 💡 Cómo funciona cada grafo

### `/agent` — grafo clásico (`app/agent.py`)

- Flujo lineal: `START → node_1 → node_2 → node_3 → END`
- `node_1` inicializa el estado
- `node_2` transforma los datos usando el valor anterior
- `node_3` finaliza el recorrido
- Ideal para lógica de negocio secuencial y procesamiento de estado

### `/llm_agent` — grafo LLM (`app/llm.py`)

- Recibe `question`, `name` y `system_message`
- Construye un `SystemMessage` dinámico usando esos valores
- Pasa `SystemMessage` + `HumanMessage` al modelo LangChain
- Devuelve un nuevo estado con la respuesta en `value`
- Ideal para chatbots o agentes conversacionales con instrucciones personalizadas

---

## 🌟 Características principales

- Dos agentes separados con responsabilidades claras
- API REST fácil de consumir
- Uso de `State` tipado con Pydantic para validación
- Soporte para mensajes de sistema dinámicos
- Puede ejecutarse desde FastAPI o desde LangGraph Studio

---

## ⚠️ Notas importantes

- El endpoint `/agent` usa `agent.py`
- El endpoint `/llm_agent` usa `llm.py`
- Si usas `/llm_agent`, asegúrate de enviar `question` y `name` según tu caso
- Para variables de entorno, añade un archivo `.env` en la raíz si necesitas claves de API

---

## 📚 Referencias

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Poetry Documentation](https://python-poetry.org/)

---

# IAagentLocal (English)

Local AI agent project based on LangGraph, with multiple node workflows, conditional execution, and HTTP APIs.

## 🚀 What this project does

- Runs two separate graphs:
  - `app/agent.py` → classic node workflow
  - `app/llm.py` → LLM-based node workflow
- Exposes two HTTP endpoints:
  - `/agent` for the classic agent graph
  - `/llm_agent` for the LLM graph
- Lets you test agents from a local API without opening notebooks

## 📋 Prerequisites

- Python 3.11+
- Conda (Anaconda or Miniconda)
- Poetry
- `uvicorn` for FastAPI

## 🧩 Project structure

```
IAagentLocal/
├── app/
│   ├── agent.py
│   ├── llm.py
│   ├── api.py
│   └── langgraph.json
├── notebooks/
├── pyproject.toml
├── poetry.lock
├── environment.yml
├── docker-compose.yml
├── open-webui_docker-compose.yml
└── README.md
```

## 🔧 Install dependencies

### 1) Create the Conda environment

```bash
conda create -n iaagentlocal python=3.11 -y
conda activate iaagentlocal
```

### 2) Install Poetry

```bash
conda install -c conda-forge poetry -y
```

### 3) Install project dependencies

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry install
```

### 4) Install FastAPI / Uvicorn

```bash
poetry add fastapi uvicorn
```

> Or: `pip install fastapi uvicorn`

## 🏃 Run the agents via API

### Option A: start the local API

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry run uvicorn app.api:app --reload --port 8000
```

### Available endpoints

- `http://127.0.0.1:8000/agent`
- `http://127.0.0.1:8000/llm_agent`

### Example calls

```bash
curl http://127.0.0.1:8000/agent
curl http://127.0.0.1:8000/llm_agent
```

### Option B: run LangGraph Dev Server

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry run langgraph dev --config app/langgraph.json
```

This starts:
- **API**: http://127.0.0.1:2024
- **Studio UI**: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

## 💡 How each graph works

### `/agent` — classic graph (`app/agent.py`)

- Linear workflow: `START → node_1 → node_2 → node_3 → END`
- `node_1` initializes state
- `node_2` transforms state data
- `node_3` completes the workflow
- Good for sequential business logic

### `/llm_agent` — LLM graph (`app/llm.py`)

- Accepts `question`, `name`, and `system_message`
- Builds a dynamic `SystemMessage` from state values
- Sends `SystemMessage` + `HumanMessage` to the model
- Returns the answer in `value`
- Ideal for conversational agents and prompt customization

## 🌟 Main features

- Two separate agent graphs
- REST API access
- Pydantic-validated state model
- Dynamic system prompt support
- Can run with FastAPI or LangGraph Studio

## ⚠️ Important notes

- `/agent` calls `agent.py`
- `/llm_agent` calls `llm.py`
- If you use `/llm_agent`, send `question` and `name` as appropriate
- Add a `.env` file if you need API keys or environment variables

## 📚 References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Poetry Documentation](https://python-poetry.org/)

