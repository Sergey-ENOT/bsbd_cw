from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interface.py_files.patient_window import Ui_MW_patient
from db_connector import ConnectorDB
from interface.py_files.see_patient_data import Ui_Form_see_patient_data
from interface.py_files.patient_take_ticket import Ui_Form_patient_take_ticket
import sys
import datetime


class FormSeePatientData(QtWidgets.QWidget):
    def __init__(self):
        super(FormSeePatientData, self).__init__()
        self.ui = Ui_Form_see_patient_data()
        self.ui.setupUi(self)
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.pushButton_close_widget.clicked.connect(self.close_widget)

    def close_widget(self):
        self.hide()

    def repaint_ui(self, surname_p, name_p, patr_p, gender_p, date_b_p, street_p,
                   n_house, n_flat, phone, ins_policy):
        try:
            self.ui.lineEdit_surname_p.setText(surname_p)
            self.ui.lineEdit_name_p.setText(name_p)
            self.ui.lineEdit_patronymic_p.setText(patr_p)
            self.ui.lineEdit_gender_p.setText(gender_p)
            self.ui.lineEdit_date_birth.setText(datetime.datetime.strftime(date_b_p, "%d.%m.%Y"))
            self.ui.lineEdit_street_p.setText(street_p)
            self.ui.lineEdit_n_house_p.setText(str(n_house))
            self.ui.lineEdit_n_flat_p.setText(str(n_flat))
            self.ui.lineEdit_phone_p.setText(phone)
            self.ui.lineEdit_ins_policy_p.setText(ins_policy)
        except Exception as err:
            print("Error:", err)


class FormTakeTicket(QtWidgets.QWidget):
    def __init__(self, connect, id_p):
        super(FormTakeTicket, self).__init__()
        self.ui = Ui_Form_patient_take_ticket()
        self.ui.setupUi(self)
        self.db_con = connect
        self.id_p = id_p
        self.allow_take = False
        self.messagebox = QMessageBox()
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.pushButton_confirm.clicked.connect(self.select_tickets)

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

    def add_items_combo(self, list_args):
        self.ui.comboBox_choose_spec_d.addItems(list_args)

    def select_tickets(self):
        try:
            self.db_con.create_connection()
            res_tickets = self.db_con.func_get_tickets(self.id_p, self.ui.comboBox_choose_spec_d.currentText())
            self.db_con.close_connection()
            self.display_table(res_tickets)
        except Exception as err:
            self.show_messagebox("critical", "Error", str(err))

    def display_table(self, list_args):
        for i in range(self.ui.tableWidget_ticket.rowCount()):
            self.ui.tableWidget_ticket.removeColumn(i)
        list_column_name = ["Номер талона", "Фамилия", "Имя", "Дата приема", "Время приема", "Кабинет"]
        numrows = len(list_args)
        numcolumns = len(list_column_name)
        self.ui.tableWidget_ticket.setColumnCount(numcolumns)
        self.ui.tableWidget_ticket.setHorizontalHeaderLabels(list_column_name)
        self.ui.tableWidget_ticket.setRowCount(numrows)
        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(list_args[row][column], datetime.date):
                    self.ui.tableWidget_ticket.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (list_args[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(list_args[row][column], datetime.time):
                    self.ui.tableWidget_ticket.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (list_args[row][column].strftime('%H:%M'))))
                elif isinstance(list_args[row][column], int):
                    self.ui.tableWidget_ticket.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((str(list_args[row][column]))))
                else:
                    self.ui.tableWidget_ticket.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((list_args[row][column])))


class MWPatient(QtWidgets.QMainWindow):
    def __init__(self, input_id):
        super(MWPatient, self).__init__()
        self.ui = Ui_MW_patient()
        self.ui.setupUi(self)
        self.connect_buttons()
        self.messagebox = QMessageBox()
        self.id_patient = input_id
        self.db_con = ConnectorDB("127.0.0.1", "patient_public", "12345678")
        self.update_ui()
        self.see_edit_win = FormSeePatientData()
        self.take_ticket_win = FormTakeTicket(self.db_con, self.id_patient)
        self.surname = ""
        self.name = ""
        self.patronymic = ""
        self.gender = ""
        self.date_birth = None
        self.street = ""
        self.n_house = 0
        self.n_flat = 0
        self.phone_n = ""
        self.inc_policy = ""
        self.area = -1
        self.get_patient_data()
        self.get_area()
        self.get_specializations()

    def update_ui(self):
        pass

    def connect_buttons(self):
        self.ui.pushButton_see_edit_data.clicked.connect(self.see_edit_data)
        self.ui.pushButton_get_area.clicked.connect(self.show_area)
        self.ui.pushButton_book_ticket.clicked.connect(self.take_ticket)

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

    def get_specializations(self):
        try:
            self.db_con.create_connection()
            list_spec = self.db_con.view_get_specializations()
            self.db_con.close_connection()
            self.take_ticket_win.add_items_combo(list_spec)
        except Exception as err:
            self.show_messagebox("Critical", "Error", str(err))

    def distribution(self, in_tuple):
        try:
            self.surname = in_tuple[0]
            self.name = in_tuple[1]
            self.patronymic = in_tuple[2]
            self.gender = in_tuple[3]
            self.date_birth = in_tuple[4]
            self.street = in_tuple[5]
            self.n_house = in_tuple[6]
            self.n_flat = in_tuple[7]
            self.phone_n = in_tuple[8]
            self.inc_policy = in_tuple[9]
            self.ui.label_welcome_p.setText(f"Пациент: {self.surname} {self.name[0]}. {self.patronymic[0]}.")
        except Exception as err:
            print("Error dist:", err)

    def get_patient_data(self):
        self.db_con.create_connection()
        received_data = self.db_con.func_select_patient_data(self.id_patient)
        self.db_con.close_connection()
        self.distribution(received_data)

    def see_edit_data(self):
        self.see_edit_win.show()
        self.see_edit_win.repaint_ui(self.surname, self.name, self.patronymic, self.gender,
                                     self.date_birth, self.street, self.n_house, self.n_flat,
                                     self.phone_n, self.inc_policy)

    def get_area(self):
        try:
            self.db_con.create_connection()
            self.area = self.db_con.func_get_area(self.id_patient)
            self.db_con.close_connection()
        except Exception as err:
            self.show_messagebox("Critical", "Error", str(err))

    def show_area(self):
        self.show_messagebox("information", "Информационное сообщение", f"Ваш участок: {self.area}")

    def take_ticket(self):
        self.take_ticket_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mw_patient = MWPatient(2)
    mw_patient.show()
    sys.exit(app.exec())
