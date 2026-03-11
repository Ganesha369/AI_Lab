import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Zero-to-Hero Academy", page_icon="🤖", layout="wide")

# --- FIXED CSS FOR PROFESSIONAL LOOK ---
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
    .beginner-note {
        background-color: #1e2130;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #4285F4;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True) # FIXED: Changed status_code to html

# --- HEADER ---
st.title("🤖 AI Zero-to-Hero Academy")
st.caption("A beginner-to-architect journey through modern Artificial Intelligence.")

# --- SIDEBAR NAVIGATION ---
curriculum = [
    '01-Basics-What-is-an-LLM-and-Tokens', '02-Basics-Prompting-and-Temperature', 
    '03-Milestone-Interactive-Prompt-Playground', '04-API-Connecting-Python-to-Gemini', 
    '05-API-Structuring-JSON-Responses', '06-Milestone-Custom-AI-Chatbot', 
    '07-Memory-What-are-Embeddings-and-Vectors', '08-Memory-Building-a-Simple-Vector-Search', 
    '09-Milestone-Chat-With-Your-Data-RAG', '10-Agents-Function-Calling-Basics', 
    '11-Agents-Building-a-Web-Search-Tool', '12-Agents-Multi-Agent-Collaboration'
]

completed = [t for t in curriculum if os.path.exists(t)]
progress = len(completed) / len(curriculum)

st.sidebar.header("📊 Your Progress")
st.sidebar.progress(progress)
selected_module = st.sidebar.selectbox("Go to Lesson:", ["🏠 Home Dashboard"] + completed)

# --- CONTENT ---
if selected_module == "🏠 Home Dashboard":
    st.subheader("Welcome to the Lab, Future Architect!")
    st.markdown("""
    This lab is a Living Project. Every day, an AI agent generates new lessons. 
    If you're a beginner, don't worry—every lesson includes:
    * 💡 Analogy-first explanations.
    * 🛠️ Library tooltips (we explain why we use specific code).
    * 🚀 Interactive playgrounds to test the concepts.
    """)
    
    st.write("---")
    st.markdown("### 📚 Your Syllabus Status")
    for topic in curriculum:
        status = "✅" if topic in completed else "⏳"
        st.markdown(f"<div class='module-card'>{status} {topic.replace('-', ' ')}</div>", unsafe_allow_html=True)

else:
    # BEGINNER FRIENDLY TOOLBAR
    st.sidebar.markdown("---")
    st.sidebar.info("💡 Beginner Tip: If the code below looks complex, check the 'LEARN.md' file in GitHub for the full story!")
    
    if st.button("⬅️ Back to Main Menu"):
        st.rerun()

    # LOADING THE PROJECT
    try:
        path = os.path.join(selected_module, "main.py")
        with open(path, encoding='utf-8') as f:
            code_content = f.read()
            # This executes the lesson code inside the Hub
            exec(code_content)
    except Exception as e:
        st.error(f"Error loading lesson: {e}")
