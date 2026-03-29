# End-to-End Agentic AI Chatbots

A comprehensive project demonstrating the implementation of agentic AI chatbots using LangGraph, featuring multiple use cases with web interfaces built using Streamlit.

## Features

- **Basic Chatbot**: Simple conversational AI using LangGraph and Groq LLM
- **Chatbot with Web Tools**: Advanced chatbot with integrated web search capabilities using Tavily
- **Modular Architecture**: Clean separation of concerns with dedicated modules for graph building, LLMs, nodes, state management, tools, and UI
- **Streamlit UI**: Interactive web interface for easy interaction with the chatbots
- **Multiple LLM Support**: Configurable LLM options with Groq models

## Project Structure

```
├── app.py                          # Main application entry point
├── main.py                         # Alternative entry point
├── pyproject.toml                  # Project configuration and dependencies
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── src/
    └── langgraphagenticai/
        ├── main.py                 # Core application logic
        ├── graph/
        │   └── graph_builder.py    # LangGraph construction logic
        ├── LLMS/
        │   └── groqllm.py          # Groq LLM configuration
        ├── nodes/
        │   ├── basic_chatbot_node.py       # Basic chatbot node
        │   └── chatbot_with_Tool_node.py   # Tool-enabled chatbot node
        ├── state/
        │   └── state.py            # State management for LangGraph
        ├── tools/
        │   └── search_tool.py      # Web search tool implementation
        └── ui/
            ├── uiconfigfile.ini    # UI configuration
            ├── uiconfigfile.py     # UI config handler
            └── streamlitui/
                ├── display_result.py   # Result display logic
                └── loadui.py           # Streamlit UI loader
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Chatbot_with_Web
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Obtain API keys for Groq and Tavily
   - Set the following environment variables:
     ```bash
     export GROQ_API_KEY="your-groq-api-key"
     export TAVILY_API_KEY="your-tavily-api-key"
     ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**:
   - Open your browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`)

3. **Select a use case**:
   - **Basic Chatbot**: Choose this for simple conversational AI
   - **Chatbot With Web**: Choose this for AI with web search capabilities

4. **Configure settings**:
   - Select your preferred LLM model from the available Groq options
   - Enter your message in the chat input

5. **Interact**:
   - The chatbot will respond based on the selected use case and model

## Dependencies

- **LangChain**: Framework for building LLM applications
- **LangGraph**: Library for building stateful, multi-actor applications
- **Streamlit**: Web app framework for Python
- **Groq**: Fast LLM inference platform
- **Tavily**: Web search API
- **FAISS**: Vector database for efficient similarity search

## Configuration

The application uses a configuration file (`src/langgraphagenticai/ui/uiconfigfile.ini`) to manage:

- Page title
- Available LLM options
- Use case options
- Groq model options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built using [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Groq](https://groq.com/)
- Web search capabilities provided by [Tavily](https://tavily.com/)# langgraph-agentic-chatbots
