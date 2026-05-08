"""Program entry point for launching the PyQt5 GUI."""

import sys

from PyQt5.QtWidgets import QApplication

from qt import MainWindow


def main() -> int:
    """Create the Qt application, show the main window, and start the event loop."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    # main.py only starts the GUI; calibration and image processing live in qt.py.
    sys.exit(main())
