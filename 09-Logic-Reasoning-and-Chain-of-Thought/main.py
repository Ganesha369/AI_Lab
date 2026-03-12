import streamlit as st
import openai

# Streamlit UI
st.set_page_config(page_title="Reasoning Lab", layout="centered")
st.title("🧠 Chain-of-Thought Reasoning Lab")
st.write("Compare how a 'Direct Answer' vs. 'Reasoning' changes the AI's output.")

# Sidebar for API Key
with st.sidebar:
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    st.info("This app demonstrates how CoT reduces logic errors.")

def get_ai_response(prompt, system_instruction):
    if not api_key:
        return "Please enter an API Key to see the logic in action!"
    
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# The Problem: A classic logic riddle
logic_problem = (
    "Sally has 3 brothers. Each of her brothers has 2 sisters. "
    "How many sisters does Sally have?"
)

st.subheader("The Logic Problem:")
st.info(logic_problem)

col1, col2 = st.columns(2)

with col1:
    if st.button("Get Direct Answer"):
        st.write("**Instruction:** Answer immediately.")
        # We purposely use a prompt that doesn't encourage thinking
        ans = get_ai_response(logic_problem, "Provide a one-sentence direct answer.")
        st.error(f"AI Result: {ans}")

with col2:
    if st.button("Get Reasoning Answer"):
        st.write("**Instruction:** Let's think step by step.")
        # We use Chain-of-Thought prompting
        ans = get_ai_response(logic_problem, "Think step by step to solve this logic puzzle. Show your reasoning.")
        st.success(f"AI Result: {ans}")

st.divider()
st.write("""
### Why does this matter?
Many LLMs might fail the 'Direct' approach (sometimes saying Sally has 6 sisters) because they predict the next word based on probability. 
By forcing **Reasoning**, the AI realizes:
1. Sally is a sister.
2. If her brothers have 2 sisters, those sisters are Sally and one other person.
3. Therefore, Sally has **1** sister.
""")