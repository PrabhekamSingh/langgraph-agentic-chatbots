from langgraph.graph import StateGraph, END
from agent.data_models import AgentState

from agent.nodes.ai_news_fetch import fetch_news
from agent.nodes.ai_news_summarize import summarize_news
from agent.nodes.ai_news_save import save_result

def create_news_agent():
    """Compiles and returns the sequential pipeline as an executable graph."""
    workflow = StateGraph(AgentState)
    
    # Add nodes directly
    workflow.add_node("fetch_news", fetch_news)
    workflow.add_node("summarize_news", summarize_news)
    workflow.add_node("save_result", save_result)
    
    # Define sequential execution flow
    workflow.set_entry_point("fetch_news")
    workflow.add_edge("fetch_news", "summarize_news")
    workflow.add_edge("summarize_news", "save_result")
    workflow.add_edge("save_result", END)
    
    return workflow.compile()
