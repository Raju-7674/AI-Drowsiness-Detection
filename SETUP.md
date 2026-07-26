# 🖥️ Cross-Platform Setup Guide

This project is designed to work on **both Linux and Windows**. Follow the appropriate section for your operating system.

---

## 🐧 Linux Setup

### Prerequisites
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip build-essential cmake

# Fedora/RHEL
sudo dnf install python3 python3-devel cmake gcc-c++

# Arch
sudo pacman -S python cmake base-devel
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Raju-7674/AI-Drowsiness-Detection.git
cd AI-Drowsiness-Detection

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate environment
source venv/bin/activate

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run the application
streamlit run app.py
```

### Linux-Specific Notes
- ✅ **dlib** compiles easily on Linux
- ✅ **Webcam access** works out of the box
- ✅ **Audio** works natively
- All dependencies are generally pre-built and available

---

## 🪟 Windows Setup

### Prerequisites
1. **Python 3.8-3.10** (64-bit) - [Download](https://www.python.org/downloads/)
   - ⚠️ Check "Add Python to PATH" during installation
2. **Visual C++ Build Tools** - [Download](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
3. **Git** - [Download](https://git-scm.com/)

### Installation (Using Conda - Recommended)

```bash
# 1. Install Anaconda from https://www.anaconda.com/download

# 2. Create environment
conda create -n drowsiness python=3.10

# 3. Activate environment
conda activate drowsiness

# 4. Clone repository
git clone https://github.com/Raju-7674/AI-Drowsiness-Detection.git
cd AI-Drowsiness-Detection

# 5. Install dependencies (Conda handles binaries better)
conda install -c conda-forge dlib opencv streamlit numpy

# 6. Install remaining pip packages
pip install -r requirements.txt

# 7. Run the application
streamlit run app.py
```

### Installation (Using venv - Alternative)

```bash
# 1. Clone repository
git clone https://github.com/Raju-7674/AI-Drowsiness-Detection.git
cd AI-Drowsiness-Detection

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
venv\Scripts\activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install Windows-optimized requirements
pip install -r requirements_windows.txt

# 6. Run the application
streamlit run app.py
```

### Windows-Specific Troubleshooting

| Issue | Solution |
|-------|----------|
| **dlib installation fails** | Use Conda: `conda install -c conda-forge dlib` |
| **Webcam not detected** | Settings → Privacy & Security → Camera (enable) |
| **"Module not found" errors** | Ensure venv is activated before pip install |
| **tflite_runtime error** | Already handled in `requirements_windows.txt` |
| **Audio not playing** | Browser may need permission; check Streamlit alerts |

---

## ✅ Compatibility Matrix

| Feature | Linux | Windows |
|---------|-------|---------|
| Python | ✅ 3.8+ | ✅ 3.8-3.10 (64-bit) |
| dlib | ✅ Easy | ⚠️ Requires C++ tools |
| OpenCV | ✅ Yes | ✅ Yes |
| TensorFlow Lite | ✅ Yes | ✅ Yes |
| Streamlit | ✅ Yes | ✅ Yes |
| Webcam | ✅ Native | ✅ Yes |
| Audio Alert | ✅ Yes | ✅ Yes |

---

## 🚀 Quick Start (All Platforms)

Once installed, start with:

```bash
# Activate your environment
# Linux: source venv/bin/activate
# Windows (venv): venv\Scripts\activate
# Windows (Conda): conda activate drowsiness

# Run the app
streamlit run app.py

# App opens at http://localhost:8501
```

---

## 🔍 Verify Installation

```bash
# Check Python
python --version

# Test imports
python -c "import cv2; print('✓ OpenCV')"
python -c "import dlib; print('✓ dlib')"
python -c "import streamlit; print('✓ Streamlit')"
python -c "import tflite_runtime; print('✓ TFLite')"

# Test webcam (Linux/Windows)
python -c "import cv2; cap = cv2.VideoCapture(0); print('✓ Webcam' if cap.isOpened() else '✗ Webcam not found')"

# Verify model files
ls Models/  # Linux
dir Models  # Windows
```

---

## 📋 Files Provided

| File | Purpose |
|------|---------|
| `requirements.txt` | Universal requirements (Linux preferred) |
| `requirements_windows.txt` | Windows-optimized with TFLite index |
| `WINDOWS_SETUP.md` | Detailed Windows guide |
| `SETUP.md` | This file (you are here) |

---

## ⚡ Performance Tips

### Linux
```bash
# Use PyPy for faster execution (if compatible)
# Or use `pypy3 -m pip install ...`
```

### Windows
- Use **Conda** for faster installation and better binary support
- Run Streamlit in **incognito mode** for best performance
- Ensure sufficient RAM (8GB+ recommended)

---

## 🆘 Common Issues Across Platforms

### Model Files Missing
```bash
# Ensure Models/ contains:
# - shape_predictor_68_face_landmarks.dat
# - CNN_Eye_classifier.tflite
# - CNN_Yawn_classifier.tflite
```

### Port 8501 Already in Use
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

### Face Not Detected
- Ensure good lighting
- Position face clearly in webcam frame
- Keep distance 30-60cm from webcam

---

## 📞 Support

- Linux issues: Check if build-essential/cmake are installed
- Windows issues: Verify Visual C++ tools are installed
- All platforms: Ensure webcam permissions are granted
- Check GitHub Issues for more solutions

---

**Your project is now ready for both Linux and Windows! 🎉**
