```python
import os
import streamlit as st
from swarms import Agent

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="AI Swarm Manager", layout="wide")
st.title("🚀 AI Swarm: Manager & Worker Workflow")
st.write("This app simulates a Manager Agent delegating tasks to specialized Workers.")

# Get your API Key (In production, use secrets)
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

    # --- 1. DEFINE THE WORKERS (The Specialists) ---
    
    # Worker 1: The Researcher
    researcher = Agent(
        agent_name="Researcher",
        system_prompt="You are a world-class tech researcher. Find the latest trends and facts about the topic provided.",
        llm_name="gpt-4o",
        max_loops=1,
        dashboard=False
    )

    # Worker 2: The Writer
    writer = Agent(
        agent_name="Writer",
        system_prompt="You are a professional blog writer. Turn research data into an engaging 3-paragraph blog post.",
        llm_name="gpt-4o",
        max_loops=1,
        dashboard=False
    )

    # --- 2. DEFINE THE MANAGER (The Boss) ---
    manager = Agent(
        agent_name="Manager",
        system_prompt="You are the Project Manager. You receive a topic, ask the Researcher for facts, then give those facts to the Writer to create a post. Finally, output the finished post.",
        llm_name="gpt-4o",
        max_loops=1,
        dashboard=False
    )

    # --- UI INTERACTION ---
    user_task = st.text_input("Enter a topic for the Swarm to handle:", "The future of Quantum Computing")

    if st.button("Launch Swarm"):
        with st.spinner("Manager is coordinating workers..."):
            # Step 1: Manager instructs Researcher
            st.subheader("Step 1: Researching...")
            research_data = researcher.run(f"Research the following topic: {user_task}")
            st.info(research_data)

            # Step 2: Manager instructs Writer using Research results
            st.subheader("Step 2: Writing...")
            final_blog = writer.run(f"Write a blog post based on this research: {research_data}")
            st.success(final_blog)

            # Step 3: Manager Final Review
            st.subheader("Step 3: Final Manager Approval")
            final_output = manager.run(f"Review and finalize this post for the user: {final_blog}")
            st.balloons()
            st.markdown(f"### Final Result:\n{final_output}")

else:
    st.warning("Please enter your OpenAI API Key in the sidebar to begin.")

# To run this: 
# 1. Install swarms: pip install swarms streamlit
# 2. Run: streamlit run your_filename.py
```