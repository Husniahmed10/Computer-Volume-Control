# Hand Gesture Volume Control using Computer Vision

This project demonstrates a real-time hand gesture volume control system using Python, OpenCV, and MediaPipe. The system leverages computer vision to detect hand landmarks and control the system volume based on the distance between the thumb and index finger.

## Features
- **Hand Detection**: Utilizes MediaPipe to detect and track hand landmarks in real-time.
- **Volume Control**: Adjusts the system volume based on the distance between the thumb and index finger.
- **Real-time Processing**: Processes video frames in real-time for smooth performance.
- **Visual Feedback**: Displays landmarks, connections, and volume level on the video feed.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- PyCaw (for volume control)
- comtypes

## Setup and Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hand-gesture-volume-control.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hand-gesture-volume-control
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the project:
    ```bash
    python main.py
    ```

## How it Works
1. **Hand Detection**: The `handDetector` class uses MediaPipe to detect hand landmarks in the video feed.
2. **Position Detection**: Extracts the positions of specific landmarks (thumb and index finger).
3. **Volume Control**: Maps the distance between the thumb and index finger to the system volume level using PyCaw.
4. **Visual Feedback**: Displays the hand landmarks, distance line, and volume level on the video feed for user feedback.

## Code Overview
- `handDetector` class: Contains methods for hand detection and landmark position extraction.
- `main` function: Initializes the video capture, processes each frame, and adjusts the volume based on hand gestures.

## Future Improvements
- Add more gesture controls for additional functionalities.
- Improve hand detection accuracy and performance.
- Develop a user interface for easier interaction.


