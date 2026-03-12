# 21-Agents: Function Calling Basics

Summary: In this lesson, you will learn the "bridge" between thinking and doing. While Large Language Models (LLMs) are incredibly smart at talking, they are "locked in a room" with no access to the outside world. **Function Calling** is the mechanism that gives the LLM "hands," allowing it to interact with databases, APIs, and software tools to perform real-world tasks.

### [🚀 CHECK LIVE RESULT](https://ganesha-ai-lab.streamlit.app/?path=21-Agents-Function-Calling-Basics)

---

### 1. The Simple Analogy: The General Contractor
Imagine you hire a **General Contractor** to renovate your house. 
*   **The Contractor (LLM):** Knows exactly how a house should look and what steps are needed. However, the contractor doesn't personally carry a pipe wrench or a saw. 
*   **The Sub-Contractors (Functions/Tools):** The contractor has a directory of specialists (Plumber, Electrician).
*   **Function Calling:** When you say, "My sink is leaking," the Contractor doesn't just talk about leaks; they identify that they need the "Fix Leak" tool, call the Plumber with the specific address, and then report back to you once the job is done.

### 2. Real-World Example: Netflix Support Bot
Imagine you are chatting with **Netflix Customer Support**.
*   **Without Function Calling:** You ask, "When does my subscription expire?" The bot might say, "You can check your settings page to find out." (Helpful, but lazy).
*   **With Function Calling:** 
    1.  The LLM recognizes you are asking about your account.
    2.  It triggers a function called `get_subscription_details(user_id="123")`.
    3.  The database returns "Expires Oct 2025."
    4.  The bot says, "Your subscription is active until October 2025!" 

**Google** uses this same logic with **Google Assistant**. When you say "Set an alarm," the LLM doesn't just say "Okay, I'll remember that"; it calls a specific system function to actually toggle the clock app on your phone.

### 3. The Workflow (The 4-Step Loop)
1.  **User Prompt:** "What is the status of order #99?"
2.  **LLM Decision:** The LLM sees the prompt and realizes it has a tool named `check_order_status`. It outputs a JSON object: `{ "function": "check_order_status", "order_id": "99" }`.
3.  **Local Execution:** Your code (not the LLM) runs that function and gets the result from your database: `"Shipped"`.
4.  **Final Response:** The LLM takes that result and tells the user: "Good news! Your order #99 has been shipped."

### 4. Tools Used
*   **OpenAI/Anthropic API:** The "Brain" that decides which tool to use.
*   **JSON:** The language used to pass data between the brain and the tools.
*   **Pydantic:** A Python library often used to strictly define what the "tools" look like so the LLM doesn't get confused.

### 💻 Full Source Code
