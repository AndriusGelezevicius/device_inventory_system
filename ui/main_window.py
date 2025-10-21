from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QPushButton, QLineEdit, QDateEdit, \
    QSpinBox, QTableWidgetItem, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Inventory System")
        self.setGeometry(200, 100, 1300, 800)
        self.setup_ui()

    def setup_ui(self):
        self.label_plan = QLabel("Plan", self)
        # self.label_plan.setGeometry(50,30,300,50)
        self.label_plan.setObjectName("label_plan")
