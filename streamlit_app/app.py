import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import os

# Title
st.set_page_config(page_title="Vehicle Detection & Counting - YOLOv8", layout="wide")
st.title("🚗 Vehicle Detection & Counting (YOLOv8)")
st.write("Upload a video or use webcam to detect and count vehicles in real-time.")

# Load YOLOv8 model
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")  # Small & fast model, good for Streamlit

model = load_model()

# Sidebar options
st.sidebar.header("⚙️ Settings")
conf_threshold = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)

# Choose input
source = st.radio("Select Input Source:", ["Upload Video", "Webcam"])

def process_frame(frame):
    results = model(frame, conf=conf_threshold)
    annotated_frame = results[0].plot()
    
    # Count vehicles (only car, bus, truck, motorbike IDs in COCO dataset)
    vehicle_ids = [2, 3, 5, 7]  
    vehicle_count = 0
    for box in results[0].boxes:
        if int(box.cls) in vehicle_ids:
            vehicle_count += 1

    return annotated_frame, vehicle_count

if source == "Upload Video":
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv"])
    if uploaded_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()
        count_placeholder = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed_frame, vehicle_count = process_frame(frame)

            stframe.image(processed_frame, channels="RGB")
            count_placeholder.markdown(f"### 🚦 Vehicles Detected: **{vehicle_count}**")

        cap.release()
        os.remove(tfile.name)

elif source == "Webcam":
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    count_placeholder = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        processed_frame, vehicle_count = process_frame(frame)

        stframe.image(processed_frame, channels="RGB")
        count_placeholder.markdown(f"### 🚦 Vehicles Detected: **{vehicle_count}**")

    cap.release()
