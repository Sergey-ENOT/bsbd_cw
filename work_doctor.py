from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interface.py_files.doctor_window import Ui_MW_doctor
from interface.py_files.start_reception import Ui_Form_start_reception
from interface.py_files.history_receptions import Ui_Form_history_receptions
from db_connector import ConnectorDB
from security_functions import check_empty
import datetime
import sys


class FormHistoryReceptions(QtWidgets.QWidget):
    def __init__(self, connect):
        super(FormHistoryReceptions, self).__init__()
        self.ui = Ui_Form_history_receptions()
        self.ui.setupUi(self)
        self.db_con = connect
        self.id_t = ""
        self.list_column_name = ["Номер талона", "Специальность", "Фамилия", "Имя",
                                 "Дата приема", "Время приема", "Жалобы", "Диагноз", "Лечение"]
        self.ui.pushButton_select_history.clicked.connect(self.get_receptions)
        self.messagebox = QMessageBox()
        self.update_ui()

    def update_ui(self):
        self.ui.tableWidget_h_r.setColumnCount(len(self.list_column_name))
        self.ui.tableWidget_h_r.setHorizontalHeaderLabels(self.list_column_name)
        self.db_con.create_connection()
        res_spec = self.db_con.view_get_specializations()
        self.db_con.close_connection()
        self.ui.comboBox_spec_d.addItems(res_spec)

    def set_data(self, id_t):
        self.id_t = id_t
        print(self.id_t)

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

    def clean_table(self):
        self.ui.tableWidget_h_r.setRowCount(0)

    def display_table(self, list_args):
        self.clean_table()
        numrows = len(list_args)
        numcolumns = len(self.list_column_name)
        self.ui.tableWidget_h_r.setRowCount(numrows)
        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(list_args[row][column], datetime.date):
                    self.ui.tableWidget_h_r.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (list_args[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(list_args[row][column], datetime.time):
                    self.ui.tableWidget_h_r.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (list_args[row][column].strftime('%H:%M'))))
                elif isinstance(list_args[row][column], int):
                    self.ui.tableWidget_h_r.setItem(row, column,
                                                    QtWidgets.QTableWidgetItem((str(list_args[row][column]))))
                else:
                    self.ui.tableWidget_h_r.setItem(row, column,
                                                    QtWidgets.QTableWidgetItem((list_args[row][column])))

    def get_receptions(self):
        try:
            self.db_con.create_connection()
            list_tickets = self.db_con.func_select_reception(self.id_t,
                                                             self.ui.comboBox_spec_d.currentText(),
                                                             self.ui.dateEdit_start_date.date().toPyDate(),
                                                             self.ui.dateEdit_end_date.date().toPyDate(),
                                                             1)
            self.db_con.close_connection()
            self.display_table(list_tickets)
        except Exception as err:
            self.show_messagebox("critical", "Error", str(err))


class FormStartReception(QtWidgets.QWidget):
    def __init__(self, connect, id_spec):
        super(FormStartReception, self).__init__()
        self.ui = Ui_Form_start_reception()
        self.ui.setupUi(self)
        self.db_con = connect
        self.allow_rec = False
        self.spec_id = id_spec
        self.h_r_win = FormHistoryReceptions(self.db_con)
        self.messagebox = QMessageBox()
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.pushButton_find_ticket.clicked.connect(self.find_n_ticket)
        self.ui.pushButton_record_reception.clicked.connect(self.record_reception)
        self.ui.pushButton_select_history.clicked.connect(self.select_history)

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

    def default_values(self):
        self.allow_rec = False
        self.ui.lineEdit_enter_n_t.setText("")
        self.ui.lineEdit_surname_p.setText("")
        self.ui.lineEdit_name_p.setText("")
        self.ui.lineEdit_patr_p.setText("")
        self.ui.dateEdit_date_b_p.setDate(datetime.date(2000, 1, 1))
        self.ui.textEdit_complains.setPlainText("")
        self.ui.textEdit_diagnosis.setPlainText("")
        self.ui.textEdit_therapy.setPlainText("")

    def find_n_ticket(self):
        n_t = self.ui.lineEdit_enter_n_t.text().strip()
        if len(n_t) == 0:
            self.show_messagebox("information", "Information", "Пустое поле с\nномером талона")
            self.allow_rec = False
        else:
            try:
                self.db_con.create_connection()
                res_patient = self.db_con.func_get_ticket_data(n_t)
                self.db_con.close_connection()
                self.ui.lineEdit_surname_p.setText(res_patient[0])
                self.ui.lineEdit_name_p.setText(res_patient[1])
                self.ui.lineEdit_patr_p.setText(res_patient[2])
                self.ui.dateEdit_date_b_p.setDate(res_patient[3])
                self.allow_rec = True
            except Exception as err:
                self.show_messagebox("critical", "Error", str(err))

    def record_reception(self):
        if self.allow_rec:
            list_args = [self.ui.lineEdit_enter_n_t.text().strip(),
                         self.ui.textEdit_complains.toPlainText().strip(),
                         self.ui.textEdit_diagnosis.toPlainText().strip(),
                         self.ui.textEdit_therapy.toPlainText().strip()]
            if check_empty(list_args):
                try:
                    self.db_con.create_connection()
                    self.db_con.proc_record_reception(list_args)
                    self.db_con.close_connection()
                    self.show_messagebox("information", "Information", "Запись добавлена")
                    self.default_values()
                except Exception as err:
                    print(err)
                    self.show_messagebox("critical", "Error", str(err))
            else:
                self.show_messagebox("warning", "Error", "Обнаружены пустые поля")
        else:
            self.show_messagebox("warning", "Error", "Сначала нужно выполнить\nпоиск талона")

    def select_history(self):
        if self.allow_rec:
            list_args = [self.ui.lineEdit_enter_n_t.text().strip()]
            if check_empty(list_args):
                try:
                    self.h_r_win.set_data(self.ui.lineEdit_enter_n_t.text().strip())
                    self.h_r_win.show()
                except Exception as err:
                    print(err)
                    self.show_messagebox("critical", "Error", str(err))
            else:
                self.show_messagebox("warning", "Error", "Пустое поле с номером талона")
        else:
            self.show_messagebox("warning", "Error", "Сначала нужно выполнить\nпоиск талона")


class MWDoctor(QtWidgets.QMainWindow):
    def __init__(self, log_str, pas_str):
        super(MWDoctor, self).__init__()
        self.ui = Ui_MW_doctor()
        self.ui.setupUi(self)
        self.log_str = log_str
        self.pas_str = pas_str
        self.id_d = ""
        self.surname_d = ""
        self.name_d = ""
        self.patr_d = ""
        self.spec_d = ""
        self.id_spec = 0
        self.db_con = ConnectorDB("127.0.0.1", log_str, pas_str)
        self.messagebox = QMessageBox()
        self.get_data()
        self.start_rec_win = FormStartReception(self.db_con, self.id_spec)
        self.connect_buttons()
        self.update_ui()

    def update_ui(self):
        self.ui.label_doctor_data.setText(f"Номер личного дела: {self.id_d}\n"
                                          f"Ф.И.О: {self.surname_d} {self.name_d[0]}.{self.patr_d[0]}.\n"
                                          f"Специальность: {self.spec_d}({self.id_spec})")

    def connect_buttons(self):
        self.ui.pushButton_start_reception.clicked.connect(self.start_reception)

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

    def get_data(self):
        try:
            self.db_con.create_connection()
            res_list = self.db_con.func_get_doctor_data(self.log_str)
            self.db_con.close_connection()
            self.id_d = res_list[0]
            self.surname_d = res_list[1]
            self.name_d = res_list[2]
            self.patr_d = res_list[3]
            self.spec_d = res_list[4]
            self.id_spec = res_list[5]
        except Exception as err:
            self.show_messagebox("critical", "Error", str(err))

    def start_reception(self):
        self.start_rec_win.default_values()
        self.start_rec_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mw_doctor = MWDoctor("f", "f")
    mw_doctor.show()
    sys.exit(app.exec())
