# Changelog

All notable changes to the Screen Capture & Annotation Tool will be documented in this file.

## [1.1.1] - 2026-02-15

### Fixed
- Fixed screen capture not working on Windows - screenshot was not being captured
  - Replaced unreliable `screen.grabWindow(0)` with multiple fallback methods
  - Added three different capture methods for maximum compatibility
  - Added proper error handling and debug logging
- Fixed selection overlay not appearing in foreground
  - Added `raise_()` and `activateWindow()` to ensure overlay is visible and receives input
- Improved troubleshooting with debug output
  - Added console logging for capture events
  - Logs show which capture method succeeded or which failed

### Added
- Debug logging throughout screen capture process
- Comprehensive troubleshooting documentation in README

## [1.1.0] - 2026-02-13

### Changed
- Updated global hotkey from F1 to ALT+F2 for better compatibility
- Updated all documentation to reflect new hotkey

## [1.0.0] - 2026-01-30

### Added
- Initial release of the screen capture and annotation tool
- Screen region selection with visual overlay
- Global hotkey support (ALT+F2) for quick capture
- System tray integration for easy access
- Annotation tools:
  - Pen tool for freehand drawing
  - Text annotation with custom input
  - Arrow tool for pointing
  - Rectangle shape tool
  - Ellipse/Circle shape tool
- Color picker for all annotation tools
- Adjustable pen width (1-20 pixels)
- Movable annotation window (drag toolbar to move)
- Save functionality (PNG/JPEG formats)
- Copy to clipboard functionality
- Cross-platform design (optimized for Windows)
- Clean, organized class-based architecture
- Comprehensive documentation

### Features
- **Real-time preview**: See size of selection while dragging
- **Undo support**: Close and recapture if needed
- **Intuitive UI**: Modern dark-themed toolbar
- **Non-intrusive**: Minimizes to system tray
- **Lightweight**: Minimal resource usage
- **Fast**: Instant screen capture and annotation

### Technical Details
- Built with PyQt5 for robust GUI
- Uses keyboard library for global hotkeys
- Pillow for image processing
- Windows-optimized with pywin32
- Modular architecture for easy maintenance

## Roadmap

Future enhancements being considered:
- [ ] Undo/Redo for annotations
- [ ] More shape tools (polygon, line)
- [ ] Blur/pixelate tools
- [ ] Screenshot history
- [ ] Custom hotkey configuration
- [ ] Multi-monitor support improvements
- [ ] Cloud upload integration
- [ ] OCR text recognition
- [ ] Auto-save functionality
- [ ] Themes and customization

## Contributing

We welcome contributions! If you'd like to add features or fix bugs, please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available for educational and personal use.
