from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit, QHBoxLayout
from PySide6.QtCore import QDate, Qt


class AddRecordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Record")
        self.setFixedSize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        # --- Label ---
        self.label_new_device = QLabel("New Record")
        self.label_new_device.setAlignment(Qt.AlignHCenter)

        self.label_date = QLabel("Date:")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)

        layout_date = QHBoxLayout()
        layout_date.addWidget(self.label_date)
        layout_date.addWidget(self.date_edit)
        layout_date.addStretch()

        # --- main layout ---
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(self.label_new_device, alignment=Qt.AlignHCenter)
        main_layout.addLayout(layout_date)

        self.setLayout(main_layout)