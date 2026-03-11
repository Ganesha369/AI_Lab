import streamlit as st
from openai import OpenAI

# 1. Setup the Page Title
st.set_page_config(page_title="Smart Summarizer", page_icon="📝")
st.title("📝 The Smart Summarizer")
st.write("Paste a long article below and get a 3-bullet point summary instantly.")

# 2. Sidebar for API Key (Security)
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

# 3. User Input Area
text_to_summarize = st.text_area("Enter your long text here:", height=300)

# 4. The Summarization Logic
if st.button("Summarize Now"):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif not text_to_summarize:
        st.warning("Please paste some text first!")
    else:
        try:
            # Initialize the OpenAI Client
            client = OpenAI(api_key=openai_api_key)
            
            with st.spinner('Thinking...'):
                # Send the request to the AI
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes text into 3 concise bullet points."},
                        {"role": "user", "content": f"Summarize this: {text_to_summarize}"}
                    ]
                )
                
                # Show the result
                summary = response.choices[0].message.content
                st.subheader("The Bottom Line:")
                st.success(summary)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 5. Footer
st.caption("Built with Streamlit and OpenAI")