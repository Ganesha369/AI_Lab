import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Student Hub", page_icon="🎓", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 8px; border: 1px solid #4285F4; text-align: left; padding-left: 20px; }
    .stButton>button:hover { background-color: rgba(66, 133, 244, 0.1); }
    </style>
    """, unsafe_allow_html=True)

# 1. Capture Direct Link from URL
query_path = st.query_params.get("path", "🏠 Home")

# 2. Sync Session State with URL
if "page" not in st.session_state:
    st.session_state.page = query_path

# --- DATA ---
curriculum = ['01-Basics-What-is-an-LLM-and-Tokens', '02-Basics-Prompting-and-Temperature', '03-Milestone-Interactive-Prompt-Playground', '04-API-Connecting-Python-to-Gemini', '05-API-Structuring-JSON-Responses', '06-API-Security-Handling-Secrets', '07-Basics-Understanding-Context-Windows', '08-Milestone-The-Smart-Summarizer-App', '09-Logic-Reasoning-and-Chain-of-Thought', '10-Logic-Self-Correction-Loops', '11-Memory-What-are-Embeddings', '12-Memory-Vector-Databases-Explained', '13-Memory-Similarity-Search-Lab', '14-RAG-Chat-with-your-PDFs', '15-RAG-Web-Search-Integration', '16-RAG-Hybrid-Search-Techniques', '17-Memory-Long-Term-Chat-History', '18-Milestone-Personal-Knowledge-Brain', '19-Vision-Analyzing-Images-and-Charts', '20-Vision-Video-Understanding-AI', '21-Agents-Function-Calling-Basics', '22-Agents-Tools-Calculators-and-APIs', '23-Agents-Building-a-Web-Researcher', '24-Agents-Multi-Task-Orchestrator', '25-Agents-AI-Coding-Assistant', '26-Swarms-Manager-and-Worker-Agents', '27-Swarms-Collaborative-Content-Team', '28-Advanced-Fine-Tuning-Concepts', '29-Advanced-AI-Ethics-and-Safety', '30-Final-Capstone-The-Autonomous-Company']
completed = [t for t in curriculum if os.path.exists(t)]

# Sidebar Navigation
st.sidebar.title("🎓 Academy Menu")
sidebar_nav = st.sidebar.selectbox("Go to:", ["🏠 Home"] + completed, index=0 if st.session_state.page not in completed else completed.index(st.session_state.page)+1)

# Sync sidebar with main page
if sidebar_nav != st.session_state.page:
    st.session_state.page = sidebar_nav
    st.query_params["path"] = sidebar_nav
    st.rerun()

# --- CONTENT AREA ---
if st.session_state.page == "🏠 Home":
    st.title("Welcome to your AI Academy Lab")
    st.write("Each module is generated daily. Select a completed lesson to begin!")
    st.divider()
    
    # Render Dashboard Cards
    for topic in curriculum:
        is_done = topic in completed
        status = "✅" if is_done else "⏳"
        if is_done:
            if st.button(f"{status} {topic.replace('-', ' ')}", key=f"dash_{topic}"):
                st.session_state.page = topic
                st.query_params["path"] = topic
                st.rerun()
        else:
            st.button(f"{status} {topic.replace('-', ' ')} (Generating...)", disabled=True)

else:
    # RUN THE LESSON DIRECTLY IN THE CENTER
    st.markdown(f"## 🚀 Project: {st.session_state.page.replace('-', ' ')}")
    if st.button("🏠 Return to Syllabus"):
        st.session_state.page = "🏠 Home"
        st.query_params["path"] = "🏠 Home"
        st.rerun()
    
    st.divider()
    
    try:
        path = os.path.join(st.session_state.page, "main.py")
        with open(path, encoding='utf-8') as f:
            exec(f.read())
    except Exception as e:
        st.error(f"Execution Error: {e}")
