# Personal Knowledge Brain - Basic Streamlit App
# This code creates a simple interface to "teach" your AI and ask it questions.

import streamlit as st
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

# 1. Setup the UI
st.set_page_config(page_title="My AI Second Brain")
st.title("🧠 Milestone 18: Personal Knowledge Brain")
st.write("Upload your knowledge and chat with your memory.")

# 2. Sidebar for API Key
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if api_key:
    # 3. Knowledge Input
    user_data = st.text_area("Paste your notes or facts here:", 
                             placeholder="e.g., My favorite color is blue and I started learning Python in 2023.")
    
    if st.button("Store in Brain"):
        st.success("Information stored in the 'Memory Vault'!")

    # 4. The RAG (Retrieval-Augmented Generation) Logic
    query = st.text_input("Ask your Brain a question:")

    if query and user_data:
        # Create a simple vector store from the text provided
        # In a real app, we would use ChromaDB to save this to a hard drive
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        
        # Simulating a database search
        # We treat the text area as our 'knowledge base'
        context = user_data 
        
        # Define the AI's personality
        template = """Answer the question based only on the following context:
        {context}
        
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        model = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")
        
        # Build the chain
        chain = (
            {"context": lambda x: context, "question": RunnablePassthrough()}
            | prompt
            | model
            | StrOutputParser()
        )
        
        # 5. Output the result
        response = chain.invoke(query)
        st.info(f"Answer: {response}")

else:
    st.warning("Please enter your OpenAI API Key in the sidebar to begin.")

# To run this:
# 1. Install requirements: pip install streamlit langchain langchain-openai
# 2. Run command: streamlit run your_file_name.py