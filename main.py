"""
Screen Capture and Annotation Tool
A Snipaste-like application for capturing screen regions and annotating them.
"""

import sys
import atexit
from PyQt5.QtWidgets import QApplication
from screen_capture import ScreenCaptureApp


def main():
    """Main entry point for the application."""
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    capture_app = ScreenCaptureApp()
    
    # Register cleanup function
    atexit.register(capture_app.cleanup)
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
