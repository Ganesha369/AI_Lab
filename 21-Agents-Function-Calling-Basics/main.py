import streamlit as st
import json

# --- MOCK TOOL FUNCTIONS ---
def get_netflix_subscription_status(email):
    """Simulates a database lookup for a Netflix account."""
    database = {
        "alice@example.com": {"plan": "Premium", "status": "Active", "expiry": "2025-12-01"},
        "bob@example.com": {"plan": "Basic", "status": "Canceled", "expiry": "Expired"}
    }
    return database.get(email, "Account not found.")

# --- STREAMLIT UI ---
st.set_page_config(page_title="AI Agent: Function Calling", page_icon="🤖")
st.title("🍿 Netflix Support Agent")
st.write("This agent simulates 'Function Calling' to check account status.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask about an account (e.g., status for alice@example.com)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- SIMULATED AGENT LOGIC ---
    with st.chat_message("assistant"):
        # 1. Logic to "Detect" if the user provided an email
        if "alice@example.com" in prompt.lower():
            target_email = "alice@example.com"
            
            # 2. Simulate the 'Function Call'
            st.info(f"DEBUG: LLM calling function `get_netflix_subscription_status` for {target_email}")
            result = get_netflix_subscription_status(target_email)
            
            # 3. Final Answer
            response = f"I've checked the system. Alice, your {result['plan']} plan is currently {result['status']} until {result['expiry']}."
        
        elif "bob@example.com" in prompt.lower():
            target_email = "bob@example.com"
            st.info(f"DEBUG: LLM calling function `get_netflix_subscription_status` for {target_email}")
            result = get_netflix_subscription_status(target_email)
            response = f"I see here that Bob's account is {result['status']}. Would you like to reactivate it?"
            
        else:
            response = "I can help you with your Netflix account. Please provide your email address so I can look up your details."

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar explanation
st.sidebar.header("How it works")
st.sidebar.write("""
1. **The Tool:** A Python function that looks up data.
2. **The Identification:** The Agent parses your text for an email.
3. **The Call:** The Agent 'calls' the function to get real data.
4. **The Response:** The Agent turns raw data into a friendly message.
""")