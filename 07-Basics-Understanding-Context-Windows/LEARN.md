# 07: Basics - Understanding Context Windows

Summary: Learn about the "memory limit" of Large Language Models (LLMs). We explore the Context Window—the specific amount of information an AI can process in a single go—using the analogy of a workspace and a real-world look at how Google handles massive data.

### [🚀 CHECK LIVE RESULT](https://ganesha-ai-lab.streamlit.app/?path=07-Basics-Understanding-Context-Windows)

---

### 1. The Simple Analogy: The "Student's Desk"
Imagine you are writing a research paper. Your **Context Window** is the size of your desk.
*   **Small Desk:** You can only have one page open at a time. If you need to look at Page 10, you have to put Page 1 away. You might forget what was on Page 1 while reading Page 10.
*   **Huge Desk:** You can spread out 500 pages, a map, and three books. You can see the connections between all of them at once.

In AI terms, the "desk space" is measured in **Tokens** (words or parts of words). If a conversation gets too long and exceeds the context window, the AI "forgets" the beginning of the chat.

### 2. Real-World Example: Google Gemini
**Google** recently made waves by expanding the context window of their model, **Gemini 1.5 Pro**, to over **1 million tokens**. 

*   **How they use it:** A developer can upload an entire codebase (thousands of files), or a filmmaker can upload an hour-long video. Because the context window is so large, the AI can "remember" a tiny detail from the 2nd minute of the video while answering a question at the 59th minute.
*   **The Benefit:** Without a large window, you'd have to cut the video into small pieces, and the AI would lose the "big picture."

### 3. Key Tools Used
*   **Tokens:** The units of measurement (roughly 0.75 words per token).
*   **Tiktoken:** A library by OpenAI used to count exactly how many tokens are in a string of text.
*   **RAG (Retrieval Augmented Generation):** A technique used when your data is *bigger* than the context window. It acts like a filing cabinet next to your desk where you only pull out what you need.

### 4. Why should you care?
If you give an AI a 100-page PDF but its context window is only 10 pages long, it will only "read" the last 10 pages and ignore the rest, or it will hallucinate (make things up) to fill the gaps.

### 💻 Full Source Code
