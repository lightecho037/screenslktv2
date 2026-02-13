# Architecture Overview

## Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                       main.py                               │
│  • Application Entry Point                                  │
│  • Initializes QApplication                                 │
│  • Creates ScreenCaptureApp                                 │
│  • Registers cleanup handlers                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ creates
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              screen_capture.py                              │
│                                                             │
│  ┌───────────────────────────────────────────────┐         │
│  │       ScreenCaptureApp                        │         │
│  │  • System tray management                     │         │
│  │  • Global hotkey registration                 │         │
│  │  • Screenshot coordination                    │         │
│  │  • Window lifecycle management                │         │
│  └───────┬───────────────────────────────────────┘         │
│          │                                                  │
│          │ creates on capture                              │
│          ▼                                                  │
│  ┌───────────────────────────────────────────────┐         │
│  │       SelectionOverlay                        │         │
│  │  • Fullscreen overlay                         │         │
│  │  • Region selection UI                        │         │
│  │  • Size display                               │         │
│  │  • Selection event handling                   │         │
│  └───────┬───────────────────────────────────────┘         │
│          │                                                  │
│          │ emits selection_made signal                     │
│          └──────────────────────────────────┐              │
└───────────────────────────────────────────────┼──────────────┘
                                               │
                                               │ creates
                                               ▼
┌─────────────────────────────────────────────────────────────┐
│              annotation_window.py                           │
│                                                             │
│  ┌───────────────────────────────────────────────┐         │
│  │       AnnotationTool                          │         │
│  │  • Tool type constants                        │         │
│  │  • PEN, TEXT, ARROW, RECTANGLE, ELLIPSE       │         │
│  └───────────────────────────────────────────────┘         │
│                     ▲                                       │
│                     │ uses                                  │
│  ┌───────────────────────────────────────────────┐         │
│  │       AnnotationWindow                        │         │
│  │  • Toolbar with tool buttons                  │         │
│  │  • Image display and rendering                │         │
│  │  • Annotation drawing logic                   │         │
│  │  • Mouse event handling                       │         │
│  │  • Color/width customization                  │         │
│  │  • Save/Copy functionality                    │         │
│  │  • Window dragging                            │         │
│  └───────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

```
User Action (ALT+F2 or Tray Menu)
        │
        ▼
ScreenCaptureApp.start_capture()
        │
        ├─► Capture screenshot
        │
        ▼
SelectionOverlay shown
        │
        ├─► User drags to select region
        │
        ▼
selection_made signal emitted
        │
        ▼
ScreenCaptureApp.on_selection_made()
        │
        ├─► Crop screenshot to selection
        │
        ▼
AnnotationWindow created & shown
        │
        ├─► User selects tools and annotates
        │
        ▼
Save or Copy
        │
        ├─► Save: QFileDialog → pixmap.save()
        └─► Copy: QApplication.clipboard()
```

## Class Relationships

```
QApplication (PyQt5)
    │
    └─► ScreenCaptureApp
            │
            ├─► QSystemTrayIcon (tray icon)
            │       │
            │       └─► QMenu (context menu)
            │
            ├─► SelectionOverlay (QWidget)
            │       │
            │       └─► selection_made (pyqtSignal)
            │
            └─► List[AnnotationWindow] (QWidget)
                    │
                    ├─► QToolBar (tools)
                    ├─► QLabel (image display)
                    └─► Annotations (list)
```

## Tool Selection Flow

```
User clicks tool button in toolbar
        │
        ▼
AnnotationWindow.set_tool(tool_type)
        │
        ├─► Update current_tool
        ├─► Update button checked states
        │
        ▼
User clicks/drags on image
        │
        ▼
mousePressEvent()
        │
        ├─► Check if toolbar (for dragging)
        └─► Create annotation based on tool type
                │
                ├─► PEN: Create QPainterPath
                ├─► TEXT: Show QInputDialog
                ├─► ARROW: Start/end points
                ├─► RECTANGLE: Start/end points
                └─► ELLIPSE: Start/end points
        │
        ▼
mouseMoveEvent() [if dragging]
        │
        ├─► Update annotation geometry
        └─► Call update_image()
        │
        ▼
mouseReleaseEvent()
        │
        ├─► Finalize annotation
        └─► Add to annotations list
```

## UI Layer Structure

```
┌────────────────────────────────────────┐
│      System Tray (always visible)      │
│  [Icon] Right-click for menu           │
└────────────────────────────────────────┘

When capturing:
┌────────────────────────────────────────┐
│    SelectionOverlay (fullscreen)       │
│                                        │
│  [Darkened screenshot]                 │
│                                        │
│  ┌──────────────────┐                 │
│  │ Selected Region  │ 800 x 600       │
│  │                  │                 │
│  └──────────────────┘                 │
│                                        │
└────────────────────────────────────────┘

After selection:
┌────────────────────────────────────────┐
│ ┌────────────────────────────────────┐ │
│ │ Toolbar (dark themed)              │ │
│ │ [Pen] [Text] [Arrow] [□] [○]      │ │
│ │ [Color] Width:[3] [Save] [Copy]   │ │
│ └────────────────────────────────────┘ │
│ ┌────────────────────────────────────┐ │
│ │                                    │ │
│ │     Captured Image                 │ │
│ │     + Annotations                  │ │
│ │                                    │ │
│ └────────────────────────────────────┘ │
└────────────────────────────────────────┘
```

## Key Design Patterns

### Observer Pattern
- `selection_made` signal connects SelectionOverlay to ScreenCaptureApp
- `destroyed` signal for cleanup of annotation windows

### Singleton-like Pattern
- ScreenCaptureApp maintains single instance per application
- System tray icon persists throughout app lifetime

### Strategy Pattern
- Different annotation tools selected at runtime
- Same drawing interface with different behaviors

### MVC-like Separation
- Model: Screenshot pixmap and annotation data
- View: QLabel displaying the image
- Controller: AnnotationWindow handling events and updates

## Thread Safety

- All UI operations on main Qt thread
- Global hotkey callback executed on keyboard library thread
- Signal/slot mechanism ensures thread-safe communication

## Resource Management

1. **Memory**
   - Screenshot stored temporarily during selection
   - Cleared after cropping to free memory
   - Annotation windows removed from list when closed

2. **System Resources**
   - Global hotkeys unregistered on exit
   - Qt painters explicitly ended
   - Proper cleanup handlers registered

3. **File Handles**
   - QFileDialog used for safe file operations
   - Error handling for save failures
   - No persistent file handles kept open
