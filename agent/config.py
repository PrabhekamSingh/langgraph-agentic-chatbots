from typing import Optional, Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class UserControls(BaseSettings):
    """
    Configuration for User Controls and API Keys.
    Values can be populated directly or loaded from the .env file.
    """
    # API Keys
    tavily_api_key: Optional[str] = Field(default=None, description="API Key for Tavily Search")
    groq_api_key: Optional[str] = Field(default=None, description="API Key for Groq LLM")
    
    # User UI Inputs
    topic: str = Field(default="", description="The topic to generate news about")
    tone: Literal["Informative", "Formal", "Casual", "Persuasive", "Humorous"] = Field(default="Informative", description="The tone of the generated article")
    length: Literal["Short", "Medium", "Long"] = Field(default="Medium", description="The length of the news article")
    timeframe: Literal["Daily", "Weekly", "Monthly"] = Field(default="Weekly", description="The timeframe for the news")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
