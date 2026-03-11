import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Zero-to-Hero Academy", page_icon="🤖", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMarkdown h1 { color: #4285F4; font-family: 'Helvetica Neue', sans-serif; }
    .module-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4285F4;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_status_code=True)

# --- HEADER ---
st.title("🤖 AI Zero-to-Hero Academy")
st.caption("A Google-level curriculum taking you from absolute beginner to AI Architect.")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("📚 Curriculum Progress")

# Define the full curriculum (must match your Github Action list)
curriculum = [
    '01-Basics-What-is-an-LLM-and-Tokens', '02-Basics-Prompting-and-Temperature', 
    '03-Milestone-Interactive-Prompt-Playground', '04-API-Connecting-Python-to-Gemini', 
    '05-API-Structuring-JSON-Responses', '06-Milestone-Custom-AI-Chatbot', 
    '07-Memory-What-are-Embeddings-and-Vectors', '08-Memory-Building-a-Simple-Vector-Search', 
    '09-Milestone-Chat-With-Your-Data-RAG', '10-Agents-Function-Calling-Basics', 
    '11-Agents-Building-a-Web-Search-Tool', '12-Agents-Multi-Agent-Collaboration'
]

# Detect completed modules
completed = [t for t in curriculum if os.path.exists(t)]
progress = len(completed) / len(curriculum)

# Progress Bar
st.sidebar.progress(progress)
st.sidebar.write(f"Overall Progress: {int(progress*100)}%")

# Sidebar Menu
selected_module = st.sidebar.selectbox("Jump to Module:", ["🏠 Home"] + completed)

# --- MAIN CONTENT ---
if selected_module == "🏠 Home":
    st.subheader("Welcome to your AI Lab")
    st.write("This lab is updated daily by an autonomous AI agent.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"✅ Modules Completed: {len(completed)}")
    with col2:
        st.warning(f"🚀 Next Topic: {curriculum[len(completed)] if len(completed) < len(curriculum) else 'All Complete!'}")

    st.markdown("### 📖 Syllabus Overview")
    for topic in curriculum:
        status = "✅" if topic in completed else "⏳"
        st.markdown(f"<div class='module-card'>{status} <b>{topic.replace('-', ' ')}</b></div>", unsafe_allow_status_code=True)

else:
    # Logic to load the specific module's main.py
    st.button("⬅️ Back to Home", on_click=lambda: st.write("Navigating..."))
    try:
        path = os.path.join(selected_module, "main.py")
        exec(open(path).read())
    except Exception as e:
        st.error(f"Error loading module: {e}")
