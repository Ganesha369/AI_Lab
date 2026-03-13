import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# --- STREAMLIT UI ---
st.set_page_config(page_title="AI Web Researcher", layout="wide")
st.title("🌐 Multi-Agent Web Researcher")
st.markdown("Enter a topic, and an AI 'Newsroom' will research and write a report for you.")

topic = st.text_input("What do you want to research?", placeholder="e.g. The impact of Solid State Batteries on EVs")

if st.button("Start Research"):
    if not topic:
        st.error("Please enter a topic!")
    else:
        with st.status("Agents are working...", expanded=True) as status:
            # --- TOOLS ---
            search_tool = DuckDuckGoSearchRun()

            # --- AGENTS ---
            st.write("🤖 Creating Agents...")
            researcher = Agent(
                role='Senior Research Analyst',
                goal=f'Uncover cutting-edge developments in {topic}',
                backstory="""You are an expert researcher. You find the most relevant, 
                recent, and factual information. You provide raw data and sources.""",
                tools=[search_tool],
                verbose=True,
                allow_delegation=False
            )

            writer = Agent(
                role='Tech Content Strategist',
                goal=f'Craft a compelling report on {topic}',
                backstory="""You are a professional writer. You take complex research 
                and turn it into engaging, easy-to-read blog posts or reports.""",
                verbose=True,
                allow_delegation=False
            )

            # --- TASKS ---
            st.write("📝 Assigning Tasks...")
            task1 = Task(
                description=f"Analyze the latest trends and news about {topic}. Focus on breakthroughs and key players.",
                agent=researcher,
                expected_output="A bulleted list of the top 5 most important findings with sources."
            )

            task2 = Task(
                description=f"Using the researcher's findings, write a 3-paragraph summary suitable for a tech newsletter.",
                agent=writer,
                expected_output="A polished 3-paragraph report in Markdown format."
            )

            # --- THE CREW ---
            st.write("🚀 Running the Crew...")
            crew = Crew(
                agents=[researcher, writer],
                tasks=[task1, task2],
                process=Process.sequential # Researcher goes first, then Writer
            )

            result = crew.kickoff()
            status.update(label="Research Complete!", state="complete", expanded=False)

        # --- DISPLAY RESULT ---
        st.subheader("Final Report")
        st.markdown(result)
        st.success("Research concluded successfully.")

# Note: To run this, you must have an OPENAI_API_KEY set in your environment variables.