from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit
from PySide6.QtCore import QDate

class AddRecordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Record")
        self.setFixedSize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        # --- Label ---
        self.label_new_device = QLabel("New device")


        layout.addWidget(self.label_new_device)
        self.setLayout(layout)