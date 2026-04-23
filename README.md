🚗 Driver Drowsiness Detection System
A real-time driver drowsiness detection system built using Python, OpenCV, and MediaPipe that monitors eye movements through a webcam and triggers an alarm when drowsiness is detected.
📌 Features
Real-time face and eye detection using MediaPipe FaceMesh
Eye Aspect Ratio (EAR) algorithm to detect eye closure
Audio alarm triggered after eyes are closed for 3+ seconds
Live video feed with on-screen status display
Lightweight and runs on any laptop with a webcam
🛠️ Technologies Used
Python 3.11
OpenCV
MediaPipe
Winsound
Math & Time (built-in libraries)
⚙️ How It Works
Webcam captures live video feed
MediaPipe FaceMesh detects 468 facial landmarks
Eye landmarks are extracted for both eyes
EAR (Eye Aspect Ratio) is calculated every frame
If EAR drops below threshold (0.25) for more than 3 seconds → Alarm triggers
👥 Use Cases
Car drivers on long trips
Truck and bus drivers
Heavy machinery operators
Night shift workers
