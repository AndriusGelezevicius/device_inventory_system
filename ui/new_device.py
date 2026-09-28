from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QTableWidget, QHeaderView, QVBoxLayout, QLabel, \
    QLineEdit


class NewDevice(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Device")
        # self.setFixedSize(300,)
        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        self.label_add_device = QLabel("Add device")
        self.label_add_device.setObjectName("label_summary")

        self.label_device_name = QLabel("Device name")
        self.input_device_name = QLineEdit()
        self.input_device_name.setPlaceholderText("Enter device name")





        self.button_save = QPushButton("Save")
        self.button_save.setObjectName("button_calculate")

        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.setObjectName("button_clear")


        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_cancel)
        layout_buttons.addWidget(self.button_save)

        main_layout.addWidget(self.label_add_device)
        main_layout.addWidget(self.label_device_name)
        main_layout.addWidget(self.input_device_name)

        main_layout.addLayout(layout_buttons)


        self.setLayout(main_layout)