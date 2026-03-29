import os
from agent.data_models import AgentState
from tavily import TavilyClient

def fetch_news(state: AgentState):
    """Node that invokes the Tavily web-search tool to fetch accurate, recent data."""
    tavily_key = state["controls"].tavily_api_key or os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        raise ValueError("Tavily API Key is missing. Please provide it in the UI or .env file.")
        
    client = TavilyClient(api_key=tavily_key)
    timeframe = state["controls"].timeframe.lower()
    
    frequency_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'yearly': 'y'}
    days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'yearly': 365}
        
    query = f"Latest news regarding {state['controls'].topic}"
    
    # We use query=query instead of input=query since Tavily SDK uses query
    response = client.search(
        query=query,
        topic='news',
        time_range=frequency_map.get(timeframe, 'w'),
        days=days_map.get(timeframe, 7),
        max_results=5,
        include_answer=True,
    )
    
    # Return delta for AgentState dictionary
    return {"news_data": response.get("results", [])}
