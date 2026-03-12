```python
# First, install the requirements:
# pip install streamlit langchain langchain-community sentence-transformers faiss-cpu

import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# --- APP INTERFACE ---
st.set_page_config(page_title="AI Memory Lab", page_icon="🧠")
st.title("🧠 Similarity Search Lab")
st.write("This app finds the most 'meaningfully similar' sentence using Vector Embeddings.")

# --- STEP 1: PREPARE DATA ---
# This acts as our "Knowledge Base" or "Memory"
knowledge_base = [
    "The golden retriever ran across the park.",
    "A cat is sleeping on the window sill.",
    "The tech giant released a new smartphone today.",
    "Deep learning models require powerful GPUs.",
    "I enjoy eating fresh green apples in the morning.",
    "Space exploration is the future of humanity."
]

# --- STEP 2: LOAD EMBEDDING MODEL ---
# We use a free, local model to turn text into numbers
@st.cache_resource
def load_model():
    # This model 'understands' English sentence meanings
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

embedding_model = load_model()

# --- STEP 3: CREATE VECTOR STORE (THE MEMORY) ---
# We "store" our knowledge base in FAISS (a vector database)
vector_db = FAISS.from_texts(knowledge_base, embedding_model)

# --- STEP 4: USER INTERFACE FOR SEARCH ---
query = st.text_input("Type something to search (e.g., 'tell me about pets' or 'new phones'):")

if query:
    # Perform the similarity search
    # k=2 means "find the top 2 closest matches"
    results = vector_db.similarity_search(query, k=2)
    
    st.subheader("Top Matches found in 'Memory':")
    for i, doc in enumerate(results):
        st.success(f"Match {i+1}: {doc.page_content}")

    st.info("💡 Notice: It finds matches even if the exact words don't exist in the memory!")

# --- VISUAL EXPLANATION ---
with st.expander("See how this works behind the scenes"):
    st.write("""
    1. **Embeddings:** Your query was turned into a vector (a list of 384 numbers).
    2. **Math:** The app calculated the 'Cosine Similarity' (distance) between your query vector and the vectors in our list.
    3. **Retrieval:** It returned the items with the smallest distance.
    """)
```