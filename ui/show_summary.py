from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit, QHBoxLayout, \
    QComboBox
from PySide6.QtCore import QDate, Qt

class ShowSummary(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Summary")
        self.setFixedSize(400,800)
        self.setup_ui()

    def setup_ui(self):
        # --- Date layout ---
        self.label_date_from = QLabel("From")
        self.button_choose_date_from = QPushButton("Choose date")
        self.label_date_until = QLabel("Until")
        self.button_choose_date_until = QPushButton("Choose date")

        layout_dates = QVBoxLayout()
        layout_dates.addWidget(self.label_date_from)
        layout_dates.addWidget(self.button_choose_date_from)
        layout_dates.addWidget(self.label_date_until)
        layout_dates.addWidget(self.button_choose_date_until)
        layout_dates.addStretch()



        # --- main layout ---
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)
        main_layout.addLayout(layout_dates)

        self.setLayout(main_layout)