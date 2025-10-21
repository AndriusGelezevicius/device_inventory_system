import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("ui/style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)


    window = MainWindow()
    window.show()
    sys.exit(app.exec())