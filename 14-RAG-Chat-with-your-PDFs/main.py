```python
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os

# 1. Setup UI
st.title("📄 Chat with your PDF (RAG)")
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())

    # 2. Load and Split Document
    loader = PyPDFLoader("temp.pdf")
    data = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)

    # 3. Create Embeddings and Vector Store (The "Filing Cabinet")
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(chunks, embeddings)

    # 4. Setup Chat Interface
    query = st.text_input("Ask a question about your PDF:")
    
    if query:
        # Create the RAG Chain
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_db.as_retriever()
        )
        
        response = qa_chain.invoke(query)
        st.write("### Answer:")
        st.write(response["result"])
else:
    st.info("Please upload a PDF and provide an API key to start.")
```