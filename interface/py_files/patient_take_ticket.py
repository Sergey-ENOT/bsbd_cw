# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../interface/ui_files/patient_take_ticket.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_patient_take_ticket(object):
    def setupUi(self, Form_patient_take_ticket):
        Form_patient_take_ticket.setObjectName("Form_patient_take_ticket")
        Form_patient_take_ticket.resize(642, 428)
        self.tableWidget_ticket = QtWidgets.QTableWidget(Form_patient_take_ticket)
        self.tableWidget_ticket.setGeometry(QtCore.QRect(5, 90, 631, 321))
        self.tableWidget_ticket.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_ticket.setObjectName("tableWidget_ticket")
        self.tableWidget_ticket.setColumnCount(0)
        self.tableWidget_ticket.setRowCount(0)
        self.pushButton_confirm = QtWidgets.QPushButton(Form_patient_take_ticket)
        self.pushButton_confirm.setGeometry(QtCore.QRect(290, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.pushButton_take_ticket = QtWidgets.QPushButton(Form_patient_take_ticket)
        self.pushButton_take_ticket.setGeometry(QtCore.QRect(520, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_take_ticket.setFont(font)
        self.pushButton_take_ticket.setObjectName("pushButton_take_ticket")
        self.layoutWidget = QtWidgets.QWidget(Form_patient_take_ticket)
        self.layoutWidget.setGeometry(QtCore.QRect(22, 20, 241, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_choose_spec_d = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_choose_spec_d.setFont(font)
        self.label_choose_spec_d.setAlignment(QtCore.Qt.AlignCenter)
        self.label_choose_spec_d.setObjectName("label_choose_spec_d")
        self.verticalLayout.addWidget(self.label_choose_spec_d)
        self.comboBox_choose_spec_d = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_choose_spec_d.setFont(font)
        self.comboBox_choose_spec_d.setObjectName("comboBox_choose_spec_d")
        self.verticalLayout.addWidget(self.comboBox_choose_spec_d)

        self.retranslateUi(Form_patient_take_ticket)
        QtCore.QMetaObject.connectSlotsByName(Form_patient_take_ticket)

    def retranslateUi(self, Form_patient_take_ticket):
        _translate = QtCore.QCoreApplication.translate
        Form_patient_take_ticket.setWindowTitle(_translate("Form_patient_take_ticket", "Окно выбора талона"))
        self.pushButton_confirm.setText(_translate("Form_patient_take_ticket", "Подтвердить"))
        self.pushButton_take_ticket.setText(_translate("Form_patient_take_ticket", "Взять талон"))
        self.label_choose_spec_d.setText(_translate("Form_patient_take_ticket", "Выберите специальность врача"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_patient_take_ticket = QtWidgets.QWidget()
    ui = Ui_Form_patient_take_ticket()
    ui.setupUi(Form_patient_take_ticket)
    Form_patient_take_ticket.show()
    sys.exit(app.exec_())
