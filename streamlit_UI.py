import streamlit as st
import time
from agent.config import UserControls

# Set page configuration
st.set_page_config(
    page_title="AI News Generator",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="expanded"
)

from agent.agent import create_news_agent
from langchain_core.messages import SystemMessage, HumanMessage

def generate_news(user_controls: UserControls):
    """Executes the LangGraph agent to dynamically search and summarize news."""
    
    # Compile the LangGraph
    agent = create_news_agent()
    
    # Synthesize the exact behavioral system instruction
    system_prompt = f"""You are an elite AI News Reporter.
Your mission is to research and write a highly engaging news article about '{user_controls.topic}'.

Strict Configuration Guidelines:
- Timeframe to cover: {user_controls.timeframe}
- Length Constraint: {user_controls.length}
- Style/Tone Constraint: {user_controls.tone}

Required Steps:
1. ALWAYS invoke the tavily web-search tool to fetch accurate, recent data regarding the topic within the requested timeframe.
2. Read the search results and synthesize them into a single, cohesive article.
3. Present your final output beautifully formatted in Markdown using headers (##). 
Do NOT output "Here is the article:" or internal metadata, only the final polished article."""

    # Hydrate the initial interaction state
    initial_state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Please research the latest news regarding: {user_controls.topic}")
        ],
        "controls": user_controls
    }
    
    # Synchronously execute the full LangGraph flow
    final_state = agent.invoke(initial_state)
    
    # Retrieve the final synthesized message 
    return final_state["messages"][-1].content

def main():
    # Header Section
    st.title("📰 AI News Generator")
    st.markdown("Generate custom news articles instantly using Artificial Intelligence.")
    st.divider()

    # Sidebar for Settings
    with st.sidebar:
        st.header("⚙️ Generation Settings")
        
        timeframe = st.selectbox(
            "TimeFrame",
            ["Daily","Weekly","Monthly"],
            help="Choose the timeframe of the generated article."
        )
        
        tavily_api_key = st.text_input("Tavily Api Key", type="password")
        groq_api_key = st.text_input("Groq Api Key", type="password")
        

        tone = st.selectbox(
            "Select Tone",
            ["Informative", "Formal", "Casual", "Persuasive", "Humorous"],
            help="Choose the tone of the generated article."
        )
        
        length = st.select_slider(
            "Article Length",
            options=["Short", "Medium", "Long"],
            value="Medium",
            help="Select how long you want the news article to be."
        )
        
        st.divider()
        st.markdown(
            "**Powered by:**\n"
            "- LangGraph\n"
            "- LLMs\n"
            "- Streamlit"
        )

    # Main Content Area
    topic = st.text_input("What topic would you like news about?", placeholder="e.g., Artificial Intelligence, Space Exploration, Tech Startups...")
    
    # Generate button
    generate_btn = st.button("Generate News", type="primary")

    if generate_btn:
        if not topic.strip():
            st.warning("Please enter a valid topic to generate news.")
        else:
            controls_kwargs = {
                "topic": topic.strip(),
                "tone": tone,
                "length": length,
                "timeframe": timeframe,
            }
            # Only override API keys if they actually typed something, otherwise default from .env
            if tavily_api_key.strip(): 
                controls_kwargs["tavily_api_key"] = tavily_api_key.strip()
            if groq_api_key.strip(): 
                controls_kwargs["groq_api_key"] = groq_api_key.strip()
                
            try:
                user_controls = UserControls(**controls_kwargs)
            except Exception as e:
                st.error(f"Configuration Error: {e}")
                st.stop()
                
            with st.spinner(f"Agent is generating news about '{topic}'..."):
                # Call the mock or backend function here
                generated_article = generate_news(user_controls)
                
            st.success("Article generated successfully!")
            
            # Display the result in a clean container
            with st.container(border=True):
                st.subheader(f"Latest Update on: {topic}")
                st.markdown(generated_article)
                
            # Offer download option
            st.download_button(
                label="Download Article",
                data=f"# Latest Update on: {topic}\n\n{generated_article}",
                file_name=f"News_{topic.replace(' ', '_')}.md",
                mime="text/markdown"
            )

if __name__ == "__main__":
    main()
