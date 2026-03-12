# To run this, install: pip install streamlit sentence-transformers
import streamlit as st
from sentence_transformers import SentenceTransformer, util
import torch

st.set_page_config(page_title="Simple Vector DB Demo")

st.title("🚀 Simple Vector Search Demo")
st.write("This app simulates how a Vector Database finds meaning instead of just keywords.")

# 1. Load a pre-trained model to turn text into "Vectors" (Numbers)
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# 2. Our "Database" of sentences
database_items = [
    "The golden retriever ran across the park.",
    "A scientist is discovering a new planet in space.",
    "The chef is cooking a delicious Italian pasta.",
    "The moon orbits the Earth every month.",
    "A puppy is playing with a ball in the grass.",
    "I love eating spicy noodles."
]

# 3. Pre-calculate vectors for our database (The 'Encoding' step)
db_vectors = model.encode(database_items, convert_to_tensor=True)

# UI Logic
user_query = st.text_input("Search for something (e.g., 'cosmos' or 'cute dog'):")

if user_query:
    # 4. Turn the user's query into a vector
    query_vector = model.encode(user_query, convert_to_tensor=True)
    
    # 5. Find the "Cosine Similarity" (The distance in our Magic Library)
    scores = util.cos_sim(query_vector, db_vectors)[0]
    
    # Get the top result
    top_results = torch.topk(scores, k=2)
    
    st.subheader("Results from 'Vector Memory':")
    
    for score, idx in zip(top_results[0], top_results[1]):
        st.info(f"**Match:** {database_items[idx]} \n\n(Similarity Score: {score:.4f})")

    st.write("---")
    st.write("*Notice that searching for 'cosmic' will find results about 'space' even if the word 'cosmic' isn't there!*")