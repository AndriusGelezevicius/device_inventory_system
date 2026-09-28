from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QTableWidget, QHeaderView, QVBoxLayout


class NewDevice(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Device")
        #self.setFixedSize(300,400)
        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()







        self.button_save = QPushButton("Save")
        self.button_save.setObjectName("button_calculate")

        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.setObjectName("button_clear")

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_cancel)
        layout_buttons.addWidget(self.button_save)

        main_layout.addLayout(layout_buttons)


        self.setLayout(main_layout)