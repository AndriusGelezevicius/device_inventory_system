from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget


class ManageDevices(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage devices")
        self.setFixedSize(300,400)
        self.setup_ui()

    def setup_ui(self):
        # self.label_new_device = QLabel("Devices")
        # self.label_new_device.setAlignment(Qt.AlignHCenter)
        #
        # main_layout = QVBoxLayout()
        # main_layout.addWidget(self.label_new_device, alignment=Qt.AlignHCenter)
        # self.setLayout(main_layout)

        self.devices_table = QTableWidget()

