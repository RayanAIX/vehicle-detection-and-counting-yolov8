# 🚗 Vehicle Detection & Counting (YOLOv8)

This computer vision project detects and counts vehicles from traffic videos in real time using **YOLOv8** and **OpenCV**. It identifies cars, motorcycles, buses, and trucks, displaying the count per frame and saving an annotated output video. This system can be used for traffic monitoring, smart city projects, and transportation research.

---

## 🎥 Input vs Output Video

### 🔹 Original Input Video  
<video src="https://github.com/user-attachments/assets/YOUR_INPUT_VIDEO_ID" width="400" controls></video>

### 🔸 Output Video with Vehicle Detection & Counting  
<video src="https://github.com/user-attachments/assets/YOUR_OUTPUT_VIDEO_ID" width="400" controls></video>

---

## 📹 Input Video

- **File:** `video.mp4`  
- **Source:** [Pixabay Free Traffic Video](https://pixabay.com/videos/search/traffic/)
- Clear daylight traffic footage for accurate detection

---

## ⚙️ How It Works

1. Load the **YOLOv8 pre-trained model** (`yolov8n.pt` for speed, `yolov8s.pt` for higher accuracy)  
2. Process video frames one by one using **OpenCV**  
3. Run YOLOv8 object detection on each frame  
4. Filter detections for **vehicle classes**: car, motorcycle, bus, truck  
5. Draw **bounding boxes** and labels with confidence scores  
6. Count vehicles in the current frame  
7. Overlay the vehicle count onto the video frame  
8. Save the processed frames into an **output video file**  

---

## 🧠 Technologies Used

- Python 3
- YOLOv8 (Ultralytics)
- OpenCV

---

## 📦 Requirements

```bash
ultralytics
opencv-python
Install them using:
pip install -r requirements.txt

 📁 Project Structure
File	Description
main.py	Main script for detection and counting
video.mp4	Input traffic video
output.mp4	Output video with detection & counting
requirements.txt	Python libraries used
README.md	Project documentation

🚀 How to Run
bash
Copy
Edit
pip install -r requirements.txt
python main.py
🔭 Future Enhancements
Lane-wise vehicle counting

Speed estimation of vehicles

Integration with real-time CCTV feeds

Dashboard for live traffic monitoring

Training YOLOv8 on a custom dataset for better accuracy

👨‍💻 Author
Muhammad Rayan Shahid
AI & ML Enthusiast | LinkedIn | GitHub

⭐ If you found this project useful, please consider starring the repository!
