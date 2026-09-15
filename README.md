# LangGraph & Groq Agentic AI Learning Project

A hands-on learning repository demonstrating the progression from basic LangGraph state machines to tool-calling ReAct agents and multi-agent supervisor systems powered by **Groq** (`ChatGroq`).

---

## 📌 Project Overview & Structure

| File / Notebook | Description | Key Technologies |
| :--- | :--- | :--- |
| **`app.py`** | Terminal-based stateful chatbot with LangGraph | LangGraph `StateGraph`, State Management |
| **`agent.ipynb`** | ReAct agent with tool integration | `create_react_agent`, Wikipedia tool, `ChatGroq` |
| **`creating_tools_and_agents.ipynb`** | Custom tools (DuckDuckGo search, math) and multi-step reasoning | LangGraph, `ChatGroq`, DuckDuckGo Search |
| **`multi_agents_supervisor.ipynb`** | Multi-agent collaboration with a supervisor router managing specialized worker agents | `langgraph-supervisor`, `ChatGroq`, Math & Research Experts |

---

## 🚀 Key Modules & Progression

### 1. Basic StateGraph Chatbot (`app.py`)
- Defines state (`State`) using message lists.
- Implements a simple graph workflow: `START -> chatbot -> END`.
- Streaming terminal interaction.

### 2. Single-Agent Tool Calling (`agent.ipynb`)
- Binds external tools (`WikipediaQueryRun`) to Groq models (`ChatGroq`).
- Uses `create_react_agent` to enable autonomous decision-making and query answering.

### 3. Custom Tools & Agentic Reasoning (`creating_tools_and_agents.ipynb`)
- Implements custom Python functions as tools (`add`, `multiply`, `search_duckduckgo`).
- Demonstrates chained execution where the Groq agent searches for live data (e.g., weather) and performs mathematical operations on the retrieved values.

### 4. Multi-Agent Supervisor Architecture (`multi_agents_supervisor.ipynb`)
- Sets up dedicated specialized agents using Groq:
  - **Math Expert**: Handles arithmetic operations (`add`, `multiply`).
  - **Research Expert**: Performs web searches via DuckDuckGo.
- Uses `langgraph-supervisor` (`create_supervisor`) powered by Groq to route complex user prompts to the appropriate expert agent and synthesize final responses.

---

## 🛠️ Setup & Installation

### 1. Clone Repository & Create Virtual Environment
```bash
git clone https://github.com/shubham-alyan24/LangGraph-Ollama-ChatBot.git
cd LangGraph-Ollama-ChatBot
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
pip install langchain-groq langgraph-supervisor duckduckgo-search wikipedia python-dotenv
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
