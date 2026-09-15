# LangGraph & Ollama Agentic AI Learning Project

A hands-on learning repository demonstrating the progression from basic LangGraph state machines and local Ollama chatbots to multi-agent supervisor systems and tool-calling ReAct agents.

---

## 📌 Project Overview & Structure

| File / Notebook | Description | Key Technologies |
| :--- | :--- | :--- |
| **`app.py`** | Terminal-based stateful chatbot using local LLM | LangGraph `StateGraph`, `langchain-ollama` (Llama 3.2) |
| **`agent.ipynb`** | ReAct agent with tool integration | `create_react_agent`, Wikipedia tool, `ChatGroq` |
| **`creating_tools_and_agents.ipynb`** | Custom tools (DuckDuckGo search, math) and multi-step reasoning agent | LangGraph, `ChatGroq`, DuckDuckGo Search |
| **`multi_agents_supervisor.ipynb`** | Multi-agent collaboration with a supervisor router managing specialized worker agents | `langgraph-supervisor`, ReAct agents (Math Expert & Research Expert) |

---

## 🚀 Key Modules & Progression

### 1. Basic StateGraph Chatbot (`app.py`)
- Defines state (`State`) using message lists.
- Implements a simple graph workflow: `START -> chatbot -> END`.
- Runs locally with Ollama (`llama3.2`) with streaming terminal interaction.

### 2. Single-Agent Tool Calling (`agent.ipynb`)
- Binds external tools (`WikipediaQueryRun`) to a chat model.
- Uses `create_react_agent` to enable autonomous decision-making and query answering.

### 3. Custom Tools & Agentic Reasoning (`creating_tools_and_agents.ipynb`)
- Implements custom Python functions as tools (`add`, `multiply`, `search_duckduckgo`).
- Demonstrates chained execution where the agent searches for live data (e.g., weather) and performs mathematical operations on the retrieved values.

### 4. Multi-Agent Supervisor Architecture (`multi_agents_supervisor.ipynb`)
- Sets up dedicated specialized agents:
  - **Math Expert**: Handles arithmetic operations (`add`, `multiply`).
  - **Research Expert**: Performs web searches via DuckDuckGo.
- Uses `langgraph-supervisor` (`create_supervisor`) to route complex user prompts to the appropriate expert agent and synthesize final responses.

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
```

For the notebook experiments (Groq, search, and supervisor):
```bash
pip install langchain-groq langgraph-supervisor duckduckgo-search wikipedia
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the Local Chatbot
Ensure [Ollama](https://ollama.ai/) is installed and running with `llama3.2`:
```bash
ollama run llama3.2
python app.py
```
