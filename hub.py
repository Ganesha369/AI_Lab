import streamlit as st
import os
import importlib.util

# 1. Setup the Page Configuration
st.set_page_config(
    page_title="AI Zero-to-Hero Academy", 
    page_icon="🤖", 
    layout="wide"
)

# 2. Get the specific project path from the URL (e.g., ?path=01-Basics.../main.py)
query_params = st.query_params
target_path = query_params.get("path")

# 3. Sidebar Navigation
with st.sidebar:
    st.title("🤖 AI Academy Hub")
    if target_path:
        if st.button("🏠 Back to Main Menu"):
            st.query_params.clear()
            st.rerun()
    st.markdown("---")
    st.markdown("*A Google-level curriculum taking you from absolute beginner to AI Architect.*")

# 4. Logic to run the selected project OR show the Homepage
if target_path and os.path.exists(target_path):
    # If the URL has a path, dynamically load and run that specific main.py
    module_name = target_path.replace("/", "_").replace(".py", "")
    spec = importlib.util.spec_from_file_location(module_name, target_path)
    module = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        st.error(f"⚠️ Error running the AI app: {e}")
        st.info("The AI might have generated a bug. Check the code in the repository!")

else:
    # 5. The Homepage (Shown if no specific link was clicked)
    st.title("🎓 AI Zero-to-Hero Academy: Live Playground")
    st.markdown("> Welcome! When you click a [🚀 RUN LIVE ON STREAMLIT] link in the GitHub README, the AI app will load here automatically.")
    st.markdown("---")
    
    st.subheader("📚 Available AI Applications")
    
    # Dynamically scan the repository for completed modules
    folders = [f for f in sorted(os.listdir('.')) if os.path.isdir(f) and not f.startswith('.')]
    apps_found = False
    
    for folder in folders:
        if os.path.exists(f"{folder}/main.py"):
            apps_found = True
            display_name = folder.replace("-", " ")
            
            # Create a card-like layout for each app
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"{display_name}")
            with col2:
                if st.button("Launch App 🚀", key=folder):
                    st.query_params["path"] = f"{folder}/main.py"
                    st.rerun()
            st.markdown("---")
            
    if not apps_found:
        st.info("⏳ The AI Professor is building the first module. Check back soon!")
