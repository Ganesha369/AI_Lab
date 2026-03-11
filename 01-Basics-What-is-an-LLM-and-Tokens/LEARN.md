# 01-Basics: Large Language Models (LLMs) and the Tokenization Primitive

This module establishes the foundational mental model for Generative AI. We transition from viewing AI as a "magic box" to understanding it as a high-dimensional probabilistic engine. We cover the transition from characters to sub-word tokens and why this architectural choice dictates the intelligence, cost, and latency of systems like Gemini or GPT-4.

[🚀 RUN LIVE ON STREAMLIT](https://ganesha-ai-lab.streamlit.app/?path=01-Basics-What-is-an-LLM-and-Tokens/main.py)

---

### Level 0: The Intuition (The Supercharged Autocomplete)
At its simplest level, an LLM is a **statistical prediction engine**. If you type "The capital of France is," the model doesn't "know" geography in the way humans do; it calculates that in its massive training dataset, the word "Paris" statistically follows that sequence with the highest probability. It is "autocomplete" trained on the scale of the entire internet.

### Level 1: The Token (The Atomic Unit)
Computers cannot process strings like "Hello." They process numbers. To bridge this gap, we use **Tokens**. 
*   A token is not always a word. It can be a part of a word (sub-word), a single character, or punctuation.
*   **Rule of thumb:** In English, 1,000 tokens is roughly equivalent to 750 words.
*   **The Vocabulary:** Every model has a fixed "dictionary" (e.g., 32,000 or 128,000 unique tokens). If a word isn't in the dictionary, it is broken down into smaller pieces.

### Level 2: Sub-word Tokenization (BPE & SentencePiece)
Why don't we just use words?
1.  **Vocabulary Explosion:** There are millions of words. Storing a unique ID for every word is inefficient.
2.  **The "Out of Vocabulary" Problem:** If the model sees "Hyper-specialization" and only knows "Hyper" and "Specialization," it can still understand the meaning.

Modern LLMs use **Byte-Pair Encoding (BPE)** or **SentencePiece**. This algorithm identifies the most common sequences of characters and merges them into a single token. 
*   *Example:* "smart" might be 1 token. "smartest" might be 2 tokens: `["smart", "est"]`.

### Level 3: From Tokens to Vectors (Embeddings)
Once text is turned into Token IDs (integers), they are converted into **Embeddings**.
*   An embedding is a high-dimensional vector (a list of numbers, e.g., 768 or 4096 dimensions).
*   In this "Latent Space," tokens with similar meanings are mathematically close to each other. "King" and "Queen" will have vectors that point in similar directions, while "King" and "Apple" will be far apart.

### Level 4: The Staff Engineer's Perspective (Constraints & Cost)
As an engineer, you must care about three things regarding tokens:
1.  **Context Window:** Models have a hard limit on the total tokens they can "see" at once (e.g., Gemini's 2M context). This is a memory constraint ($O(n^2)$ complexity in standard attention).
2.  **Cost:** Most APIs charge per 1M tokens. Inefficient prompting increases costs.
3.  **Information Density:** Different languages have different tokenization efficiencies. English is usually token-efficient; Kanji or Cyrillic often requires more tokens per concept, making those queries more expensive and slower.