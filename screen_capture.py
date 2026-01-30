"""
Screen capture functionality with region selection.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSystemTrayIcon, QMenu, 
                             QAction, qApp)
from PyQt5.QtCore import Qt, QRect, QPoint, pyqtSignal
from PyQt5.QtGui import (QPainter, QPen, QColor, QPixmap, QGuiApplication, 
                        QScreen, QIcon, QCursor)
import keyboard
from annotation_window import AnnotationWindow


class SelectionOverlay(QWidget):
    """Overlay widget for selecting screen region to capture."""
    
    selection_made = pyqtSignal(QRect)
    
    def __init__(self, screenshot):
        super().__init__()
        self.screenshot = screenshot
        self.selection_rect = QRect()
        self.start_pos = None
        self.is_selecting = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the overlay UI."""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowState(Qt.WindowFullScreen)
        self.setCursor(Qt.CrossCursor)
        self.showFullScreen()
        
    def paintEvent(self, event):
        """Paint the overlay with selection rectangle."""
        painter = QPainter(self)
        
        # Draw darkened screenshot
        painter.drawPixmap(0, 0, self.screenshot)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 100))
        
        # Draw selection rectangle
        if not self.selection_rect.isNull():
            # Clear the selected area
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(self.selection_rect, Qt.transparent)
            
            # Draw border around selection
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            pen = QPen(QColor(0, 120, 215), 2, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawRect(self.selection_rect)
            
            # Draw size label
            if self.selection_rect.width() > 0 and self.selection_rect.height() > 0:
                size_text = f"{self.selection_rect.width()} x {self.selection_rect.height()}"
                painter.setPen(QColor(255, 255, 255))
                text_rect = painter.fontMetrics().boundingRect(size_text)
                text_pos = QPoint(
                    self.selection_rect.right() - text_rect.width() - 5,
                    self.selection_rect.bottom() + 20
                )
                painter.drawText(text_pos, size_text)
    
    def mousePressEvent(self, event):
        """Handle mouse press to start selection."""
        if event.button() == Qt.LeftButton:
            self.start_pos = event.pos()
            self.selection_rect = QRect(self.start_pos, self.start_pos)
            self.is_selecting = True
            self.update()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move to update selection."""
        if self.is_selecting and self.start_pos:
            self.selection_rect = QRect(self.start_pos, event.pos()).normalized()
            self.update()
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release to complete selection."""
        if event.button() == Qt.LeftButton and self.is_selecting:
            self.is_selecting = False
            if self.selection_rect.width() > 5 and self.selection_rect.height() > 5:
                self.selection_made.emit(self.selection_rect)
                self.close()
            else:
                # If selection too small, cancel
                self.close()
    
    def keyPressEvent(self, event):
        """Handle key press events."""
        if event.key() == Qt.Key_Escape:
            self.close()


class ScreenCaptureApp:
    """Main application class for screen capture tool."""
    
    def __init__(self):
        self.tray_icon = None
        self.annotation_windows = []
        self.setup_tray_icon()
        self.setup_hotkeys()
        
    def setup_tray_icon(self):
        """Set up system tray icon."""
        self.tray_icon = QSystemTrayIcon()
        
        # Create icon (simple colored icon for now)
        icon_pixmap = QPixmap(64, 64)
        icon_pixmap.fill(QColor(0, 120, 215))
        painter = QPainter(icon_pixmap)
        painter.setPen(QPen(QColor(255, 255, 255), 8))
        painter.drawRect(10, 10, 44, 44)
        painter.end()
        
        self.tray_icon.setIcon(QIcon(icon_pixmap))
        
        # Create menu
        menu = QMenu()
        
        capture_action = QAction("Capture Screen (F1)", None)
        capture_action.triggered.connect(self.start_capture)
        menu.addAction(capture_action)
        
        menu.addSeparator()
        
        quit_action = QAction("Quit", None)
        quit_action.triggered.connect(qApp.quit)
        menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()
        
        # Set tooltip
        self.tray_icon.setToolTip("Screen Capture Tool - Press F1 to capture")
        
    def setup_hotkeys(self):
        """Set up global hotkeys."""
        try:
            keyboard.add_hotkey('f1', self.start_capture)
        except Exception as e:
            print(f"Warning: Could not register hotkey F1: {e}")
            print("You can still use the tray icon menu to capture.")
    
    def start_capture(self):
        """Start the screen capture process."""
        # Take screenshot of all screens
        screen = QGuiApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
        
        # Show selection overlay
        overlay = SelectionOverlay(screenshot)
        overlay.selection_made.connect(self.on_selection_made)
        
    def on_selection_made(self, rect):
        """Handle the selection completion."""
        # Capture the selected region
        screen = QGuiApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
        
        # Crop to selected region
        cropped = screenshot.copy(rect)
        
        # Open annotation window
        annotation_window = AnnotationWindow(cropped, rect.topLeft())
        annotation_window.show()
        self.annotation_windows.append(annotation_window)
