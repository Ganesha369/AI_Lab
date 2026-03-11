import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Zero-to-Hero Academy", page_icon="🤖", layout="wide")

# --- CUSTOM CSS (Glassmorphism & Alignment) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #1e2130; color: white; border: 1px solid #4285F4; }
    .stButton>button:hover { background-color: #4285F4; border: 1px solid white; }
    .module-card { background: #1e2130; padding: 20px; border-radius: 15px; border-left: 8px solid #4285F4; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- QUERY PARAMETER LOGIC (The "Direct Link" Feature) ---
# This looks at the URL (e.g., ?path=01-Basics) and opens it automatically
query_params = st.query_params
direct_path = query_params.get("path", "🏠 Home")

# Initialize Session State
if "current_page" not in st.session_state:
    st.session_state.current_page = direct_path

# --- DATA: THE 30-PROJECT ROADMAP ---
curriculum = [
    # Phase 1: Foundations
    '01-Basics-What-is-an-LLM-and-Tokens', '02-Basics-Prompting-and-Temperature', 
    '03-Milestone-Interactive-Prompt-Playground', '04-API-Connecting-Python-to-Gemini', 
    '05-API-Structuring-JSON-Responses', '06-API-Security-Handling-Secrets',
    '07-Basics-Understanding-Context-Windows', '08-Milestone-The-Smart-Summarizer-App',
    '09-Logic-Reasoning-and-Chain-of-Thought', '10-Logic-Self-Correction-Loops',
    # Phase 2: Memory & Knowledge (RAG)
    '11-Memory-What-are-Embeddings', '12-Memory-Vector-Databases-Explained',
    '13-Memory-Similarity-Search-Lab', '14-RAG-Chat-with-your-PDFs',
    '15-RAG-Web-Search-Integration', '16-RAG-Hybrid-Search-Techniques',
    '17-Memory-Long-Term-Chat-History', '18-Milestone-Personal-Knowledge-Brain',
    '19-Vision-Analyzing-Images-and-Charts', '20-Vision-Video-Understanding-AI',
    # Phase 3: Autonomous Agents & Swarms
    '21-Agents-Function-Calling-Basics', '22-Agents-Tools-Calculators-and-APIs',
    '23-Agents-Building-a-Web-Researcher', '24-Agents-Multi-Task-Orchestrator',
    '25-Agents-AI-Coding-Assistant', '26-Swarms-Manager-and-Worker-Agents',
    '27-Swarms-Collaborative-Content-Team', '28-Advanced-Fine-Tuning-Concepts',
    '29-Advanced-AI-Ethics-and-Safety', '30-Final-Capstone-The-Autonomous-Company'
]

completed = [t for t in curriculum if os.path.exists(t)]

# --- UI: SIDEBAR ---
st.sidebar.title("🤖 AI Academy")
st.sidebar.progress(len(completed)/len(curriculum))
nav = st.sidebar.selectbox("Navigate Menu", ["🏠 Home"] + completed, index=0 if st.session_state.current_page not in completed else completed.index(st.session_state.current_page)+1)

# Update state if sidebar changes
if nav != st.session_state.current_page:
    st.session_state.current_page = nav
    st.query_params["path"] = nav
    st.rerun()

# --- MAIN PAGE RENDERING ---
if st.session_state.current_page == "🏠 Home":
    st.title("Welcome to the Zero-to-Hero AI Academy")
    st.write("Click a module below to start learning. New projects are added daily!")
    
    # Display Syllabus in order
    for topic in curriculum:
        is_done = topic in completed
        status = "✅" if is_done else "⏳"
        if is_done:
            if st.button(f"{status} {topic.replace('-', ' ')}", key=f"btn_{topic}"):
                st.session_state.current_page = topic
                st.query_params["path"] = topic
                st.rerun()
        else:
            st.button(f"{status} {topic.replace('-', ' ')} (Locked)", disabled=True)

else:
    # --- AUTOMATIC RESULT VIEW ---
    st.markdown(f"## 🚀 Project: {st.session_state.current_page.replace('-', ' ')}")
    if st.button("⬅️ Back to Syllabus"):
        st.session_state.current_page = "🏠 Home"
        st.query_params["path"] = "🏠 Home"
        st.rerun()

# Run the lesson code directly in the center
    try:
        path = os.path.join(st.session_state.current_page, "main.py")
        with open(path, encoding='utf-8') as f:
            exec(f.read())
    except Exception as e:
        st.error(f"Execution Error: {e}")
