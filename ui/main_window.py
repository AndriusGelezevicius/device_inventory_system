from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QPushButton, QLineEdit, QDateEdit, \
    QSpinBox, QTableWidgetItem, QLabel, QHeaderView


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Inventory System")
        self.setFixedSize(1300, 800)
        self.setup_ui()

    def setup_ui(self):

        self.label_plan = QLabel("Plan")
        self.label_plan.setObjectName("label_plan")
        self.label_plan.setAlignment(Qt.AlignCenter)


        self.table = QTableWidget(10, 3)
        self.table.setObjectName("table")
        self.table.setHorizontalHeaderLabels(["Name", "Date", "Bank"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.label_plan)
        left_layout.addWidget(self.table)

        self.button_add = QPushButton("Add Record")
       # self.button_add.setObjectName("btn_add")


        right_layout = QVBoxLayout()
        right_layout.addWidget(self.button_add,alignment=Qt.AlignTop)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, stretch=3)
        main_layout.addLayout(right_layout, stretch=1)


        self.setLayout(main_layout)


