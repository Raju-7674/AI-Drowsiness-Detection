# 🚗 AI-Powered Driver Drowsiness Detection System

An end-to-end **AI-Powered Driver Drowsiness Detection System** that monitors driver alertness in real time using **Computer Vision** and **Deep Learning**. The application detects prolonged eye closure and yawning, calculates a drowsiness score, and instantly alerts the driver when signs of fatigue are detected.

The system integrates real-time webcam processing, facial landmark detection, optimized deep learning models, and an interactive web dashboard to provide an intelligent driver monitoring solution.

---

## 📌 Features

- 👁️ Real-time Eye Closure Detection
- 😮 Real-time Yawn Detection
- 🙂 Facial Landmark Detection using **dlib (68 landmarks)**
- 🚨 Instant Audio Alert when drowsiness is detected
- 📹 Live Webcam Integration using **Streamlit-WebRTC**
- 📊 Interactive Streamlit Dashboard
- ⚡ TensorFlow Lite optimized inference
- 🧠 Dynamic Drowsiness Calculation
- 📈 Real-time Monitoring and Status Display

---

## 🛠️ Tech Stack

- Python
- TensorFlow Lite
- OpenCV
- dlib
- NumPy
- Streamlit
- Streamlit-WebRTC
- Git
- GitHub

---

## 📂 Project Structure

```text
AI_Driver_Drowsiness_Detection/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── alarm.mp3
│   └── images/
│
├── models/
│   ├── eye_model.tflite
│   └── yawn_model.tflite
│
├── src/
│   ├── webcam.py
│   ├── face_detector.py
│   ├── eye_detector.py
│   ├── yawn_detector.py
│   ├── drowsiness_score.py
│   ├── dashboard.py
│   └── utils.py
│
├── notebooks/
│
├── evaluation/
│
└── docs/
```

---

## 🚀 Project Workflow

```text
                 Webcam
                    │
                    ▼
          Streamlit-WebRTC
                    │
                    ▼
              OpenCV Frames
                    │
                    ▼
          dlib Face Detection
                    │
                    ▼
        68 Facial Landmark Detection
                    │
        ┌───────────┴────────────┐
        ▼                        ▼
   Eye Region              Mouth Region
        │                        │
        ▼                        ▼
 TensorFlow Lite          TensorFlow Lite
 Eye Detection            Yawn Detection
        │                        │
        └───────────┬────────────┘
                    ▼
         Drowsiness Score Engine
                    │
                    ▼
           Driver Status Decision
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Normal Driver     Drowsy Driver
                              │
                              ▼
                     Audio Alert + Dashboard
```

---

## 📊 Dashboard

The Streamlit dashboard provides:

- 📹 Live Webcam Feed
- 👁️ Eye Status
- 😮 Yawn Status
- 📈 Drowsiness Score
- ⏱️ Eye Closure Timer
- 🚨 Alarm Status
- 🟢 Driver State Monitoring

---

## 🎯 Models Used

### Eye Closure Detection
- Framework: TensorFlow Lite
- Model Type: Convolutional Neural Network (CNN)
- Classes:
  - Open Eye
  - Closed Eye

### Yawn Detection
- Framework: TensorFlow Lite
- Model Type: Convolutional Neural Network (CNN)
- Classes:
  - Yawn
  - No Yawn

---

## 💡 What I Learned

- Building an end-to-end AI application
- Real-time Computer Vision using OpenCV
- Facial Landmark Detection using dlib
- Optimizing TensorFlow Lite models for efficient inference
- Integrating multiple AI models into a single application
- Developing interactive dashboards using Streamlit
- Debugging dependency and deployment issues
- Project structuring and modular development
- Version control using Git and GitHub

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Raju-7674/AI-Driver-Drowsiness-Detection.git
```

Navigate to the project directory:

```bash
cd AI-Driver-Drowsiness-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

- Head Pose Estimation
- Blink Rate Analysis
- Face Recognition
- Driver Identity Verification
- Cloud Deployment
- Mobile Application
- Performance Analytics Dashboard
- Driver Fatigue Reports
- Multi-Person Detection
- Night Vision Support

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. Your support motivates me to continue building and sharing AI-powered applications.

---

## 👨‍💻 Author

**KanakaRaju Simhadri**

Aspiring AI Engineer | Machine Learning | Deep Learning | Computer Vision | Python | Building Real-World AI Applications
