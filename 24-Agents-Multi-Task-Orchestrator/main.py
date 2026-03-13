```python
import streamlit as st
from crewai import Agent, Task, Crew, Process

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="AI Orchestrator", layout="wide")
st.title("🤖 Multi-Task Agent Orchestrator")
st.write("Enter a complex request, and watch the Orchestrator delegate tasks!")

user_input = st.text_input("What do you want to build today?", "Research the impact of AI on healthcare and write a blog post.")

if st.button("Run Orchestrator"):
    with st.status("Orchestrator is working...", expanded=True) as status:
        
        # 1. Define Specialized Agents
        st.write("🕵️ Creating Specialized Agents...")
        
        researcher = Agent(
            role='Senior Research Analyst',
            goal='Uncover cutting-edge developments in {topic}',
            backstory="You are an expert at finding and synthesizing complex information.",
            allow_delegation=False,
            verbose=True
        )
        
        writer = Agent(
            role='Content Strategist',
            goal='Write a compelling blog post based on research',
            backstory="You take complex data and turn it into engaging stories.",
            allow_delegation=False,
            verbose=True
        )

        # 2. Define Tasks
        st.write("📋 Defining Sub-Tasks...")
        
        task1 = Task(
            description=f"Analyze the following request: {user_input}. Provide a bulleted list of key findings.",
            expected_output="A summary of key trends.",
            agent=researcher
        )
        
        task2 = Task(
            description=f"Using the research, write a 300-word blog post about {user_input}.",
            expected_output="A formatted blog post.",
            agent=writer
        )

        # 3. The Orchestration (The Crew)
        st.write("🚀 Orchestrating the Workflow...")
        crew = Crew(
            agents=[researcher, writer],
            tasks=[task1, task2],
            process=Process.sequential # The Orchestrator ensures Task 1 finishes before Task 2 starts
        )

        result = crew.kickoff()
        status.update(label="Tasks Complete!", state="complete", expanded=False)

    # Display Result
    st.subheader("Final Output")
    st.markdown(result)
    st.success("The Orchestrator successfully coordinated the Researcher and the Writer.")

# TO RUN: 
# 1. Install requirements: pip install streamlit crewai
# 2. Set your API Key: export OPENAI_API_KEY='your-key'
# 3. run: streamlit run your_script.py
```