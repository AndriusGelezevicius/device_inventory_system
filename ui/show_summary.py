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

        self.label_summary = QLabel("Summary")
        self.label_summary.setObjectName("label_summary")
        self.label_summary_text = QLabel("Choose a period and the device you want to include")
        self.label_summary_text.setObjectName("label_summary_text")

        # --- Date layout ---
        self.label_date_from = QLabel("From")
        self.button_choose_date_from = QPushButton("Choose date")
        self.label_date_until = QLabel("Until")
        self.button_choose_date_until = QPushButton("Choose date")

        layout_summary = QVBoxLayout()
        layout_summary.addWidget(self.label_summary)
        layout_summary.addWidget(self.label_summary_text)

        layout_dates = QHBoxLayout()
        layout_dates.addWidget(self.label_date_from)
        layout_dates.addWidget(self.button_choose_date_from)
        layout_dates.addWidget(self.label_date_until)
        layout_dates.addWidget(self.button_choose_date_until)
        layout_dates.addStretch()

        #  --- selection area ---

        self.selection_text = QLabel("Selection type")
        self.selection_text.setObjectName("selection_text")

        layout_selection = QVBoxLayout()
        layout_selection.addWidget(self.selection_text)





        # --- main layout ---
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)
        main_layout.addLayout(layout_summary)
        main_layout.addLayout(layout_dates)
        main_layout.addLayout(layout_selection)

        self.setLayout(main_layout)