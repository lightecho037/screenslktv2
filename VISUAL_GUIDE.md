# Visual Guide

This document shows what the application looks like during use.

## 1. System Tray Icon

When the application starts, it minimizes to the system tray:

```
System Tray Area:
┌──────────────────────────────────┐
│  [🖼️] ← Screen Capture Tool      │
└──────────────────────────────────┘

Right-click menu:
┌──────────────────────────────────┐
│  Capture Screen (ALT+F2)         │
│  ──────────────────────────────  │
│  Quit                            │
└──────────────────────────────────┘
```

## 2. Selection Overlay (After pressing ALT+F2)

The entire screen darkens, and you can select a region:

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  [Darkened fullscreen view of your desktop]               │
│                                                            │
│    ┌─────────────────────────────┐                        │
│    │                             │                        │
│    │    Selected Region          │  Width x Height        │
│    │    (clear/visible area)     │  displayed here        │
│    │                             │                        │
│    └─────────────────────────────┘                        │
│                                                            │
│  Cursor: Crosshair (+)                                    │
│                                                            │
│  [Rest of screen is darkened]                             │
│                                                            │
└────────────────────────────────────────────────────────────┘

Instructions:
- Click and drag to select region
- See real-time dimensions
- Blue border shows selection
- ESC to cancel
```

## 3. Annotation Window (After selection)

After selecting a region, the annotation window appears:

```
┌──────────────────────────────────────────────────────────────┐
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOOLBAR (Dark Theme - #2d2d30)                           │ │
│ │                                                          │ │
│ │ [✏️ Pen] [📝 Text] [➡️ Arrow] [⬜ Rect] [⭕ Ellipse]     │ │
│ │                                                          │ │
│ │ [🎨 Color] Width: [3▼]  [💾 Save] [📋 Copy] [❌ Close]  │ │
│ └──────────────────────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │                                                          │ │
│ │                                                          │ │
│ │                                                          │ │
│ │            YOUR CAPTURED SCREENSHOT                      │ │
│ │                                                          │ │
│ │         (with annotations drawn on top)                  │ │
│ │                                                          │ │
│ │                                                          │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
     ↑ Drag this area to move the window
```

## 4. Tool Usage Examples

### Pen Tool (Freehand Drawing)
```
┌────────────────────┐
│                    │
│   ___    ___       │  ← Freehand lines
│  /   \  /   \      │    (follow mouse path)
│ |     ||     |     │
│  \___/  \___/      │
│                    │
└────────────────────┘
```

### Text Tool
```
┌────────────────────┐
│                    │
│  Click here ←      │  ← Click to place text
│                    │    Dialog appears for input
│  Hello World!      │    Text appears at click point
│                    │
└────────────────────┘
```

### Arrow Tool
```
┌────────────────────┐
│                    │
│         ┌────────► │  ← Drag from start to end
│  Start  │          │    Arrow with arrowhead
│         │          │    appears
│                    │
└────────────────────┘
```

### Rectangle Tool
```
┌────────────────────┐
│                    │
│  ┌──────────────┐  │  ← Drag to create
│  │              │  │    Outlined rectangle
│  │   Rectangle  │  │    (not filled)
│  └──────────────┘  │
│                    │
└────────────────────┘
```

### Ellipse Tool
```
┌────────────────────┐
│                    │
│     ╭─────────╮    │  ← Drag to create
│    │           │   │    Outlined ellipse/circle
│    │  Ellipse  │   │    (not filled)
│     ╰─────────╯    │
│                    │
└────────────────────┘
```

## 5. Color Picker Dialog

When you click the Color button:

```
┌─────────────────────────────────┐
│  Choose Color                   │
│                                 │
│  ┌───────────────────────────┐  │
│  │                           │  │
│  │   [Color Spectrum]        │  │
│  │                           │  │
│  └───────────────────────────┘  │
│                                 │
│  R: [255] G: [0  ] B: [0  ]    │
│                                 │
│  [OK]  [Cancel]                 │
└─────────────────────────────────┘
```

## 6. Save Dialog

When you click Save:

```
┌─────────────────────────────────────┐
│  Save Image                         │
│                                     │
│  Save in: [Documents ▼]            │
│                                     │
│  File name: [screenshot.png]       │
│                                     │
│  Save as type: [PNG Files ▼]      │
│   • PNG Files (*.png)               │
│   • JPEG Files (*.jpg)              │
│   • All Files (*)                   │
│                                     │
│  [Save]  [Cancel]                   │
└─────────────────────────────────────┘
```

## 7. Multiple Annotation Example

Combined annotations on one screenshot:

```
┌──────────────────────────────────────┐
│  Important Note! ← Text annotation   │
│                                      │
│  ┌────────────────────────┐          │
│  │                        │          │
│  │  ~~~ Freehand mark ~~~ │          │
│  │                     ↓  │          │
│  │     See here ─────────→│          │
│  │                   (Pen)│          │
│  │         ⭕              │          │
│  └────────────────────────┘          │
│                                      │
└──────────────────────────────────────┘
 └── Rectangle  └── Ellipse └── Arrow
```

## 8. Window States

### Initial State
- Window appears at the location where you made the selection
- Frameless window (no title bar)
- Dark toolbar at top
- Screenshot displayed below

### Dragging State
- Click and drag the toolbar to move
- Window follows cursor
- Stays on top of other windows

### Annotating State
- Selected tool highlighted in toolbar
- Cursor changes based on tool
- Real-time drawing feedback
- Annotations appear immediately

## 9. Cursor Appearance

Different cursors for different states:

```
Selection Mode:   +        (Crosshair)
Normal Mode:      ←        (Arrow)
Pen Drawing:      •        (Dot/Pen)
Window Dragging:  ✋        (Hand)
```

## 10. Color Examples

The color picker allows any RGB color:

```
Red annotations:     ━━━━  (255, 0, 0)
Blue annotations:    ━━━━  (0, 0, 255)
Green annotations:   ━━━━  (0, 255, 0)
Yellow annotations:  ━━━━  (255, 255, 0)
Custom colors:       ━━━━  (Any RGB value)
```

## 11. Width Examples

Pen width from 1 to 20 pixels:

```
Width 1:  ─
Width 3:  ━  (default)
Width 5:  ━━
Width 10: ████
Width 20: ████████
```

## Usage Flow Diagram

```
Start Application
      │
      ▼
[Tray Icon appears]
      │
      ├─► Right-click: Show Menu
      └─► Press ALT+F2: Start Capture
            │
            ▼
      [Selection Overlay]
            │
            ├─► Drag to select region
            ├─► ESC to cancel
            │
            ▼
      [Annotation Window]
            │
            ├─► Select Tool
            ├─► Choose Color
            ├─► Set Width
            ├─► Draw Annotations
            │
            ▼
      [Save or Copy]
            │
            ├─► Save: Choose location
            └─► Copy: Goes to clipboard
                  │
                  ▼
            [Paste anywhere]
```

## Tips for Best Visual Results

1. **High Contrast**: Use bright colors on dark backgrounds
2. **Pen Width**: Use width 3-5 for most annotations
3. **Arrows**: Make them long enough to be visible
4. **Text**: Keep it short and clear
5. **Shapes**: Use rectangles to highlight areas
6. **Colors**: Use red for errors, green for success, yellow for warnings

---

**Note**: Actual appearance may vary slightly based on your Windows theme and display settings.
