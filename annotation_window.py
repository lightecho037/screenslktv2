"""
Annotation window for captured screenshots.
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QToolBar, QAction, QColorDialog, QInputDialog,
                             QFileDialog, QApplication, QLabel, QSpinBox)
from PyQt5.QtCore import Qt, QPoint, QRect, pyqtSignal
from PyQt5.QtGui import (QPainter, QPen, QColor, QPixmap, QImage, QCursor,
                        QFont, QPainterPath, QPolygonF)
import io
from PIL import Image


class AnnotationTool:
    """Base class for annotation tools."""
    PEN = 0
    TEXT = 1
    ARROW = 2
    RECTANGLE = 3
    ELLIPSE = 4
    

class AnnotationWindow(QWidget):
    """Window for displaying and annotating captured screenshots."""
    
    def __init__(self, screenshot, original_pos=None):
        super().__init__()
        self.screenshot = screenshot
        self.original_pos = original_pos or QPoint(0, 0)
        self.annotations = []  # List of annotation items
        self.current_tool = AnnotationTool.PEN
        self.pen_color = QColor(255, 0, 0)
        self.pen_width = 3
        self.is_drawing = False
        self.last_point = None
        self.current_annotation = None
        
        # For moving the window
        self.dragging = False
        self.drag_position = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the annotation window UI."""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        
        # Set initial position
        self.move(self.original_pos)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Toolbar
        toolbar = self.create_toolbar()
        layout.addWidget(toolbar)
        
        # Image label
        self.image_label = QLabel()
        self.update_image()
        layout.addWidget(self.image_label)
        
        self.setLayout(layout)
        
        # Set window size
        self.resize(self.screenshot.width(), self.screenshot.height() + 40)
        
    def create_toolbar(self):
        """Create the toolbar with annotation tools."""
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setStyleSheet("""
            QToolBar { 
                background-color: #2d2d30; 
                border: 1px solid #3e3e42;
                spacing: 3px;
                padding: 2px;
            }
            QToolButton { 
                background-color: #3e3e42;
                color: white;
                border: 1px solid #555;
                padding: 5px;
                margin: 1px;
            }
            QToolButton:hover {
                background-color: #007acc;
            }
            QToolButton:checked {
                background-color: #007acc;
            }
        """)
        
        # Pen tool
        pen_action = QAction("✏️ Pen", self)
        pen_action.setCheckable(True)
        pen_action.setChecked(True)
        pen_action.triggered.connect(lambda: self.set_tool(AnnotationTool.PEN))
        toolbar.addAction(pen_action)
        self.pen_action = pen_action
        
        # Text tool
        text_action = QAction("📝 Text", self)
        text_action.setCheckable(True)
        text_action.triggered.connect(lambda: self.set_tool(AnnotationTool.TEXT))
        toolbar.addAction(text_action)
        self.text_action = text_action
        
        # Arrow tool
        arrow_action = QAction("➡️ Arrow", self)
        arrow_action.setCheckable(True)
        arrow_action.triggered.connect(lambda: self.set_tool(AnnotationTool.ARROW))
        toolbar.addAction(arrow_action)
        self.arrow_action = arrow_action
        
        # Rectangle tool
        rect_action = QAction("⬜ Rectangle", self)
        rect_action.setCheckable(True)
        rect_action.triggered.connect(lambda: self.set_tool(AnnotationTool.RECTANGLE))
        toolbar.addAction(rect_action)
        self.rect_action = rect_action
        
        # Ellipse tool
        ellipse_action = QAction("⭕ Ellipse", self)
        ellipse_action.setCheckable(True)
        ellipse_action.triggered.connect(lambda: self.set_tool(AnnotationTool.ELLIPSE))
        toolbar.addAction(ellipse_action)
        self.ellipse_action = ellipse_action
        
        toolbar.addSeparator()
        
        # Color picker
        color_action = QAction("🎨 Color", self)
        color_action.triggered.connect(self.choose_color)
        toolbar.addAction(color_action)
        
        # Pen width
        width_label = QLabel(" Width: ")
        width_label.setStyleSheet("color: white; padding: 0 5px;")
        toolbar.addWidget(width_label)
        
        self.width_spinner = QSpinBox()
        self.width_spinner.setMinimum(1)
        self.width_spinner.setMaximum(20)
        self.width_spinner.setValue(3)
        self.width_spinner.valueChanged.connect(self.change_width)
        self.width_spinner.setStyleSheet("""
            QSpinBox {
                background-color: #3e3e42;
                color: white;
                border: 1px solid #555;
                padding: 3px;
            }
        """)
        toolbar.addWidget(self.width_spinner)
        
        toolbar.addSeparator()
        
        # Save button
        save_action = QAction("💾 Save", self)
        save_action.triggered.connect(self.save_image)
        toolbar.addAction(save_action)
        
        # Copy button
        copy_action = QAction("📋 Copy", self)
        copy_action.triggered.connect(self.copy_to_clipboard)
        toolbar.addAction(copy_action)
        
        toolbar.addSeparator()
        
        # Close button
        close_action = QAction("❌ Close", self)
        close_action.triggered.connect(self.close)
        toolbar.addAction(close_action)
        
        return toolbar
        
    def set_tool(self, tool):
        """Set the current annotation tool."""
        self.current_tool = tool
        
        # Update checked state of tool buttons
        self.pen_action.setChecked(tool == AnnotationTool.PEN)
        self.text_action.setChecked(tool == AnnotationTool.TEXT)
        self.arrow_action.setChecked(tool == AnnotationTool.ARROW)
        self.rect_action.setChecked(tool == AnnotationTool.RECTANGLE)
        self.ellipse_action.setChecked(tool == AnnotationTool.ELLIPSE)
        
    def choose_color(self):
        """Open color picker dialog."""
        color = QColorDialog.getColor(self.pen_color, self, "Choose Color")
        if color.isValid():
            self.pen_color = color
            
    def change_width(self, value):
        """Change pen width."""
        self.pen_width = value
        
    def update_image(self):
        """Update the displayed image with annotations."""
        # Create a copy of the screenshot
        result = QPixmap(self.screenshot)
        
        # Draw annotations
        painter = QPainter(result)
        painter.setRenderHint(QPainter.Antialiasing)
        
        for annotation in self.annotations:
            self.draw_annotation(painter, annotation)
            
        # Draw current annotation if any
        if self.current_annotation:
            self.draw_annotation(painter, self.current_annotation)
            
        painter.end()
        
        self.image_label.setPixmap(result)
        
    def draw_annotation(self, painter, annotation):
        """Draw a single annotation."""
        pen = QPen(annotation['color'], annotation['width'])
        painter.setPen(pen)
        
        if annotation['type'] == AnnotationTool.PEN:
            path = annotation['path']
            painter.drawPath(path)
            
        elif annotation['type'] == AnnotationTool.TEXT:
            font = QFont()
            font.setPointSize(annotation.get('font_size', 12))
            painter.setFont(font)
            painter.drawText(annotation['pos'], annotation['text'])
            
        elif annotation['type'] == AnnotationTool.ARROW:
            start = annotation['start']
            end = annotation['end']
            
            # Draw line
            painter.drawLine(start, end)
            
            # Draw arrowhead
            arrow_size = 10
            angle = QPoint(end.x() - start.x(), end.y() - start.y())
            
            # Simple arrowhead (triangle)
            dx = end.x() - start.x()
            dy = end.y() - start.y()
            length = (dx*dx + dy*dy) ** 0.5
            
            if length > 0:
                # Normalize
                dx /= length
                dy /= length
                
                # Perpendicular
                px = -dy
                py = dx
                
                # Arrowhead points
                p1 = QPoint(int(end.x() - arrow_size * dx + arrow_size/2 * px),
                           int(end.y() - arrow_size * dy + arrow_size/2 * py))
                p2 = QPoint(int(end.x() - arrow_size * dx - arrow_size/2 * px),
                           int(end.y() - arrow_size * dy - arrow_size/2 * py))
                
                polygon = QPolygonF([end, p1, p2])
                painter.setBrush(annotation['color'])
                painter.drawPolygon(polygon)
            
        elif annotation['type'] == AnnotationTool.RECTANGLE:
            rect = QRect(annotation['start'], annotation['end'])
            painter.drawRect(rect.normalized())
            
        elif annotation['type'] == AnnotationTool.ELLIPSE:
            rect = QRect(annotation['start'], annotation['end'])
            painter.drawEllipse(rect.normalized())
    
    def mousePressEvent(self, event):
        """Handle mouse press events."""
        # Check if clicking on toolbar area
        if event.pos().y() < 40:
            if event.button() == Qt.LeftButton:
                self.dragging = True
                self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            return
            
        # Handle annotation tools
        if event.button() == Qt.LeftButton:
            pos = event.pos() - QPoint(0, 40)  # Adjust for toolbar
            
            if self.current_tool == AnnotationTool.PEN:
                self.is_drawing = True
                self.last_point = pos
                path = QPainterPath()
                path.moveTo(pos)
                self.current_annotation = {
                    'type': AnnotationTool.PEN,
                    'color': self.pen_color,
                    'width': self.pen_width,
                    'path': path
                }
                
            elif self.current_tool == AnnotationTool.TEXT:
                text, ok = QInputDialog.getText(self, 'Add Text', 'Enter text:')
                if ok and text:
                    self.annotations.append({
                        'type': AnnotationTool.TEXT,
                        'color': self.pen_color,
                        'width': self.pen_width,
                        'pos': pos,
                        'text': text,
                        'font_size': 12
                    })
                    self.update_image()
                    
            elif self.current_tool in [AnnotationTool.ARROW, AnnotationTool.RECTANGLE, AnnotationTool.ELLIPSE]:
                self.is_drawing = True
                self.current_annotation = {
                    'type': self.current_tool,
                    'color': self.pen_color,
                    'width': self.pen_width,
                    'start': pos,
                    'end': pos
                }
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events."""
        if self.dragging:
            self.move(event.globalPos() - self.drag_position)
            return
            
        if self.is_drawing:
            pos = event.pos() - QPoint(0, 40)
            
            if self.current_tool == AnnotationTool.PEN:
                if self.current_annotation:
                    self.current_annotation['path'].lineTo(pos)
                    self.update_image()
                    
            elif self.current_tool in [AnnotationTool.ARROW, AnnotationTool.RECTANGLE, AnnotationTool.ELLIPSE]:
                if self.current_annotation:
                    self.current_annotation['end'] = pos
                    self.update_image()
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release events."""
        if self.dragging:
            self.dragging = False
            return
            
        if event.button() == Qt.LeftButton and self.is_drawing:
            self.is_drawing = False
            
            if self.current_annotation:
                self.annotations.append(self.current_annotation)
                self.current_annotation = None
                self.update_image()
    
    def save_image(self):
        """Save the annotated image to a file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            "",
            "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)"
        )
        
        if file_path:
            # Get the current pixmap with annotations
            pixmap = self.image_label.pixmap()
            pixmap.save(file_path)
            
    def copy_to_clipboard(self):
        """Copy the annotated image to clipboard."""
        pixmap = self.image_label.pixmap()
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(pixmap)
