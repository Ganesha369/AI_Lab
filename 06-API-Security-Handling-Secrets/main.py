import streamlit as st
import os

# --- INSTRUCTIONS ---
# To run this locally, create a folder named '.streamlit' 
# inside your project folder. Create a file named 'secrets.toml' inside it.
# Add this line to that file:
# MY_API_KEY = "super-secret-key-12345"
# --------------------

st.title("🔐 Secure API Key Handler")

st.write("""
This app demonstrates how to access a 'Secret' without showing it in the code.
In a real app, we would use this key to call an API like OpenAI or Google Maps.
""")

# Accessing the secret safely
try:
    # In Streamlit, st.secrets is the standard way to handle keys
    api_key = st.secrets["MY_API_KEY"]
    
    st.success("Successfully found the API Key in the 'Vault'!")
    
    # Demonstration of "Masking" - Never show the full key to the user!
    masked_key = api_key[:4] + "********" + api_key[-2:]
    
    st.info(f"The key we are using is: `{masked_key}`")
    
    st.warning("Notice: The actual code says `st.secrets['MY_API_KEY']`. The real value is hidden!")

except FileNotFoundError:
    st.error("Error: I couldn't find your secrets file! Create `.streamlit/secrets.toml` to fix this.")
except KeyError:
    st.error("Error: The key 'MY_API_KEY' is missing from your secrets.")

# Comparison UI
st.divider()
st.subheader("Comparison")
col1, col2 = st.columns(2)

with col1:
    st.error("❌ Bad Practice (Hardcoded)")
    st.code("""
# This is dangerous!
api_key = "sk-1234567890abcdef"
    """)

with col2:
    st.success("✅ Good Practice (Secrets)")
    st.code("""
# This is safe!
api_key = st.secrets["MY_API_KEY"]
    """)