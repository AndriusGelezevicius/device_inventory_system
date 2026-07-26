from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit, QHBoxLayout, \
    QComboBox, QMessageBox
from PySide6.QtCore import QDate, Qt
from services.device_service import load_devices
from services.records_service import save_record


class AddRecordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Record")
        self.setFixedSize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        # --- Label ---
        self.label_new_device = QLabel("New Record")
        self.label_new_device.setAlignment(Qt.AlignHCenter)

        # --- Date layout ---
        self.label_date = QLabel("Date:")
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.date_edit.setCalendarPopup(True)

        layout_date = QHBoxLayout()
        layout_date.addWidget(self.label_date)
        layout_date.addWidget(self.date_edit)
        layout_date.addStretch()

        # --- Device layout ---

        self.label_device = QLabel("Device:")

        self.dropdown = QComboBox()
        self.dropdown.addItems(load_devices())

        layout_device = QHBoxLayout()
        layout_device.addWidget(self.label_device)
        layout_device.addWidget(self.dropdown)
        layout_device.addStretch()

        # --- Quantity layout ---
        self.label_quantity = QLabel("Amount:")
        self.quantity = QSpinBox()
        self.quantity.setRange(0, 200)
        self.quantity.setSingleStep(1)
        self.quantity.setValue(1)

        layout_quantity = QHBoxLayout()
        layout_quantity.addWidget(self.label_quantity)
        layout_quantity.addWidget(self.quantity)
        layout_quantity.addStretch()


        # --- Buttons layout ---

        self.button_cancel = QPushButton("Cancel")
        self.button_add = QPushButton("Add")

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_cancel)
        layout_buttons.addWidget(self.button_add)


        # --- main layout ---
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        main_layout.addWidget(self.label_new_device, alignment=Qt.AlignHCenter)
        main_layout.addLayout(layout_date)
        main_layout.addLayout(layout_device)
        main_layout.addLayout(layout_quantity)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

        self.button_cancel.clicked.connect(self.close)
        self.button_add.clicked.connect(self.add_record)

    # --- methods ---
    def add_record(self):
        record_date = self.date_edit.date().toString("yyyy-MM-dd")
        device = self.dropdown.currentText()
        amount = self.quantity.value()

        if amount == 0:
            QMessageBox.warning(
                self,
                "Invalid amount",
                "Amount must be greater than zero!"
            )
            return

        record = {
            "date": record_date,
            "device": device,
            "amount": amount
        }

        save_record(record)

        QMessageBox.information(
            self,
            "Record added",
            f"{amount} units of {device} were added"
        )

        self.close()