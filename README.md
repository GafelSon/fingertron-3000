# 🎉 Fingertron 3000

![Fingertron 3000](/thumb/view.png)
**The Ultimate Finger-Counting Technological Marvel!** 🖐️

## 🌟 Project Overview

Fingertron 3000 is a cutting-edge finger-detection system that brings together computer vision, Arduino, and pure technological excitement. It's not just a finger counter—it's a revolution in human-computer interaction!

## 🚀 Key Features

- 🤌 **Advanced Finger Detection**: Leveraging state-of-the-art computer vision
- 🖥️ **Real-time Processing**: Instant finger counting with remarkable accuracy
- 🤖 **Arduino Integration**: Seamless communication between detection and display
- 🌈 **Multi-platform Support**: Works across different environments

## 🛠️ Prerequisites

pip
virtualenv (optional but recommended)

### System Requirements
- Python 3.11 (recommended version) - (conservative releases)
- Arduino Uno
- Webcam or external camera

### Software Dependencies

```bash
# Install required Python packages
pip install opencv-python
pip install mediapipe
pip install pyserial
```

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/gafelson/fingertron-3000.git
cd fingertron-3000
```

### 2. Set Up Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
![Fingertron 3000](/thumb/p2.png)

## 🚀 Running the Project

### Detector Test
```bash
python detector.py
```

### Arduino Uno Board Test
```bash
python uno.py
```

### Main Application
```bash
python main.py
```
![Fingertron 3000](/thumb/p1.png)

## 🔍 How It Works

1. **Camera Detection**:
   - OpenCV captures video stream
   - MediaPipe processes hand landmarks
   - Intelligent algorithm counts visible fingers

2. **Serial Communication**:
   - Detected finger count transmitted via serial port
   - Arduino receives and processes the data

3. **Display**:
   - 7-segment display shows the finger count
   - Real-time update with each detection

## 🎨 Project Architecture

```
fingertron-3000/
│
├── detector.py       # Finger detection module
├── uno.py            # Arduino communication test
├── main.py           # Primary application
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## 🤔 Why Fingertron 3000?

- **Innovation**: Because counting fingers manually is so last century!
- **Learning**: Perfect project for exploring:
  - Computer Vision
  - Arduino Programming
  - Serial Communication
- **Fun**: Who doesn't want a machine that counts fingers?

## 🚧 Future Roadmap

- [ ] Add multi-hand detection
- [ ] Implement gesture recognition
- [ ] Create web dashboard
- [ ] Support more display types

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is open-source. See [LICENSE](LICENSE) for details.

## 🙌 Acknowledgments

- OpenCV Community
- MediaPipe Team
- Arduino Project

---

**Disclaimer**: Fingertron 3000 is not responsible for any existential crises caused by realizing how many fingers you actually have! 😄🖐️
