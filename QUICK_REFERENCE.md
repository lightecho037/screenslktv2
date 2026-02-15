# Quick Reference Guide

## Installation (One-Time Setup)

```bash
# 1. Clone the repository
git clone https://github.com/lightecho037/screenslktv2.git
cd screenslktv2

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python main.py
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **ALT+F2** | Start screen capture |
| **ESC** | Cancel selection |
| **Click + Drag** | Select region |

## Annotation Tools

| Tool | Icon | Usage |
|------|------|-------|
| **Pen** | ✏️ | Freehand drawing |
| **Text** | 📝 | Add text (click to place) |
| **Arrow** | ➡️ | Draw arrow (drag from start to end) |
| **Rectangle** | ⬜ | Draw rectangle (drag to size) |
| **Ellipse** | ⭕ | Draw circle/ellipse (drag to size) |

## Common Tasks

### Capture Screen Region
1. Press **ALT+F2** (or right-click tray icon → "Capture Screen")
2. Click and drag to select region
3. Release mouse to capture

### Annotate
1. After capture, select tool from toolbar
2. Click/drag on image to annotate
3. Use **Color** button to change color
4. Adjust **Width** spinner to change pen size

### Save Image
1. Click **💾 Save** button
2. Choose location and filename
3. Select format (PNG or JPEG)
4. Click Save

### Copy to Clipboard
1. Click **📋 Copy** button
2. Paste in any application (Ctrl+V)

### Move Window
- Click and drag the **dark toolbar area** to move the window

### Close
- Click **❌ Close** button or close window normally

## Troubleshooting Quick Fixes

### ALT+F2 Hotkey Not Working
- Run as Administrator
- Or use tray icon menu instead

### Can't See Tray Icon
- Click the **↑** arrow in system tray
- Check hidden icons area

### Application Won't Start
```bash
# Check Python version (need 3.7+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## File Locations

- **Saved Screenshots**: Where you choose to save them
- **Application**: Where you extracted/cloned the repository
- **Configuration**: No config files (everything in memory)

## Tips & Tricks

1. **Precise Selection**: Use zoom in your display settings for pixel-perfect selection
2. **Quick Capture**: ALT+F2 is fastest way to capture
3. **Color Coding**: Use different colors for different types of annotations
4. **Text Size**: Currently 12pt, adjustable in future versions
5. **Multiple Windows**: You can have multiple annotation windows open

## System Requirements

- **OS**: Windows 10/11 (recommended)
- **Python**: 3.7 or higher
- **RAM**: 100MB minimum
- **Disk**: 50MB for application + screenshot storage

## Getting Help

1. Check [README.md](README.md) for detailed documentation
2. See [INSTALL.md](INSTALL.md) for installation help
3. Review [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
4. Check [CHANGELOG.md](CHANGELOG.md) for version history

## Uninstall

1. Close the application (right-click tray icon → Quit)
2. Delete the project folder
3. (Optional) Uninstall packages:
   ```bash
   pip uninstall PyQt5 pillow keyboard pywin32
   ```

---

**Need more help?** See the full documentation in README.md
