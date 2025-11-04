from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit, QHBoxLayout, \
    QComboBox
from PySide6.QtCore import QDate, Qt

class ShowSummary(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Summary")
        self.setFixedSize(600,600)
        self.setup_ui()

    def setup_ui(self):
        # --- Date layout ---
        self.label_date = QLabel("Dates:")
        self.button_choose_dates = QPushButton("Choose dates")

        layout_dates = QHBoxLayout()
        layout_dates.addWidget(self.label_date)
        layout_dates.addWidget(self.button_choose_dates)
        layout_dates.addStretch()


        # --- main layout ---
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)
        main_layout.addLayout(layout_dates)

        self.setLayout(main_layout)