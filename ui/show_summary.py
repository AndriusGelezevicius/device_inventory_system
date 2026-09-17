from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDateEdit, QHBoxLayout, \
    QComboBox, QRadioButton, QButtonGroup, QCheckBox, QGridLayout, QFrame, QTableWidget, QHeaderView
from PySide6.QtCore import QDate, Qt
from pathlib import Path
import json

class ShowSummary(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Summary")
        self.setup_ui()

    def setup_ui(self):

        self.label_summary = QLabel("Summary")
        self.label_summary.setObjectName("label_summary")
        self.label_summary_text = QLabel("Choose a period and the device you want to include")
        self.label_summary_text.setObjectName("label_summary_text")

        # --- Date layout ---
        self.label_date_from = QLabel("From")
        self.button_choose_date_from = QPushButton("Choose date")
        self.label_date_until = QLabel("Until")
        self.button_choose_date_until = QPushButton("Choose date")

        layout_summary = QVBoxLayout()
        layout_summary.addWidget(self.label_summary)
        layout_summary.addWidget(self.label_summary_text)

        layout_dates = QHBoxLayout()
        layout_dates.addWidget(self.label_date_from)
        layout_dates.addWidget(self.button_choose_date_from)
        layout_dates.addWidget(self.label_date_until)
        layout_dates.addWidget(self.button_choose_date_until)
        layout_dates.addStretch()

        #  --- selection area ---
        self.selection_text = QLabel("Selection type")
        self.selection_text.setObjectName("selection_text")
        layout_selection = QVBoxLayout()
        layout_selection.addWidget(self.selection_text)

        self.radio_group = QRadioButton("Group")
        self.radio_individual = QRadioButton("Individual devices")
        self.radio_all_devices = QRadioButton("All devices")

        self.selection_group = QButtonGroup(self)
        self.selection_group.addButton(self.radio_group)
        self.selection_group.addButton(self.radio_individual)
        self.selection_group.addButton(self.radio_all_devices)
        self.radio_group.setChecked(True)

        radio_button_layout = QHBoxLayout()
        radio_button_layout.setSpacing(10)
        radio_button_layout.addWidget(self.radio_group)
        radio_button_layout.addWidget(self.radio_individual)
        radio_button_layout.addWidget(self.radio_all_devices)
        radio_button_layout.addStretch()

        # Choosing group
        self.group_dropdown = QComboBox()
        self.group_dropdown.addItems(["FS", "EXFO", "Videoprobes"])

        # Choosing individual devices from json
        self.devices_container = QWidget()
        devices_layout = QGridLayout(self.devices_container)

        devices_layout.setHorizontalSpacing(15)
        devices_layout.setVerticalSpacing(8)

        devices_path = (Path(__file__).resolve().parent.parent / "data" / "devices.json")
        with open(devices_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        devices = data["devices"]

        columns = 3
        rows = (len(devices) + columns - 1) // columns

        self.device_checkbox = []
        for index, device in enumerate(devices):
            checkbox = QCheckBox(device)
            row = index % rows
            column = index // rows

            devices_layout.addWidget(checkbox, row, column)
            self.device_checkbox.append(checkbox)

        self.button_clear = QPushButton("Clear")
        self.button_clear.setObjectName("button_clear")
        self.button_calculate = QPushButton("Calculate")
        self.button_calculate.setObjectName("button_calculate")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_clear)
        button_layout.addWidget(self.button_calculate)

        # --- Results container ---
        self.results_container = QWidget()
        results_layout = QVBoxLayout(self.results_container)
        results_layout.setContentsMargins(0, 0, 0, 0)

        # line
        self.results_line = QFrame()
        self.results_line.setFrameShape(QFrame.HLine)
        self.results_line.setObjectName("results_line")
        self.results_line.setFixedHeight(1)


        results_label_layout = QHBoxLayout()
        self.results_label = QLabel("Results")
        self.results_label.setObjectName("result_label")
        self.results_total_label = QLabel("Total delivered")


        results_info_layout = QHBoxLayout()
        # time period
        self.results_period = QLabel(":xxx")
        self.results_period.setObjectName("results_period")
        # total devices
        self.results_total = QLabel("xxx")
        self.results_total.setObjectName("results_total")

        # table
        self.results_table = QTableWidget(0, 2)
        self.results_table.setObjectName("results_table")
        self.results_table.setHorizontalHeaderLabels(["Device", "Delivered"])

        self.results_table.verticalHeader().hide()
        # Pirmas stulpelis užima likusį plotį
        header = self.results_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        results_layout.addWidget(self.results_line)
        results_layout.addSpacing(10)

        results_label_layout.addWidget(self.results_label)
        results_label_layout.addStretch()  # Užpildo tarpą tarp tekstų
        results_label_layout.addWidget(self.results_total_label)

        # Rezultatų vartotojas neturi redaguoti
        self.results_table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        results_info_layout.addWidget(self.results_period)
        results_info_layout.addStretch()  # Užpildo tarpą tarp tekstų
        results_info_layout.addWidget(self.results_total)

        results_layout.addLayout(results_label_layout)
        results_layout.addLayout(results_info_layout)
        results_layout.addWidget(self.results_table)


        #self.results_container.hide()




        # --- main layout ---
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)

        main_layout.addLayout(layout_summary)
        main_layout.addLayout(layout_dates)
        main_layout.addLayout(layout_selection)
        main_layout.addLayout(radio_button_layout)
        main_layout.addWidget(self.group_dropdown)
        main_layout.addWidget(self.devices_container)
        main_layout.addLayout(button_layout)
        main_layout.addSpacing(10)

        main_layout.addWidget(self.results_container)

        self.setLayout(main_layout)





        # Signals
        self.radio_group.toggled.connect(self.update_visibility)
        self.radio_individual.toggled.connect(self.update_visibility)
        self.radio_all_devices.toggled.connect(self.update_visibility)
        self.update_visibility()







    def update_visibility(self):
        self.group_dropdown.setVisible(
            self.radio_group.isChecked()
        )
        self.devices_container.setVisible(
            self.radio_individual.isChecked()
        )