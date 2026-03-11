import streamlit as st
import tiktoken

# Streamlit UI Setup
st.set_page_config(page_title="Context Window Visualizer", layout="centered")

st.title("🪟 Context Window Visualizer")
st.write("""
    Every LLM has a limit. This tool helps you visualize how much 
    'space' your text takes up in a model's memory.
""")

# Sidebar settings
model_choice = st.sidebar.selectbox("Select Model Window Limit", 
                                    ["GPT-3.5 (4,096 tokens)", 
                                     "GPT-4 (8,192 tokens)", 
                                     "Gemini 1.5 (1,000,000 tokens)"])

# Define limits based on selection
limits = {
    "GPT-3.5 (4,096 tokens)": 4096,
    "GPT-4 (8,192 tokens)": 8192,
    "Gemini 1.5 (1,000,000 tokens)": 1000000
}
max_tokens = limits[model_choice]

# Input Text
user_text = st.text_area("Paste your long document or prompt here:", height=300, 
                         placeholder="Type or paste something long...")

# Logic to count tokens
def count_tokens(text):
    # Using the cl100k_base encoding (used by GPT-4)
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

if user_text:
    token_count = count_tokens(user_text)
    usage_pct = min((token_count / max_tokens), 1.0)

    # Display Stats
    st.subheader("Results")
    col1, col2 = st.columns(2)
    col1.metric("Tokens Used", f"{token_count:,}")
    col2.metric("Remaining Space", f"{max_tokens - token_count:,}")

    # Visual Progress Bar
    st.write(f"**Context Window Usage: {usage_pct:.2%}**")
    if token_count > max_tokens:
        st.error("⚠️ Over Limit! The AI will forget the beginning of this text.")
        st.progress(1.0)
    else:
        st.success("✅ Fits comfortably within the context window.")
        st.progress(usage_pct)

    # Explanation for students
    with st.expander("What does this mean?"):
        st.write(f"""
        You are using the **cl100k_base** tokenizer. 
        Your text is approximately **{token_count}** units of 'AI memory'. 
        If this bar reaches 100%, the model will start 'truncating' (cutting off) 
        the earliest parts of your conversation to make room for new info.
        """)
else:
    st.info("Enter some text above to see the token count.")