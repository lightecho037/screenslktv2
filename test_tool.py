"""
Example usage and testing script for the screen capture tool.
"""

import sys


def test_imports():
    """Test that all modules can be imported."""
    try:
        import screen_capture
        import annotation_window
        print("✓ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_class_definitions():
    """Test that all classes are defined."""
    try:
        from screen_capture import ScreenCaptureApp, SelectionOverlay
        from annotation_window import AnnotationWindow, AnnotationTool
        
        print("✓ ScreenCaptureApp class available")
        print("✓ SelectionOverlay class available")
        print("✓ AnnotationWindow class available")
        print("✓ AnnotationTool class available")
        
        # Check tool constants
        assert hasattr(AnnotationTool, 'PEN')
        assert hasattr(AnnotationTool, 'TEXT')
        assert hasattr(AnnotationTool, 'ARROW')
        assert hasattr(AnnotationTool, 'RECTANGLE')
        assert hasattr(AnnotationTool, 'ELLIPSE')
        print("✓ All annotation tools defined")
        
        return True
    except Exception as e:
        print(f"✗ Class definition test error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run tests."""
    print("=" * 50)
    print("Screen Capture Tool - Tests")
    print("=" * 50)
    
    success = True
    
    if not test_imports():
        success = False
    
    if not test_class_definitions():
        success = False
    
    print("=" * 50)
    if success:
        print("All tests passed! Code structure is valid.")
    else:
        print("Some tests failed!")
    print("=" * 50)
    
    print("\nTo run the application:")
    print("  python main.py")
    print("\nNote: Requires a display/GUI environment (Windows recommended).")
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
