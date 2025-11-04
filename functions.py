def add_record(window):
    from ui.add_record_window import AddRecordWindow
    window.add_window = AddRecordWindow()
    window.add_window.show()

def show_summary(window):
    from ui.show_summary import ShowSummary
    window.add_window = ShowSummary()
    window.add_window.show()