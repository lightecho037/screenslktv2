# Screen Capture & Annotation Tool

A powerful Python-based screen capture and annotation tool similar to Snipaste. Capture any region of your screen, annotate it with various tools, and save or copy the result to clipboard.

## Features

- 🖼️ **Screen Region Capture**: Select and capture any region of your screen
- ⌨️ **Global Hotkeys**: Use ALT+F2 to quickly capture screen (customizable)
- 🎨 **Annotation Tools**:
  - ✏️ Pen/Drawing tool for freehand annotations
  - 📝 Text annotations
  - ➡️ Arrows for pointing
  - ⬜ Rectangle shapes
  - ⭕ Ellipse/Circle shapes
- 🎨 **Customization**: Choose colors and pen width for all tools
- 🖱️ **Movable Overlay**: Drag the annotation window anywhere on screen
- 💾 **Save**: Save annotated screenshots as PNG or JPEG
- 📋 **Copy**: Copy to clipboard for quick sharing
- 🪟 **Windows Compatible**: Designed to run smoothly on Windows

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lightecho037/screenslktv2.git
cd screenslktv2
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Application

Run the application:
```bash
python main.py
```

The application will minimize to the system tray. Look for the screen capture icon in your system tray.

### Capturing Screen

**Method 1: Global Hotkey**
- Press `ALT+F2` anywhere on your system to start capturing

**Method 2: System Tray**
- Right-click the tray icon
- Select "Capture Screen (ALT+F2)"

### Selecting Region

1. After triggering capture, your screen will darken
2. Click and drag to select the region you want to capture
3. Release the mouse to confirm selection
4. Press `ESC` to cancel

### Annotating

Once you've captured a region, the annotation window appears with these tools:

- **✏️ Pen**: Draw freehand lines and shapes
- **📝 Text**: Click to add text annotations
- **➡️ Arrow**: Draw arrows to point at specific areas
- **⬜ Rectangle**: Draw rectangle shapes
- **⭕ Ellipse**: Draw ellipse/circle shapes

**Additional Controls**:
- **🎨 Color**: Click to choose annotation color
- **Width**: Adjust the pen width (1-20 pixels)
- **💾 Save**: Save the annotated image to a file
- **📋 Copy**: Copy the image to clipboard
- **❌ Close**: Close the annotation window

### Moving the Window

Click and drag the toolbar area (top dark bar) to move the annotation window anywhere on your screen.

## System Requirements

- Python 3.7 or higher
- Windows OS (tested on Windows 10/11)
- PyQt5
- Additional dependencies listed in requirements.txt

## Dependencies

- **PyQt5**: GUI framework
- **Pillow**: Image processing
- **keyboard**: Global hotkey support
- **pywin32**: Windows-specific functionality (Windows only)

## Architecture

The application is organized into clean, modular classes:

- **`main.py`**: Application entry point
- **`screen_capture.py`**: 
  - `ScreenCaptureApp`: Main application and tray icon management
  - `SelectionOverlay`: Screen region selection interface
- **`annotation_window.py`**:
  - `AnnotationWindow`: Annotation interface and tool management
  - `AnnotationTool`: Tool definitions

## Troubleshooting

### Hotkey Not Working

If ALT+F2 hotkey doesn't work:
- The application may not have sufficient permissions
- Try running as administrator
- Use the tray icon menu as an alternative

### Application Not Appearing in Tray

- Check if your system tray is set to show all icons
- Look in the hidden icons area (click the up arrow in system tray)

## License

This project is open source and available for educational and personal use.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Acknowledgments

Inspired by Snipaste - an excellent screen capture tool.