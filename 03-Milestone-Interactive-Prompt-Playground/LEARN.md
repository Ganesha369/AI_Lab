# Milestone 03: Building an Interactive Prompt Engineering Playground

In this milestone, we transition from static scripts to a dynamic, interactive playground. You will learn how to build a tool that allows you to experiment with System Prompts, hyper-parameters (like Temperature and Top-P), and different Prompt Engineering techniques in real-time. This environment is essential for "vibe-checking" models and fine-tuning instructions before deploying them into production workflows.

### The Importance of a Playground
Prompt engineering is an empirical science. Because LLMs are non-deterministic, small changes in wording or parameters can lead to vastly different outputs. An interactive playground allows you to:
1. **Iterate Rapidly:** Swap system instructions without restarting your application.
2. **Observe Parameter Impact:** See how 'Temperature' affects creativity vs. factual consistency.
3. **Test Few-Shot Learning:** Easily add examples to the prompt to guide the model's behavior.

### Key Components of the Playground
To build an effective playground, we focus on three main areas:

#### 1. The Configuration Sidebar
This is where we control the "engine" of the LLM. 
*   **Model Selection:** Choosing between models (e.g., GPT-3.5-Turbo, GPT-4o).
*   **Temperature:** Controls randomness. (0 = deterministic, 1 = creative).
*   **Max Tokens:** Limits the length of the response to manage costs and prevent rambling.

#### 2. The Instruction Layer (System Prompt)
The System Prompt sets the persona and the boundaries for the AI. In our playground, we keep this separate from the user input so we can test how changing the "Identity" of the AI changes the result of the same user question.

#### 3. The Input/Output Loop
We use a reactive framework (Streamlit) to handle the state. When the "Run" button is clicked, the application packages the System Prompt and User Prompt into a message array and sends it to the API.

### Prompting Techniques to Test
While using your playground, try these three patterns:
*   **Zero-Shot:** Direct instruction without examples.
*   **Few-Shot:** Provide 2-3 examples of the desired input/output format within the prompt.
*   **Chain of Thought:** Asking the model to "Think step-by-step" to improve reasoning.