from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit
from PySide6.QtCore import QDate, Qt


class AddRecordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Record")
        self.setFixedSize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        # --- Label ---
        self.label_new_device = QLabel("New Record")

        layout.addWidget(self.label_new_device, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.setLayout(layout)