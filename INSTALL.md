# Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Windows 10/11 (recommended)

## Step-by-Step Installation

### 1. Install Python

If you don't have Python installed:

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Complete the installation

### 2. Clone or Download the Repository

**Option A: Using Git**
```bash
git clone https://github.com/lightecho037/screenslktv2.git
cd screenslktv2
```

**Option B: Download ZIP**
1. Download the repository as ZIP
2. Extract to a folder
3. Open Command Prompt in that folder

### 3. Install Dependencies

Open Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

This will install:
- PyQt5 (GUI framework)
- Pillow (Image processing)
- keyboard (Global hotkeys)
- pywin32 (Windows support)

### 4. Run the Application

**Option A: Using the batch file (Windows)**
```bash
run.bat
```

**Option B: Using Python directly**
```bash
python main.py
```

The application will start and minimize to the system tray.

## Troubleshooting

### "Python is not recognized"

- Python is not in your PATH
- Reinstall Python and check "Add Python to PATH"
- Or use full path: `C:\Python3x\python.exe main.py`

### "No module named PyQt5"

- Dependencies not installed
- Run: `pip install -r requirements.txt`

### Hotkey not working

- Try running as Administrator
- Check if another application is using ALT+F2
- Use the tray icon menu instead

### Application doesn't appear in tray

- Check system tray settings
- Look in hidden icons area (click arrow in system tray)
- Windows may hide the icon by default

## Virtual Environment (Optional but Recommended)

To avoid conflicts with other Python projects:

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

## Uninstallation

Simply delete the project folder. If you want to remove the Python packages:

```bash
pip uninstall PyQt5 pillow keyboard pywin32
```

## Next Steps

After installation, see [README.md](README.md) for usage instructions.
