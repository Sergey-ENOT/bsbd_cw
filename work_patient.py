from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interface.py_files.patient_window import Ui_MW_patient
from db_connector import ConnectorDB
from interface.py_files.see_edit_patient_data import Ui_Form_see_edit_patient_data
import sys


class FormSeeEditPatientData(QtWidgets.QWidget):
    def __init__(self):
        super(FormSeeEditPatientData, self).__init__()
        self.ui = Ui_Form_see_edit_patient_data()
        self.ui.setupUi(self)
        self.connect_buttons()
        self.ui.comboBox_gender_p.addItems(["мужской", "женский"])

    def connect_buttons(self):
        # self.ui.pushButton_edit_data.clicked.connect()
        self.ui.pushButton_close_widget.clicked.connect(self.close_widget)

    def close_widget(self):
        self.hide()

    def repaint_ui(self, surname_p, name_p, patr_p, gender_p, date_b_p, street_p,
                   n_house, n_flat, phone, ins_policy, list_streets):
        try:
            self.ui.comboBox_street_p.addItems(list_streets)
            self.ui.lineEdit_surname_p.setText(surname_p)
            self.ui.lineEdit_name_p.setText(name_p)
            self.ui.lineEdit_patronymic_p.setText(patr_p)
            self.ui.comboBox_gender_p.setCurrentText(gender_p)
            self.ui.dateEdit_date_birth_p.setDate(date_b_p)
            self.ui.comboBox_street_p.setCurrentText(street_p)
            self.ui.lineEdit_n_house_p.setText(str(n_house))
            self.ui.lineEdit_n_flat_p.setText(str(n_flat))
            self.ui.lineEdit_phone_p.setText(phone)
            self.ui.lineEdit_ins_policy_p.setText(ins_policy)
        except Exception as err:
            print("Error:", err)


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
        self.see_edit_win = FormSeeEditPatientData()
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
        self.received_streets = None
        self.get_patient_data()

    def update_ui(self):
        self.ui.pushButton_see_edit_data.setText("Просмотреть или\nредактировать данные")

    def connect_buttons(self):
        self.ui.pushButton_see_edit_data.clicked.connect(self.see_edit_data)

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
        temp_streets = self.db_con.view_get_streets_title()
        self.received_streets = [x[0] for x in temp_streets]
        self.db_con.close_connection()
        print(received_data)
        print("streets:", self.received_streets)
        self.distribution(received_data)

    def see_edit_data(self):
        self.see_edit_win.show()
        self.see_edit_win.repaint_ui(self.surname, self.name, self.patronymic, self.gender,
                                     self.date_birth, self.street, self.n_house, self.n_flat,
                                     self.phone_n, self.inc_policy, self.received_streets)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mw_patient = MWPatient(2)
    mw_patient.show()
    sys.exit(app.exec())
