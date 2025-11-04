from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QPushButton, QLineEdit, QDateEdit, \
    QSpinBox, QTableWidgetItem, QLabel, QHeaderView, QComboBox
from functions import add_record


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Inventory System")
        self.setFixedSize(1300, 800)
        self.setup_ui()

    def setup_ui(self):
        # --- Label ---
        self.label_plan = QLabel("Plan")
        self.label_plan.setObjectName("label_plan")
        self.label_plan.setAlignment(Qt.AlignCenter)

        # --- Table ---
        self.table = QTableWidget(10, 3)
        self.table.setObjectName("table")
        self.table.setHorizontalHeaderLabels(["Name", "Date", "Bank"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.label_plan)
        left_layout.addWidget(self.table)

        # --- Right column: button + dropdown ---
        self.button_add = QPushButton("Add Record")
        self.button_add.setObjectName("main")


        self.dropdown = QComboBox()
        self.dropdown.setObjectName("dropdown_devices")
        self.dropdown.addItems(["Router", "Switch", "Server", "Laptop"])

        self.button_summary = QPushButton("Show Summary")
        self.button_summary.setObjectName("main")
        self.button_new_plan = QPushButton("Upload new plan")
        self.button_new_plan.setObjectName("main")
        self.button_export_excel = QPushButton("excel")
        self.button_export_excel.setObjectName("export")
        self.button_export_pdf = QPushButton("pdf")
        self.button_export_pdf.setObjectName("export")

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignTop)
        right_layout.setSpacing(20)
        right_layout.setContentsMargins(10, 40, 10, 10)
        right_layout.addWidget(self.button_add)
        right_layout.addWidget(self.dropdown)
        right_layout.addWidget(self.button_summary)
        right_layout.addStretch()
        right_layout.addWidget(self.button_new_plan)

        right_horizont_layout = QHBoxLayout()
        right_horizont_layout.setSpacing(10)
        right_horizont_layout.addWidget(self.button_export_excel)
        right_horizont_layout.addWidget(self.button_export_pdf)

        right_layout.addLayout(right_horizont_layout)

        # --- Main layout ---
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, stretch=3)
        main_layout.addLayout(right_layout, stretch=1)


        self.setLayout(main_layout)


        # --- Button actions ---
        self.button_add.clicked.connect(lambda: add_record(self))



