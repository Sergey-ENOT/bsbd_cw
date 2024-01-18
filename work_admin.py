import sys
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interface.py_files.admin_window import Ui_MW_admin
from interface.py_files.edit_patient_data import Ui_Form_edit_patient_data
from interface.py_files.add_patient_data import Ui_Form_add_patient_data
from interface.py_files.add_doctor_data import Ui_Form_add_doctor_data
from interface.py_files.edit_doctor_data import Ui_Form_edit_doctor_data
from db_connector import ConnectorDB
from security_functions import check_empty


class FormAddPatientData(QtWidgets.QWidget):
    def __init__(self, db_connect):
        super(FormAddPatientData, self).__init__()
        self.ui = Ui_Form_add_patient_data()
        self.db_con = db_connect
        self.ui.setupUi(self)
        self.messagebox = QMessageBox()
        self.connect_buttons()
        self.default_ui()

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

    def connect_buttons(self):
        self.ui.pushButton_close_widget.clicked.connect(self.close_widget)
        self.ui.pushButton_add_patient.clicked.connect(self.add_patient)

    def close_widget(self):
        self.hide()

    def add_combobox(self, f_arg, s_arg):
        self.ui.comboBox_gender_p.addItems(f_arg)
        self.ui.comboBox_street_p.addItems(s_arg)

    def default_ui(self):
        try:
            self.ui.lineEdit_surname_p.setText("")
            self.ui.lineEdit_name_p.setText("")
            self.ui.lineEdit_patronymic_p.setText("")
            self.ui.comboBox_gender_p.setCurrentText("мужской")
            self.ui.dateEdit_date_birth_p.setDate(datetime.date(2000, 1, 1))
            self.ui.lineEdit_n_house_p.setText("")
            self.ui.lineEdit_n_flat_p.setText("")
            self.ui.lineEdit_phone_p.setText("")
            self.ui.lineEdit_ins_policy_p.setText("")
        except Exception as err:
            print("Error:", err)

    def add_patient(self):
        try:
            t_surname = self.ui.lineEdit_surname_p.text().strip().capitalize()
            t_name = self.ui.lineEdit_name_p.text().strip().capitalize()
            t_patronymic = self.ui.lineEdit_patronymic_p.text().strip().capitalize()
            t_gender = self.ui.comboBox_gender_p.currentText()
            t_date = self.ui.dateEdit_date_birth_p.date().toPyDate()
            t_street = self.ui.comboBox_street_p.currentText()
            t_n_h = self.ui.lineEdit_n_house_p.text()
            t_n_f = self.ui.lineEdit_n_flat_p.text()
            t_phone = self.ui.lineEdit_phone_p.text()
            t_ins_p = self.ui.lineEdit_ins_policy_p.text().capitalize()
            list_args = [t_surname, t_name, t_patronymic, t_n_h, t_n_f, t_phone, t_ins_p]
            if check_empty(list_args):
                self.db_con.create_connection()
                self.db_con.proc_add_patient(t_surname, t_name, t_patronymic, t_gender,
                                             t_date, t_street, t_n_h,
                                             t_n_f, t_phone, t_ins_p)
                self.db_con.close_connection()
                self.show_messagebox("information", "Уведомление", "Пациент добавлен")
            else:
                self.show_messagebox("warning", "Error", "Обнаружены пустые поля")
                self.default_ui()
        except Exception as err:
            self.show_messagebox("warning", "Error", str(err))


class FormEditPatientData(QtWidgets.QWidget):
    def __init__(self, connect):
        super(FormEditPatientData, self).__init__()
        self.ui = Ui_Form_edit_patient_data()
        self.ui.setupUi(self)
        self.db_con = connect
        self.allow_edit = False
        self.res_id = -1
        self.res_patient = []
        self.messagebox = QMessageBox()
        self.connect_buttons()

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

    def connect_buttons(self):
        self.ui.pushButton_close_widget.clicked.connect(self.close_widget)
        self.ui.pushButton_edit_patient.clicked.connect(self.edit_patient)
        self.ui.pushButton_find_data.clicked.connect(self.find_data)

    def close_widget(self):
        self.hide()

    def add_combobox(self, f_arg, s_arg):
        self.ui.comboBox_gender_p.addItems(f_arg)
        self.ui.comboBox_street_p.addItems(s_arg)

    def default_ui(self):
        try:
            self.ui.lineEdit_surname_p.setText("")
            self.ui.lineEdit_name_p.setText("")
            self.ui.lineEdit_patronymic_p.setText("")
            self.ui.comboBox_gender_p.setCurrentText("мужской")
            self.ui.dateEdit_date_birth_p.setDate(datetime.date(2000, 1, 1))
            self.ui.lineEdit_n_house_p.setText("")
            self.ui.lineEdit_n_flat_p.setText("")
            self.ui.lineEdit_phone_p.setText("")
            self.ui.lineEdit_ins_policy_p.setText("")
            self.ui.lineEdit_input_ins_policy.setText("")
            self.ui.dateEdit_input_date_b.setDate(datetime.date(2000, 12, 12))
        except Exception as err:
            print("Error:", err)

    def repaint_ui(self, list_data):
        try:
            self.ui.lineEdit_surname_p.setText(list_data[0])
            self.ui.lineEdit_name_p.setText(list_data[1])
            self.ui.lineEdit_patronymic_p.setText(list_data[2])
            self.ui.comboBox_gender_p.setCurrentText(list_data[3])
            self.ui.dateEdit_date_birth_p.setDate(list_data[4])
            self.ui.comboBox_street_p.setCurrentText(list_data[5])
            self.ui.lineEdit_n_house_p.setText(str(list_data[6]))
            self.ui.lineEdit_n_flat_p.setText(str(list_data[7]))
            self.ui.lineEdit_phone_p.setText(list_data[8])
            self.ui.lineEdit_ins_policy_p.setText(list_data[9])
        except Exception as err:
            print("Error:", err)

    def find_data(self):
        try:
            ins_policy = self.ui.lineEdit_input_ins_policy.text()
            date_b = self.ui.dateEdit_input_date_b.date().toPyDate()
            self.db_con.create_connection()
            self.res_id = self.db_con.check_patient_data(ins_policy, date_b)
            if self.res_id != -1:
                self.allow_edit = True
                self.res_patient = self.db_con.func_select_patient_data(self.res_id)
                self.db_con.close_connection()
                self.repaint_ui(self.res_patient)
            else:
                self.db_con.close_connection()
                self.show_messagebox("information", "Information", "Пациент не найден")
        except Exception as err:
            self.show_messagebox("critical", "Error", str(err))

    def edit_patient(self):
        if self.allow_edit:
            try:
                c_surname = self.ui.lineEdit_surname_p.text().strip().capitalize()
                c_name = self.ui.lineEdit_name_p.text().strip().capitalize()
                c_patr = self.ui.lineEdit_patronymic_p.text().strip().capitalize()
                c_gender = self.ui.comboBox_gender_p.currentText()
                c_street = self.ui.comboBox_street_p.currentText()
                c_n_h = self.ui.lineEdit_n_house_p.text().strip()
                c_n_f = self.ui.lineEdit_n_flat_p.text().strip()
                c_phone = self.ui.lineEdit_phone_p.text()
                list_args = [c_surname, c_name, c_patr, c_gender, c_street, c_n_h, c_n_f, c_phone]
                if check_empty(list_args):
                    self.db_con.create_connection()
                    self.db_con.proc_update_patient(self.res_id, c_surname, c_name, c_patr, c_gender,
                                                    c_street, c_n_h, c_n_f, c_phone)
                    self.db_con.close_connection()
                    self.show_messagebox("information", "Information", "Данные успешно обновлены")
                    self.default_ui()
                else:
                    self.show_messagebox("warning", "Warning", "Обнаружены пустые поля")
            except Exception as err:
                self.show_messagebox("critical", "Error", str(err))
        else:
            self.show_messagebox("information", "Information", "Сначала сделайте поиск данных")


class FormAddDoctorData(QtWidgets.QWidget):
    def __init__(self, connect):
        super(FormAddDoctorData, self).__init__()
        self.ui = Ui_Form_add_doctor_data()
        self.ui.setupUi(self)
        self.db_con = connect
        self.res_doctor = []
        self.messagebox = QMessageBox()
        self.connect_buttons()
        self.get_spec_list()

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

    def connect_buttons(self):
        self.ui.pushButton_close_widget.clicked.connect(self.close_widget)
        self.ui.pushButton_add_doctor.clicked.connect(self.add_doctor)

    def close_widget(self):
        self.hide()

    def default_ui(self):
        self.ui.lineEdit_log_doctor.setText(""),
        self.ui.lineEdit_pass_doctor.setText(""),
        self.ui.lineEdit_id_d.setText(""),
        self.ui.lineEdit_surname_d.setText(""),
        self.ui.lineEdit_name_d.setText(""),
        self.ui.lineEdit_patronymic_d.setText(""),
        self.ui.dateEdit_date_birth_d.setDate(datetime.date(2000, 1, 1)),
        self.ui.dateEdit_date_s_w_d.setDate(datetime.date(2000, 1, 1)),

    def add_doctor(self):
        try:
            self.res_doctor = [self.ui.lineEdit_log_doctor.text().strip(),
                               self.ui.lineEdit_pass_doctor.text().strip(),
                               self.ui.lineEdit_id_d.text(),
                               self.ui.lineEdit_surname_d.text().strip().capitalize(),
                               self.ui.lineEdit_name_d.text().strip().capitalize(),
                               self.ui.lineEdit_patronymic_d.text().strip().capitalize()]
            if check_empty(self.res_doctor):
                self.res_doctor.append(self.ui.dateEdit_date_s_w_d.date().toPyDate())
                self.res_doctor.append(self.ui.dateEdit_date_birth_d.date().toPyDate())
                self.res_doctor.append(self.ui.comboBox_spec_d.currentText())
                self.db_con.create_connection()
                self.db_con.proc_add_doctor(self.res_doctor)
                self.db_con.close_connection()
                self.show_messagebox("information", "Information", "Врач добавлен")
                self.default_ui()
            else:
                self.show_messagebox("warning", "Warning", "Обнаружены пустые поля")
        except Exception as err:
            self.show_messagebox("critical", "Error", str(err))

    def get_spec_list(self):
        try:
            self.db_con.create_connection()
            list_spec = self.db_con.view_get_specializations()
            self.ui.comboBox_spec_d.addItems(list_spec)
        except Exception as err:
            self.show_messagebox("critical", "Critical", str(err))


class FormEditDoctorData(QtWidgets.QWidget):
    def __init__(self, connect):
        super(FormEditDoctorData, self).__init__()
        self.ui = Ui_Form_edit_doctor_data()
        self.ui.setupUi(self)
        self.db_con = connect
        self.allow_edit = False
        self.res_doctor = []
        self.messagebox = QMessageBox()
        self.connect_buttons()
        self.get_spec_list()

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

    def connect_buttons(self):
        self.ui.pushButton_close_widget.clicked.connect(self.close_widget)
        self.ui.pushButton_edit_doctor.clicked.connect(self.edit_doctor)
        self.ui.pushButton_find_data.clicked.connect(self.find_data)

    def close_widget(self):
        self.hide()

    def default_ui(self):
        self.ui.lineEdit_input_log_doctor.setText(""),
        self.ui.lineEdit_id_d.setText(""),
        self.ui.lineEdit_surname_d.setText(""),
        self.ui.lineEdit_name_d.setText(""),
        self.ui.lineEdit_patronymic_d.setText(""),
        self.ui.dateEdit_date_s_w.setDate(datetime.date(2000, 1, 1)),
        self.ui.dateEdit_date_b_d.setDate(datetime.date(2000, 1, 1)),

    def repaint_ui(self, list_data):
        try:
            self.ui.lineEdit_id_d.setText(list_data[0])
            self.ui.lineEdit_surname_d.setText(list_data[1])
            self.ui.lineEdit_name_d.setText(list_data[2])
            self.ui.lineEdit_patronymic_d.setText(list_data[3])
            self.ui.dateEdit_date_s_w.setDate(list_data[4])
            self.ui.dateEdit_date_b_d.setDate(list_data[5])
            self.ui.comboBox_spec_d.setCurrentText(list_data[6])
        except Exception as err:
            print("Error:", err)

    def find_data(self):
        in_log = self.ui.lineEdit_input_log_doctor.text().strip()
        try:
            if check_empty([in_log]):
                self.db_con.create_connection()
                self.res_doctor = self.db_con.func_select_doctor_data(self.ui.lineEdit_input_log_doctor.text())
                self.db_con.close_connection()
                self.repaint_ui(self.res_doctor)
                self.allow_edit = True
            else:
                self.show_messagebox("information", "Information", "Незаполненное поле с логином")
        except Exception as err:
            self.show_messagebox("critical", "Error", str(err))

    def edit_doctor(self):
        if self.allow_edit:
            try:
                self.res_doctor = [self.ui.lineEdit_input_log_doctor.text().strip(),
                                   self.ui.lineEdit_surname_d.text().strip().capitalize(),
                                   self.ui.lineEdit_name_d.text().strip().capitalize(),
                                   self.ui.lineEdit_patronymic_d.text().strip().capitalize()]
                if check_empty(self.res_doctor):
                    self.db_con.create_connection()
                    self.db_con.proc_update_doctor(self.res_doctor)
                    self.db_con.close_connection()
                    self.show_messagebox("information", "Information", "Врач добавлен")
                    self.default_ui()
                else:
                    self.show_messagebox("warning", "Warning", "Обнаружены пустые поля")
            except Exception as err:
                self.show_messagebox("critical", "Error", str(err))
        else:
            self.show_messagebox("information", "Information", "Сначала сделайте поиск данных")

    def get_spec_list(self):
        try:
            self.db_con.create_connection()
            list_spec = self.db_con.view_get_specializations()
            self.ui.comboBox_spec_d.addItems(list_spec)
        except Exception as err:
            self.show_messagebox("critical", "Critical", str(err))


class MWAdmin(QtWidgets.QMainWindow):
    def __init__(self, log_str, pas_str):
        super(MWAdmin, self).__init__()
        self.ui = Ui_MW_admin()
        self.ui.setupUi(self)
        self.db_con = ConnectorDB("127.0.0.1", log_str, pas_str)
        self.messagebox = QMessageBox()
        self.add_patient_win = FormAddPatientData(self.db_con)
        self.edit_patient_win = FormEditPatientData(self.db_con)
        self.add_doctor_win = FormAddDoctorData(self.db_con)
        self.edit_doctor_win = FormEditDoctorData(self.db_con)
        self.list_genders = ["мужской", "женский"]
        self.connect_buttons()
        self.get_streets()

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

    def connect_buttons(self):
        self.ui.pushButton_add_patient.clicked.connect(self.add_patient)
        self.ui.pushButton_edit_patient.clicked.connect(self.edit_patient)
        self.ui.pushButton_add_doctor.clicked.connect(self.add_doctor)
        self.ui.pushButton_edit_doctor.clicked.connect(self.edit_doctor)

    def get_streets(self):
        try:
            self.db_con.create_connection()
            list_streets = self.db_con.view_get_streets_title()
            self.db_con.close_connection()
            self.add_patient_win.add_combobox(self.list_genders, list_streets)
            self.edit_patient_win.add_combobox(self.list_genders, list_streets)
        except Exception as err:
            self.show_messagebox("Critical", "Error", str(err))

    def add_patient(self):
        self.add_patient_win.show()
        self.add_patient_win.default_ui()

    def edit_patient(self):
        self.edit_patient_win.show()
        self.edit_patient_win.allow_edit = False
        self.edit_patient_win.default_ui()

    def add_doctor(self):
        self.add_doctor_win.show()
        self.add_doctor_win.default_ui()

    def edit_doctor(self):
        self.edit_doctor_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mw_admin = MWAdmin("d", "d")
    mw_admin.show()
    sys.exit(app.exec())
