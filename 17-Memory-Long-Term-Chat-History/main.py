```python
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# --- CONFIGURATION ---
st.set_page_config(page_title="Long-Term Memory Bot", page_icon="🧠")
st.title("🧠 AI with Long-Term Memory")

# 1. Setup the "Filing Cabinet" (In-memory for this demo, 
# but in production, you'd link this to a real Database)
history = StreamlitChatMessageHistory(key="chat_messages")

# 2. Initialize the AI Model
llm = ChatOpenAI(api_key=st.sidebar.text_input("OpenAI API Key", type="password"))

# 3. Display the "Memory" from previous sessions
for msg in history.messages:
    st.chat_message(msg.type).write(msg.content)

# 4. Handle New Input
if prompt := st.chat_input("Tell me something you want me to remember..."):
    # Show user message
    st.chat_message("human").write(prompt)
    
    # AI Logic: It looks at 'history.messages' to understand context
    full_context = history.messages + [HumanMessage(content=prompt)]
    
    try:
        response = llm.invoke(full_context)
        
        # Save to Long-Term Memory
        history.add_user_message(prompt)
        history.add_ai_message(response.content)
        
        # Show AI message
        st.chat_message("ai").write(response.content)
    except Exception as e:
        st.error("Please enter a valid OpenAI API Key in the sidebar.")

# 5. Instructions for the Student
st.info("""
**Student Task:** 
1. Enter your API key.
2. Tell the AI: 'My favorite color is Blue.'
3. Refresh the page (Simulating coming back tomorrow).
4. Ask the AI: 'What is my favorite color?'
5. Notice how it remembers because the history is stored!
""")
```