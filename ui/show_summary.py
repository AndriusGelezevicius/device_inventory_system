from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit, QHBoxLayout, \
    QComboBox
from PySide6.QtCore import QDate, Qt

class ShowSummary(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Summary")
        self.setFixedSize(500,400)
        # self.setup_ui()

    # def setup_ui(self):