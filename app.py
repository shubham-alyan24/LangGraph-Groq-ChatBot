from typing import List, Dict 
from langgraph.graph import StateGraph,START,END
from langchain_ollama.llms import OllamaLLM

#defining state
class State(Dict):
    messages:List[Dict[str,str]] 

#initialize stategraph
graph_builder = StateGraph(State)

#initialize the llm 
llm = OllamaLLM(model="llama3.2")

#define chatbot
def chatbot(state:State):
    response = llm.invoke(state["messages"])
    state["messages"].append({"role": "assistant",
    "content":response})
    return{"messages":state["messages"]}

#add nodes and edges
graph_builder.add_node("chatbot",chatbot)
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)

#compile the graph
graph = graph_builder.compile()

# stream updates
def stream_graph_updates(user_input:str):
    #initialize state with user input
    state = {"messages":[{"role":"user",
    "content":user_input}]}
    for event in graph.stream(state):
        for value in event.values():
            #print assistant resposne 
            print("assistant: ",value["messages"][-1]["content"]
        )

if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit","exit","q"]:
                print("GoodBye!")
                break
            stream_graph_updates(user_input)
        except Exception as e:
            print(f"an error accured: {e}")
            break 


