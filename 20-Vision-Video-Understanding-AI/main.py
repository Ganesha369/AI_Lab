import streamlit as st
import cv2
import tempfile
from PIL import Image

# Note: In a real environment, you would use a model like Video-LLaVA or Gemini API.
# This code demonstrates the workflow: Upload -> Extract Frames -> Analyze.

st.set_page_config(page_title="Video Understanding AI AI Explorer")

st.title("📹 Video Understanding AI Explorer")
st.write("Upload a video to see how AI 'sees' motion through frames.")

uploaded_file = st.file_uploader("Choose a video file...", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save the uploaded video to a temporary file
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    # Open video using OpenCV
    video_caps = cv2.VideoCapture(tfile.name)
    
    st.subheader("Step 1: AI Frame Extraction")
    st.info("AI 'understands' video by sampling frames over time to detect motion.")

    col1, col2, col3 = st.columns(3)
    
    # Extract 3 sample frames (beginning, middle, end)
    total_frames = int(video_caps.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_to_show = [0, total_frames // 2, total_frames - 1]
    
    for i, frame_idx in enumerate(frames_to_show):
        video_caps.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = video_caps.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            if i == 0: col1.image(img, caption="Start (0s)")
            if i == 1: col2.image(img, caption="Middle (Action)")
            if i == 2: col3.image(img, caption="End (Result)")

    st.subheader("Step 2: AI Logical Reasoning (Simulated)")
    st.success("""
    **AI Analysis Report:**
    - **Objects Detected:** Person, Football, Grass.
    - **Action Recognized:** 'Kicking'.
    - **Temporal Understanding:** The ball moved from the ground toward the goal.
    - **Conclusion:** The video shows a successful penalty kick.
    """)
    
    st.video(uploaded_file)
else:
    st.info("Please upload a video to begin the lesson.")