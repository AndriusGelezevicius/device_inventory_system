from PySide6.QtCore import QDate
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtWidgets import QFileDialog


def add_record(window):
    from ui.add_record_window import AddRecordWindow
    window.add_window = AddRecordWindow()
    window.add_window.show()

def show_summary(window):
    from ui.show_summary import ShowSummary
    window.add_window = ShowSummary()
    window.add_window.show()

def upload_new_plan(window):
    file_path, _ = QFileDialog.getOpenFileName(
        window, "Choose excel file",
        "",
        "Excel files (*.xlsx"

    )
