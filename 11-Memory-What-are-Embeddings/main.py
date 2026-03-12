# First, pip install streamlit sentence-transformers
import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Load a simple, lightweight model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

st.title("🧠 The Embedding Visualizer")
st.write("See how AI understands the 'closeness' of meanings!")

# User inputs
word1 = st.text_input("Enter first sentence:", "The cat is sleeping")
word2 = st.text_input("Enter second sentence:", "A kitten is taking a nap")

if st.button("Calculate Similarity"):
    # 1. Convert sentences into Embeddings (Lists of numbers)
    emb1 = model.encode(word1, convert_to_tensor=True)
    emb2 = model.encode(word2, convert_to_tensor=True)
    
    # 2. Compare how close they are (Cosine Similarity)
    cosine_scores = util.cos_sim(emb1, emb2)
    score = cosine_scores.item()
    
    st.subheader(f"Similarity Score: {score:.4f}")
    
    # Logic to explain the score
    if score > 0.7:
        st.success("These are very similar in meaning!")
    elif score > 0.3:
        st.warning("These are somewhat related.")
    else:
        st.error("These have totally different meanings.")

    # Show what an embedding actually looks like (the first 10 numbers)
    st.write("### What the AI sees (First 10 dimensions of Sentence 1):")
    st.code(emb1.tolist()[:10])