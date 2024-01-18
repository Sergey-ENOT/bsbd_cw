import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interface.py_files.authorization import Ui_auth_choose
from work_admin import MWAdmin
from work_doctor import MWDoctor
from work_patient import MWPatient
from db_connector import ConnectorDB
import sys


class ChooseAuthWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ChooseAuthWindow, self).__init__()
        self.ui = Ui_auth_choose()
        self.ui.setupUi(self)
        self.add_clicked()
        self.messagebox = QMessageBox()
        self.application = None
        self.selected_radio = ""

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

    def add_clicked(self):
        self.ui.rB_choose_admin.toggled.connect(self.button_state)
        self.ui.rB_choose_doctor.toggled.connect(self.button_state)
        self.ui.rB_choose_patient.toggled.connect(self.button_state)
        self.ui.pB_execute_auth.clicked.connect(self.auth_func)
        self.ui.rB_choose_admin.setChecked(True)

    def button_state(self):
        b = self.sender()
        self.ui.lineEdit_f_arg.setText("")
        self.ui.lineEdit_s_arg.setText("")
        if b.text() == "Администратор" or b.text() == "Врач":
            self.ui.label_enter_f_arg.setText("Логин:")
            self.ui.lineEdit_f_arg.setInputMask("")
            self.ui.label_enter_s_arg.setText("Пароль:")
            self.ui.lineEdit_s_arg.setInputMask("")
            self.ui.lineEdit_s_arg.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.ui.label_enter_f_arg.setText("Страховой полис:")
            self.ui.lineEdit_f_arg.setInputMask("9999999999999999")
            self.ui.label_enter_s_arg.setText("Дата рождения:")
            self.ui.lineEdit_s_arg.setInputMask("9999_99_99")
            self.ui.lineEdit_s_arg.setEchoMode(0)

    def get_radio(self):
        if self.ui.rB_choose_admin.isChecked():
            temp_var = 1
        elif self.ui.rB_choose_doctor.isChecked():
            temp_var = 2
        elif self.ui.rB_choose_patient.isChecked():
            temp_var = 3
        else:
            temp_var = 4
        self.selected_radio = temp_var

    def check_fill(self):
        f_arg = self.ui.lineEdit_f_arg.text().strip()
        s_arg = self.ui.lineEdit_s_arg.text().strip()
        if (len(f_arg) == 0) or (len(s_arg) == 0):
            self.show_messagebox("warning", "Warning", "Обнаружены незаполненные поля\n"
                                                       "либо содержатся только пробелы")
            return False
        return True

    def auth_func(self):
        self.get_radio()
        c_r = self.selected_radio
        if self.check_fill():
            f_arg = self.ui.lineEdit_f_arg.text()
            s_arg = self.ui.lineEdit_s_arg.text()
            if c_r == 1 or c_r == 2:
                try:
                    db_con = ConnectorDB("127.0.0.1", f_arg, s_arg)
                    db_con.create_connection()
                    db_con.close_connection()
                    if c_r == 1:
                        self.hide()
                        self.application = MWAdmin(f_arg, s_arg)
                        self.application.show()
                    else:
                        self.hide()
                        self.application = MWDoctor(f_arg, s_arg)
                        self.application.show()
                except Exception as err:
                    print(err)
                    self.show_messagebox("warning", "Предупреждение", str(err))
            else:
                try:
                    db_con = ConnectorDB("127.0.0.1", "patient_public", "12345678")
                    db_con.create_connection()
                    res_query = db_con.check_patient_data(f_arg, s_arg)
                    db_con.close_connection()
                    if res_query != -1:
                        self.hide()
                        self.application = MWPatient(res_query)
                        self.application.show()
                    else:
                        self.show_messagebox("warning", "Предупреждение", "Неверные данные")
                except Exception as err:
                    self.show_messagebox("warning", "Предупреждение", str(err))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    choose_auth = ChooseAuthWindow()
    choose_auth.show()
    sys.exit(app.exec())

# test_var = ConnectorDB("127.0.0.1", "postgres", "admin123")
# test_var.create_connection()
# test_var.close_connection()
