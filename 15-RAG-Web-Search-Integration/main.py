import streamlit as st
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
import os

# --- 1. SETUP UI ---
st.set_page_config(page_title="AI Live Web Researcher", page_icon="🌐")
st.title("🌐 RAG: Web Search Integration")
st.write("Ask me anything! I can search the live web for real-time information.")

# --- 2. CONFIGURATION (Add your keys here) ---
# In a real app, use st.secrets or environment variables
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
os.environ["TAVILY_API_KEY"] = "your_tavily_api_key"

# --- 3. INITIALIZE TOOLS & AGENT ---
def get_web_agent():
    # The Search Tool
    search_tool = TavilySearchResults(k=3) # Returns top 3 results
    
    # The LLM (The Brain)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    # The Agent: Combines LLM and Search Tool
    # ZERO_SHOT_REACT_DESCRIPTION tells the agent to "Think -> Action -> Observation"
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent

# --- 4. THE CHAT INTERFACE ---
query = st.text_input("What would you like to know today?", placeholder="e.g., What is the current price of NVDA stock?")

if query:
    with st.spinner("Searching the live web..."):
        try:
            agent_executor = get_web_agent()
            response = agent_executor.run(query)
            
            st.subheader("Search Result:")
            st.success(response)
            
        except Exception as e:
            st.error(f"Make sure you have added your API keys! Error: {e}")

# --- HOW TO RUN ---
# 1. Install requirements: pip install streamlit langchain-openai langchain-community tavily-python
# 2. Save this as app.py
# 3. Run: streamlit run app.py