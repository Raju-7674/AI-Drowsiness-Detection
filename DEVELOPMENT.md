# 🛠️ Development Setup Guide

This guide helps contributors and developers set up the project for development or testing.

---

## Platform-Specific Guides

### For Windows Users
See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for detailed Windows-specific instructions.

### For Linux/Mac Users
See [SETUP.md](SETUP.md) for general cross-platform instructions.

---

## Environment Variables (Optional)

```bash
# Set debug mode
export DEBUG=1  # Linux/Mac
set DEBUG=1     # Windows

# Set custom Streamlit port
export STREAMLIT_SERVER_PORT=8502  # Linux/Mac
set STREAMLIT_SERVER_PORT=8502     # Windows
```

---

## IDE Setup Recommendations

### VS Code
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
}
```

### PyCharm
1. Go to Settings → Project → Python Interpreter
2. Select "Add..." → "Existing Environment"
3. Navigate to `venv/bin/python` (Linux) or `venv\Scripts\python.exe` (Windows)

---

## Testing the Installation

### Quick Test
```bash
python -c "
import cv2, dlib, streamlit, numpy as np, tflite_runtime
print('✓ All packages imported successfully!')
"
```

### Full Test
```bash
streamlit run app.py --logger.level=debug
```

---

## Troubleshooting

### "ModuleNotFoundError"
```bash
# Ensure venv is activated
# Linux: source venv/bin/activate
# Windows: venv\Scripts\activate

# Reinstall requirements
pip install --force-reinstall -r requirements.txt
```

### "Permission Denied" (Linux)
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### "No module named 'streamlit'"
```bash
# Inside activated venv
pip install streamlit==1.28.1
```

---

For detailed platform-specific instructions, refer to [SETUP.md](SETUP.md) or [WINDOWS_SETUP.md](WINDOWS_SETUP.md).
