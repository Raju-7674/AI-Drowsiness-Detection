# 🪟 Windows Setup Guide for AI Drowsiness Detection

This guide provides comprehensive instructions for installing and running the AI Drowsiness Detection System on Windows.

## ✅ System Requirements

- **Windows 10/11** (64-bit recommended)
- **Python 3.8-3.10** (64-bit version)
- **Webcam** for live feed
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: ~500MB

## 📋 Pre-Installation Steps

### 1. Install Python
- Download Python 3.10 from [python.org](https://www.python.org/downloads/)
- **IMPORTANT**: Check "Add Python to PATH" during installation
- Verify installation:
  ```bash
  python --version
  ```

### 2. Install Visual C++ Build Tools (Required for dlib)
dlib requires compilation on Windows. You need Visual C++ build tools:

**Option A: Use Visual Studio Build Tools**
- Download from: [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)
- Select "Desktop development with C++"
- Install it

**Option B: Use Visual C++ Redistributable**
- Download: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Minimal installation needed

### 3. Grant Camera Permissions (Windows 10/11)
1. Go to **Settings → Privacy & Security → Camera**
2. Enable camera access
3. Allow Python to access the camera

---

## 🚀 Installation Methods

### Method 1: Using Conda (RECOMMENDED for Windows)

Conda handles binary dependencies much better on Windows.

```bash
# 1. Download and install Anaconda
# From: https://www.anaconda.com/download

# 2. Create a new environment
conda create -n drowsiness python=3.10

# 3. Activate the environment
conda activate drowsiness

# 4. Clone the repository
git clone https://github.com/Raju-7674/AI-Drowsiness-Detection.git
cd AI-Drowsiness-Detection

# 5. Install conda dependencies (includes pre-compiled dlib)
conda install -c conda-forge dlib opencv streamlit numpy

# 6. Install pip dependencies
pip install -r requirements_windows.txt

# 7. Run the application
streamlit run app.py
```

### Method 2: Using Python venv (if Conda not available)

```bash
# 1. Clone the repository
git clone https://github.com/Raju-7674/AI-Drowsiness-Detection.git
cd AI-Drowsiness-Detection

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install dependencies from requirements_windows.txt
pip install -r requirements_windows.txt

# 6. Run the application
streamlit run app.py
```

---

## 🔧 Troubleshooting Common Windows Issues

### ❌ Problem: "dlib installation failed"

**Solution 1: Use Pre-compiled Wheel**
```bash
# Download pre-compiled dlib wheel
pip install dlib --only-binary :all:
```

**Solution 2: Install Visual C++ Build Tools first**
```bash
# Then retry
pip install dlib
```

**Solution 3: Use Conda (Easiest)**
```bash
conda install -c conda-forge dlib
```

---

### ❌ Problem: "tflite_runtime not found"

**Solution:**
```bash
pip install --index-url https://google-coral.github.io/py-repo/tflite_runtime tflite_runtime
```

Or use the pre-configured `requirements_windows.txt`

---

### ❌ Problem: "Module 'av' not found"

**Solution:**
```bash
pip install av
# If that fails, try:
conda install av
```

---

### ❌ Problem: "Webcam access denied"

**Solution:**
1. Go to Windows Settings → Privacy & Security → Camera
2. Ensure camera access is enabled
3. Restart the Streamlit app

---

### ❌ Problem: "shape_predictor_68_face_landmarks.dat not found"

**Solution:**
```bash
# Ensure the file exists in Models/ directory
# If missing, download from:
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# Extract and place in AI-Drowsiness-Detection/Models/
```

---

## ✅ Quick Start Checklist

- [ ] Python 3.10 installed and added to PATH
- [ ] Visual C++ Build Tools installed (if using pip method)
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] All dependencies installed
- [ ] Models folder contains `.dat` and `.tflite` files
- [ ] Webcam permissions granted
- [ ] Streamlit app running without errors

---

## 🎯 Running the Application

Once everything is installed:

```bash
# Make sure your environment is activated
# For conda:
conda activate drowsiness

# For venv:
venv\Scripts\activate

# Run the app
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## 📊 First-Run Tips

1. **Ensure good lighting** for accurate face detection
2. **Position your face properly** in the center of the webcam feed
3. **Wait 2-3 seconds** for the face landmarks to appear
4. **Test eye and yawn detection** before using as a driver alert
5. **Enable warning sound** in the right panel

---

## 🐛 Debugging Commands

If you encounter issues, run these commands to check your setup:

```bash
# Check Python version
python --version

# Check if modules can be imported
python -c "import cv2; print('OpenCV OK')"
python -c "import dlib; print('dlib OK')"
python -c "import streamlit; print('Streamlit OK')"
python -c "import tflite_runtime; print('TFLite OK')"

# Check model files
dir Models\

# Test webcam access
python -c "import cv2; cap = cv2.VideoCapture(0); print('Webcam accessible' if cap.isOpened() else 'Webcam not found')"
```

---

## 📞 Getting Help

If you still encounter issues:
1. Check the GitHub Issues section
2. Verify all model files are present in the `Models/` directory
3. Try using Conda instead of pip
4. Ensure Windows Defender or antivirus isn't blocking Python

---

**Happy detecting! 🚗👁️**
