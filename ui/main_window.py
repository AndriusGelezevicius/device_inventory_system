from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QPushButton, QLineEdit, QDateEdit, \
    QSpinBox, QTableWidgetItem, QLabel, QHeaderView


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Inventory System")
        self.setFixedSize(1300, 800)
        self.setup_ui()

    def setup_ui(self):
        self.label_plan = QLabel("Plan", self)
        self.label_plan.setGeometry(500,30,300,50)
        self.label_plan.setObjectName("label_plan")

        self.table = QTableWidget(10,3, self)
        self.table.setHorizontalHeaderLabels(["Name", "Date", "Bank"])
        self.table.setGeometry(50,80,1000,650)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setObjectName("table")


