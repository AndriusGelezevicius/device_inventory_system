from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget, QHeaderView, QHBoxLayout, QPushButton


class ManageDevices(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage devices")
        #self.setFixedSize(300,400)
        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        self.devices_table = QTableWidget()
        self.devices_table.setColumnCount(2)
        self.devices_table.setHorizontalHeaderLabels(["Device", "Group"])
        self.devices_table.verticalHeader().hide()
        # Abu stulpeliai vienodai užpildo lentelės plotį
        self.devices_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.button_add = QPushButton("Add device")
        self.button_add.setObjectName("button_calculate")

        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.setObjectName("button_clear")

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.button_cancel)

        main_layout.addWidget(self.devices_table)
        main_layout.addLayout(layout_buttons)


        self.setLayout(main_layout)