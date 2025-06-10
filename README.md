# Gesture Controlled Volume using Hand Tracking 

This project allows you to control your system volume using hand gestures via your webcam. It uses **OpenCV** and **MediaPipe** to track hand landmarks, and **Pycaw** to manipulate the system's audio levels.

---

## Features

- Real-time hand tracking using MediaPipe.
- Volume control using the distance between thumb and index finger.
- Smooth volume interpolation with visual feedback.
- FPS counter and live video stream with OpenCV.

---

## Project Structure
```
GestureVolumeControl/
├── HandTrackingModule.py # Module for hand detection and landmark extraction
├── GestureControlVolume.py # Main script to control system volume via gestures
├── README.md
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- Webcam
- Windows (required for Pycaw to work)

### Install dependencies

```bash
pip install -r requirements.txt

```

## How It Works

-Detect hand landmarks using MediaPipe.

-Extract positions of thumb tip (id 4) and index finger tip (id 8).

-Calculate distance between them.

-Map this distance to the system's volume range using Pycaw.

-Update UI with visual indicators and FPS counter.

## Controls
-Pinch gesture (thumb and index) to control volume.

-Close pinch → Lower volume

-Wide pinch → Raise volume

## Notes
-Works only on Windows because Pycaw interfaces with Windows Core Audio.

-Lighting conditions can affect hand detection quality.

-MediaPipe can detect up to 2 hands, but only one hand is used here.

## License
This project is open-source and free to use under the MIT License.
