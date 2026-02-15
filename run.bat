@echo off
REM Screen Capture Tool Launcher for Windows
REM This batch file starts the screen capture application

echo Starting Screen Capture Tool...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

REM Check if PyQt5 is installed
python -c "import PyQt5" >nul 2>&1
if errorlevel 1 (
    echo Error: Required dependencies are not installed
    echo.
    echo Installing dependencies...
    echo.
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo Error: Failed to install dependencies
        echo.
        echo Please try manually running: python -m pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
    echo.
    echo Dependencies installed successfully!
    echo.
)

echo Press ALT+F2 to capture screen
echo Right-click tray icon to access menu
echo.

python main.py

if errorlevel 1 (
    echo.
    echo Error: Failed to start application
    echo.
    echo Please check the error message above for details.
    echo If you see import errors, try reinstalling dependencies:
    echo   python -m pip install -r requirements.txt
    echo.
    pause
)
