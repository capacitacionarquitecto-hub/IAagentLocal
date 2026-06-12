# IAagentLocal

Proyecto de un agente de IA local basado en LangGraph para crear workflows con múltiples nodos y ejecución condicional.

## 📋 Requisitos Previos

- Python 3.11+
- Conda (Anaconda o Miniconda)
- Poetry (para gestión de dependencias)

## 🚀 Instalación

### 1. Crear el Entorno Conda

```bash
conda create -n demo python=3.11
conda activate demo
conda install -c conda-forge poetry
conda env export > environment.yml
```

### 2. Instalar Dependencias con Poetry

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry install
```

## 📁 Estructura del Proyecto

```
IAagentLocal/
├── app/
│   ├── agent.py              # Definición del grafo y nodos
│   └── langgraph.json        # Configuración de LangGraph
├── notebooks/
│   └── 01_conditional.ipynb  # Notebook de prueba
├── pyproject.toml            # Configuración de dependencias
├── poetry.lock               # Lock file de Poetry
├── environment.yml           # Exportación del entorno Conda
├── docker-compose.yml        # Configuración Docker (opcional)
├── open-webui_docker-compose.yml
├── README.md                 # Este archivo
└── LICENSE

```

## 🔧 Cambios y Correcciones Realizadas

### 1. **Corrección en `pyproject.toml`**
   - **Problema**: `requires-python = "y"` (valor inválido)
   - **Solución**: Cambiar a `requires-python = "^3.11"` para compatibilidad con Python 3.11+

### 2. **Corrección en `app/langgraph.json`**
   - **Problema**: Campo `"dependency"` (singular) no reconocido por LangGraph CLI
   - **Solución**: Cambiar a `"dependencies"` (plural) como array:
   ```json
   {
       "dependencies": [
           "."
       ],
       "graphs": {
           "nodes_OG": "./app/agent.py:graph"
       },
       "python_version": "3.11"
   }
   ```

### 3. **Corrección en `app/agent.py`**
   - **Problema**: KeyError `'custom_name'` en node_2
   - **Root Cause**: Typo - node_1 establecía `state["customer_name"]` pero node_2 buscaba `state["custom_name"]`
   - **Solución**: Unificar el nombre de variable a `custom_name` en node_1
   ```python
   # Antes: state["customer_name"] = "Node 1"
   # Después: state["custom_name"] = "Node 1"
   ```

### 4. **Instalación de Dependencias**
   - Se agregaron a `pyproject.toml`:
     - `langgraph (>=1.2.4,<2.0.0)` - Framework de grafos
     - `langchain-openai (>=1.3.0,<2.0.0)` - Integración con OpenAI
     - `python-dotenv (>=1.2.2,<2.0.0)` - Manejo de variables de entorno
     - `langgraph-cli[inmem] (>=0.4.28,<0.5.0)` - CLI de LangGraph con runtime en memoria

## 🏃 Ejecutar la Aplicación

### Usar LangGraph Dev Server

```bash
cd F:\CAPACITACION\PORTAFOLIO\IAagentLocal
poetry run langgraph dev --config app/langgraph.json
```

Esto inicia un servidor de desarrollo en:
- **API**: http://127.0.0.1:2024
- **Studio UI**: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

### Ejecutar Notebooks

```bash
# Instalar Jupyter si no está disponible
pip install jupyter

# Ejecutar notebook
jupyter notebook notebooks/01_conditional.ipynb
```

## 📊 Estructura del Grafo (agent.py)

El grafo define 3 nodos:

```
START → node_1 → node_2 → node_3 → END
```

**node_1**: Inicializa estado con valor "Hello World, New Agent" y custom_name = "Node 1"

**node_2**: Accede a custom_name y crea un mensaje concatenado

**node_3**: Nodo final de transición

**Estado (TypedDict)**:
```python
class State(TypedDict):
    name: str
    value: str
    custom_name: str
```

## 🐳 Docker (Opcional)

Para ejecutar con Docker Compose:

```bash
docker-compose up -d
```

## 📝 Notas Importantes

1. **Versión de Python**: El proyecto está configurado para Python 3.11+
2. **Variables de Entorno**: Crear un archivo `.env` si se necesita configurar variables (OpenAI API key, etc.)
3. **Persistencia**: El servidor dev usa persistencia en memoria (no persistente entre reinicios)
4. **Studio**: Acceder a LangGraph Studio en el navegador para visualizar y depurar el grafo

## 📚 Referencias

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [Poetry Documentation](https://python-poetry.org/)

