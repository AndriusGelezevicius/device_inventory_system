from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QPushButton, QLineEdit, QDateEdit, \
    QSpinBox, QTableWidgetItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Inventory System")
        self.setGeometry(200, 100, 1300, 800)
       # self.setup_ui(self)

   # def setup_ui(self):

