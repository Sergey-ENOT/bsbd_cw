from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interface.py_files.admin_window import Ui_MW_admin
from db_connector import ConnectorDB
import sys


class MWAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MWAdmin, self).__init__()
        self.ui = Ui_MW_admin()
        self.ui.setupUi(self)
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
    mw_admin = MWAdmin()
    mw_admin.show()
    sys.exit(app.exec())
