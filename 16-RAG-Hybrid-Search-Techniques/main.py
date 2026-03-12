```python
import streamlit as st
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers import EnsembleRetriever
from langchain_core.documents import Document
import os

# Streamlit UI
st.title("🚀 Hybrid Search Explorer")
st.write("Combining Keyword (BM25) + Semantic (Vector) Search")

# 1. Setup Sample Data
docs = [
    Document(page_content="The iPhone 15 has a titanium body and USB-C.", metadata={"id": 1}),
    Document(page_content="Apple's latest smartphone features a great camera.", metadata={"id": 2}),
    Document(page_content="The MacBook Pro uses the M3 chip for high performance.", metadata={"id": 3}),
    Document(page_content="The Galaxy S23 is a flagship Android phone.", metadata={"id": 4}),
]

# 2. Initialize Retrievers
# Note: You'll need an OPENAI_API_KEY in your environment
if "OPENAI_API_KEY" in os.environ:
    # A. Keyword Retriever (BM25)
    keyword_retriever = BM25Retriever.from_documents(docs)
    keyword_retriever.k = 2

    # B. Semantic Retriever (Vector)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    semantic_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # C. Hybrid Retriever (Ensemble)
    # weights=[0.5, 0.5] means we trust both methods equally
    hybrid_retriever = EnsembleRetriever(
        retrievers=[keyword_retriever, semantic_retriever], 
        weights=[0.5, 0.5]
    )

    # User Input
    query = st.text_input("Search for something (e.g., 'USB-C' or 'latest phone'):")

    if query:
        st.subheader("Results")
        results = hybrid_retriever.invoke(query)
        
        for i, doc in enumerate(results):
            st.info(f"Result {i+1}: {doc.page_content}")
            
        st.success("Hybrid search successfully merged keyword and semantic matches!")
else:
    st.warning("Please set your OPENAI_API_KEY to run the live demo.")

```