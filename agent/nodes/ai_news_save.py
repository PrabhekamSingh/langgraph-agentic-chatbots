import os
from agent.data_models import AgentState

def save_result(state: AgentState):
    """Saves the final summarized news markdown to disk for persistence if needed."""
    
    # Check if a generated message exists
    if not state.get("messages"):
        return state
        
    final_content = state["messages"][-1].content
    topic = state["controls"].topic.replace(" ", "_")
    
    filename = f"generated_news_{topic}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    # No state state modifications needed, return empty delta
    return {}
