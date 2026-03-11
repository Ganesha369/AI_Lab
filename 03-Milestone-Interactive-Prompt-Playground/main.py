import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
# Ensure you have OPENAI_API_KEY in your environment variables
client = OpenAI()

st.set_page_config(page_title="AI Prompt Playground", layout="wide")

st.title("🧪 Milestone 03: Prompt Playground")
st.markdown("Experiment with system instructions and hyper-parameters in real-time.")

# --- Sidebar Configuration ---
with st.sidebar:
    st.header("Model Settings")
    model_choice = st.selectbox("Select Model", ["gpt-3.5-turbo", "gpt-4o"])
    temp = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
    max_tokens = st.number_input("Max Tokens", min_value=50, max_value=4000, value=500)
    
    st.divider()
    st.info("The System Prompt defines the AI's persona.")

# --- Main Interface ---
col1, col2 = st.columns(2)

with col1:
    system_message = st.text_area(
        "System Prompt (Instructions)", 
        value="You are a helpful assistant that explains complex topics simply.",
        height=150
    )
    
    user_message = st.text_area(
        "User Prompt (Query)", 
        placeholder="Explain quantum entanglement...",
        height=150
    )
    
    run_button = st.button("Generate Response", type="primary")

with col2:
    st.subheader("Model Output")
    if run_button:
        try:
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model=model_choice,
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": user_message}
                    ],
                    temperature=temp,
                    max_tokens=max_tokens
                )
                
                output_text = response.choices[0].message.content
                st.write(output_text)
                
                # Metadata display
                st.caption(f"Tokens used: {response.usage.total_tokens}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.write("Click 'Generate Response' to see the result.")

# How to run:
# 1. Install dependencies: pip install streamlit openai
# 2. Run command: streamlit run your_script_name.py