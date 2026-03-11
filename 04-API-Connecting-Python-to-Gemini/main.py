import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. SETUP: Load your secret API key from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. CONFIGURATION: Tell the library which key to use
genai.configure(api_key=api_key)

# 3. INITIALIZE MODEL: We are using Gemini 1.5 Pro (the smart one!)
model = genai.GenerativeModel('gemini-1.5-pro')

# 4. STREAMLIT UI: Create the "Face" of the app
st.set_page_config(page_title="Gemini AI Explorer", page_icon="🤖")
st.title("🤖 Gemini AI Connector")
st.write("Type a prompt below to chat with Google's most advanced AI.")

# Create a text input box for the user
user_prompt = st.text_input("What would you like to ask?", placeholder="e.g., Explain quantum physics like I'm five.")

# Create a button to trigger the AI
if st.button("Generate Response"):
    if user_prompt:
        with st.spinner("Wait for it... the AI is thinking... 🧠"):
            try:
                # 5. THE MAGIC: Send the prompt to Gemini
                response = model.generate_content(user_prompt)
                
                # 6. DISPLAY: Show the result to the user
                st.subheader("The AI says:")
                st.write(response.text)
                
                # Bonus: Show success message
                st.success("Successfully connected to Gemini API!")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt first!")

# Instructions to run:
# Save this file as app.py
# In your terminal, type: streamlit run app.py