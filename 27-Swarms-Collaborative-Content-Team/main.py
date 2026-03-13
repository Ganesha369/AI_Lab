import streamlit as st
from swarms import Agent, SequentialWorkflow

# 1. Setup the Streamlit UI
st.set_page_config(page_title="AI Content Swarm", layout="wide")
st.title("🚀 Multi-Agent Collaborative Content Team")
st.write("Input a topic and watch the Researcher, Writer, and Editor work together.")

topic = st.text_input("Enter a topic for the article:", "The Future of Quantum Computing")

if st.button("Generate Content"):
    with st.status("Swarm at work...", expanded=True) as status:
        
        # 2. Define our Agents (The Team)
        
        # The Researcher
        researcher = Agent(
            agent_name="Researcher",
            system_prompt="Gather key facts, statistics, and recent breakthroughs about the given topic.",
            llm_name="gpt-4o", # Simplified for example
        )

        # The Writer
        writer = Agent(
            agent_name="Writer",
            system_prompt="Use the research provided to write a 300-word engaging blog post.",
            llm_name="gpt-4o",
        )

        # The Editor
        editor = Agent(
            agent_name="Editor",
            system_prompt="Review the blog post for tone, clarity, and SEO keywords. Provide the final polished version.",
            llm_name="gpt-4o",
        )

        # 3. Create the Workflow (The Collaboration)
        # SequentialWorkflow ensures Agent A finishes before Agent B starts
        workflow = SequentialWorkflow(
            agents=[researcher, writer, editor],
            max_loops=1
        )

        # 4. Run the Swarm
        st.write("🔍 Researcher is gathering data...")
        result = workflow.run(topic)
        
        status.update(label="Content Generated!", state="complete", expanded=False)

    # 5. Display the final result
    st.subheader("Final Polished Article")
    st.markdown(result)
    
    st.success("Collaborative Swarm Task Completed!")

# Note: To run this, you would need the 'swarms' library installed 
# and your OpenAi API Key configured in your environment.