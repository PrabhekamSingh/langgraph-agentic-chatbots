import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
from agent.data_models import AgentState

def summarize_news(state: AgentState):
    """Summarizes fetched news data into a requested word count limit."""
    news_data = state.get("news_data", [])
    controls = state["controls"]
    
    groq_key = controls.groq_api_key or os.getenv("GROQ_API_KEY")
    if not groq_key:
        raise ValueError("Groq API Key is missing.")
        
    model = ChatGroq(
        api_key=groq_key,
        model_name="llama3-70b-8192", 
        temperature=0.3
    )
    
    # Prepare the context
    news_context = ""
    for idx, item in enumerate(news_data):
        news_context += f"Source {idx+1}:\nTitle: {item.get('title')}\nContent: {item.get('content')}\n\n"
        
    system_prompt = f"""You are an elite AI News Reporter. 
Your mission is to write a highly engaging news article about '{controls.topic}'.

Strict Constraints:
- Tone/Style: {controls.tone}
- CRITICAL OUTPUT LENGTH CONSTRAINT: Your task is to output a description of 350 words or less. DO NOT exceed 350 words!

Here is the retrieved news context from Tavily search:
{news_context}

Please synthesize the findings into a compelling news format reflecting the constraints above. Present output beautifully formatted in Markdown."""

    # Add the single instruction to messages
    messages = [SystemMessage(content=system_prompt)]
    
    response = model.invoke(messages)
    
    return {"messages": [response]}
