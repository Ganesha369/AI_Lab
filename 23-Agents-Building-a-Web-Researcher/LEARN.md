# Building a Multi-Agent Web Researcher

Summary: Learn how to build an automated research team using AI agents. This lesson covers how multiple specialized agents (Searcher and Writer) collaborate to browse the internet, synthesize information, and create comprehensive reports using CrewAI and Streamlit.

### [🚀 CHECK LIVE RESULT](https://ganesha-ai-lab.streamlit.app/?path=23-Agents-Building-a-Web-Researcher)

---

### 1. The Simple Analogy: The Newsroom
Imagine you are the Editor-in-Chief of a newspaper. To write a story about "The Future of Mars Colonization," you don't do everything yourself. You hire two people:
*   **The Researcher:** Goes to the library, interviews experts, and gathers stacks of raw notes.
*   **The Writer:** Takes those messy notes and turns them into a polished, easy-to-read article.
*   **The Manager (You):** Gives the initial topic and reviews the final result.

Building a **Web Researcher** works exactly like this newsroom, but the "people" are AI agents.

### 2. Real-World Example: Netflix Content Strategy
How does **Netflix** decide which shows to produce in different countries? 
Instead of one person manually googling "What is popular in South Korea?", they use automated systems (similar to our Web Researcher) to:
1.  Scan social media trends and local news (Research Agent).
2.  Analyze competitor viewership data (Analyst Agent).
3.  Synthesize a report for executives to greenlight a new show like *Squid Game* (Reporting Agent).

### 3. The Tools of the Trade
To build this, we use three main components:
*   **CrewAI:** The "Manager" that orchestrates the agents and tells them when to talk to each other.
*   **Tavily/DuckDuckGo:** The "Eyes" of the agent, allowing it to actually browse the live web.
*   **Streamlit:** The "TV Screen" where we build the user interface so anyone can use our tool.
*   **LLM (OpenAI/Groq/Claude):** The "Brain" that powers the logic of each agent.

### 4. Why Use "Agents" Instead of a Single Prompt?
If you ask a standard AI "Research X," it might hallucinate or give a surface-level answer. By splitting it into agents:
*   The **Researcher** is forced to find facts.
*   The **Writer** is forced to focus on grammar and flow.
*   This "division of labor" results in much higher quality work.

### 💻 Full Source Code
