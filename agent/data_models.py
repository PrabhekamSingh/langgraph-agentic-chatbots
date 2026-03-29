from typing import TypedDict, Annotated, List, Literal, Any, Dict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from agent.config import UserControls

class AgentState(TypedDict, total=False):
    messages: Annotated[List[BaseMessage], add_messages]
    controls: UserControls
    frequency: str
    news_data: List[Dict[str, Any]]