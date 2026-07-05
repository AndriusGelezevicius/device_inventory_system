from PySide6.QtCore import QDate
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem


def add_record(window):
    from ui.add_record_window import AddRecordWindow
    window.add_window = AddRecordWindow()
    window.add_window.show()

def show_summary(window):
    from ui.show_summary import ShowSummary
    window.add_window = ShowSummary()
    window.add_window.show()

def upload_new_plan(window):
    file_path, _ = QFileDialog.getOpenFileName(
        window, "Choose Excel file",
         "",
        "Excel files (*.xlsx)"

    )
    if not file_path:
        return

    try:
        from openpyxl import load_workbook
        workbook = load_workbook(file_path)
        sheet = workbook.active
# we made data list
        rows = list(sheet.iter_rows(values_only=True))
        if not rows:
            QMessageBox.warning(window, "Empty File", "Excel file is empty.")
            return

        headers = rows[0] # cia bus Device, data, amount
        data_rows = rows[1:] # cia bus FOD6020, 2026-01-05, 5. visos eilutes

        window.table.clear()
        window.table.setColumnCount(len(headers))
        window.table.setRowCount(len(data_rows))
        window.table.setHorizontalHeaderLabels([str(header) for header in headers])
#str()? Nes Excel pirmoje eilutėje teoriškai gali būti ne tekstas, o skaičius arba data. O setHorizontalHeaderLabels() nori gauti tekstų sąrašą

        for row_index, row_data in enumerate(data_rows):
            for col_index, value in enumerate(row_data):
                item = QTableWidgetItem("" if value is None else str(value))
                window.table.setItem(row_index, col_index, item)

    except Exception as error:
        QMessageBox.critical(window, "Error", f"Could not load Excel file:\n{error}")