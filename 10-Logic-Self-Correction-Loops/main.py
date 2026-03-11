import streamlit as st
import time

def self_correction_simulation():
    st.title("🔄 The 10-Logic-Loop Simulator")
    st.write("Goal: The AI must generate a sentence exactly **5 words long**.")
    
    target_length = 5
    max_loops = 10
    
    # Mock 'AI' responses that simulate errors and eventual success
    mock_responses = [
        "This is a very long sentence.", # 6 words
        "Hello world.",                  # 2 words
        "I am an AI assistant bot.",    # 5 words (Success!)
    ]
    
    if st.button("Start Logic Loop"):
        current_attempt = 1
        success = False
        
        while current_attempt <= max_loops:
            st.subheader(f"Attempt {current_attempt}:")
            
            # Simulate AI thinking
            with st.spinner("AI is thinking..."):
                time.sleep(1)
                # In a real app, this would be an LLM call
                # We cycle through mock responses for demo purposes
                output = mock_responses[min(current_attempt-1, len(mock_responses)-1)]
            
            word_count = len(output.split())
            st.write(f"**Output:** '{output}'")
            st.write(f"**Check:** {word_count} words found.")
            
            # THE LOGIC CHECK
            if word_count == target_length:
                st.success(f"✅ Logic Corrected! Achieved in {current_attempt} loops.")
                success = True
                break
            else:
                st.error(f"❌ Failed logic check. Retrying...")
                current_attempt += 1
                time.sleep(0.5)
        
        if not success:
            st.warning("Reached 10-loop limit without perfect logic.")

if __name__ == "__main__":
    self_correction_simulation()