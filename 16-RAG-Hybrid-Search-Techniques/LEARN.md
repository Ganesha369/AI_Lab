# 16-RAG-Hybrid-Search-Techniques: The "Best of Both Worlds" Approach

Summary: Hybrid Search is a technique in Retrieval-Augmented Generation (RAG) that combines **Keyword Search** (looking for exact words) and **Semantic Search** (looking for meaning). This ensures that if a user searches for "The Dark Knight," the system finds the exact title AND understands they are looking for "Batman movies."

### [🚀 CHECK LIVE RESULT](https://ganesha-ai-lab.streamlit.app/?path=16-RAG-Hybrid-Search-Techniques)

---

### 1. The Analogy: The Library Search
Imagine you are in a massive library:
*   **Keyword Search (BM25):** You go to the computer and type "Harry Potter." The computer shows you every book with those exact words on the cover. It’s fast and precise, but if you type "Wizarding world," it might miss some books.
*   **Semantic Search (Vector):** You ask a librarian, "I want something about a boy attending a magic school." The librarian understands the *concept* and points you to Harry Potter, even though you didn't say the name.
*   **Hybrid Search:** You use both. You find the exact titles you know, and the librarian helps you find related concepts you missed.

### 2. Real-World Example: Netflix
When you search on Netflix:
*   **Keyword:** If you type "Stranger Things," Netflix uses keyword search to put that exact show at the top.
*   **Semantic:** If you type "scary 80s nostalgia," Netflix uses semantic search (vector embeddings) to suggest *Stranger Things*, *It*, or *Summer of 84*, even if those titles don't contain the word "nostalgia."
*   **Hybrid:** Netflix combines these results to ensure that if there is an exact match, you see it, but if you’re browsing by "vibe," you still get great results.

### 3. The Tools of the Trade
To build this, we use:
1.  **Vector Database:** (e.g., Pinecone, Weaviate, or FAISS) to store the "meaning" of text.
2.  **BM25 Algorithm:** A mathematical formula used to rank documents based on how often specific keywords appear.
3.  **Reciprocal Rank Fusion (RRF):** This is the "glue." It takes the list from Keyword search and the list from Semantic search and merges them into one master list.
4.  **LangChain:** The framework that connects our LLM to these search tools.

### 4. Why use Hybrid?
*   **Handle Acronyms:** Semantic search often struggles with weird industry acronyms (like "RAG" or "GPU"). Keyword search finds them easily.
*   **Handle Context:** Keyword search fails if the user uses synonyms. Semantic search excels there.

### 💻 Full Source Code
