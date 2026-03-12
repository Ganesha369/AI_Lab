import streamlit as st
import base64
import requests

# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

st.set_page_config(page_title="AI Vision Analyst", layout="wide")
st.title("👁️ AI Vision: Image & Chart Analyst")
st.write("Upload an image or a chart, and let AI explain what it sees.")

# User Inputs
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
user_question = st.text_input("What do you want to know about this image?", "Summarize the key findings in this image.")

if uploaded_file is not None and api_key:
    # Display the image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    if st.button("Analyze Image"):
        base64_image = encode_image(uploaded_file)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # The payload structure for GPT-4o (Vision)
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_question},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 500
        }

        with st.spinner('The Digital Detective is investigating...'):
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                st.subheader("Analysis Results:")
                st.write(result['choices'][0]['message']['content'])
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

elif not api_key:
    st.info("Please enter your OpenAI API key in the sidebar to begin.")