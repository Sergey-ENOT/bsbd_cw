from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interface.py_files.doctor_window import Ui_MW_doctor
from db_connector import ConnectorDB
import sys


class MWDoctor(QtWidgets.QMainWindow):
    def __init__(self, log_str, pas_str):
        super(MWDoctor, self).__init__()
        self.ui = Ui_MW_doctor()
        self.ui.setupUi(self)
        self.log_str = log_str
        self.pas_str = pas_str
        self.messagebox = QMessageBox()

    def show_messagebox(self, level, title, text):
        if level == "critical":
            self.messagebox.setIcon(QMessageBox.Critical)
        elif level == "warning":
            self.messagebox.setIcon(QMessageBox.Warning)
        elif level == "information":
            self.messagebox.setIcon(QMessageBox.Information)
        self.messagebox.setWindowTitle(title)
        self.messagebox.setText(text)
        self.messagebox.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mw_doctor = MWDoctor()
    mw_doctor.show()
    sys.exit(app.exec())
