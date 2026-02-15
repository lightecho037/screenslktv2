@echo off
REM Screen Capture Tool Launcher for Windows
REM This batch file starts the screen capture application

echo Starting Screen Capture Tool...
echo.
echo Press ALT+F2 to capture screen
echo Right-click tray icon to access menu
echo.

python main.py

if errorlevel 1 (
    echo.
    echo Error: Failed to start application
    echo.
    echo Please ensure:
    echo 1. Python is installed and in PATH
    echo 2. Dependencies are installed: pip install -r requirements.txt
    echo.
    pause
)
