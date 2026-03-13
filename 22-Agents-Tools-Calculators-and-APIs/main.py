```python
# First, pip install streamlit langchain langchain-openai duckduckgo-search
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

# Streamlit UI Setup
st.set_page_config(page_title="AI Agent with Tools", page_icon="🤖")
st.title("🤖 AI Agent: I have a Utility Belt!")
st.write("I can use a **Calculator** and **Google Search** to answer your questions.")

# Input for OpenAI API Key
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if api_key:
    # 1. Initialize the LLM (The Brain)
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, temperature=0)

    # 2. Define the Tools (The Utility Belt)
    # 'llm-math' is a calculator, 'ddg-search' is DuckDuckGo web search
    tools = load_tools(["ddg-search", "llm-math"], llm=llm)

    # 3. Initialize the Agent
    # ZERO_SHOT_REACT_DESCRIPTION allows the agent to decide which tool to use based on the tool's description
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )

    user_query = st.text_input("Ask me something (e.g., 'What is the current price of Bitcoin and what is that divided by 2?')")

    if user_query:
        with st.spinner("Thinking and using tools..."):
            try:
                # The agent will:
                # 1. Search for BTC price
                # 2. Use the calculator to divide by 2
                # 3. Give the final answer
                response = agent.run(user_query)
                st.success(response)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Please enter your OpenAI API Key in the sidebar to start.")

# TO RUN: streamlit run your_script_name.py
```