# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../interface/ui_files/patient_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MW_patient(object):
    def setupUi(self, MW_patient):
        MW_patient.setObjectName("MW_patient")
        MW_patient.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MW_patient)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_see_edit_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_see_edit_data.setGeometry(QtCore.QRect(10, 110, 151, 51))
        self.pushButton_see_edit_data.setObjectName("pushButton_see_edit_data")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 330, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 330, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_welcome_p = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome_p.setGeometry(QtCore.QRect(70, 10, 211, 51))
        self.label_welcome_p.setStyleSheet("background-color: yellow;")
        self.label_welcome_p.setObjectName("label_welcome_p")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 100, 441, 111))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 410, 551, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 200, 231, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 210, 141, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        MW_patient.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MW_patient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MW_patient.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MW_patient)
        self.statusbar.setObjectName("statusbar")
        MW_patient.setStatusBar(self.statusbar)

        self.retranslateUi(MW_patient)
        QtCore.QMetaObject.connectSlotsByName(MW_patient)

    def retranslateUi(self, MW_patient):
        _translate = QtCore.QCoreApplication.translate
        MW_patient.setWindowTitle(_translate("MW_patient", "Окно для работы пациента"))
        self.pushButton_see_edit_data.setText(_translate("MW_patient", "Редактировать данные"))
        self.pushButton_2.setText(_translate("MW_patient", "Посмотреть талоны"))
        self.pushButton_3.setText(_translate("MW_patient", "Посмотреть приёмы"))
        self.label_welcome_p.setText(_translate("MW_patient", "Добро пожаловать, ФИО пациента"))
        self.label_2.setText(_translate("MW_patient", "всплывающее новое окно.две половины, статичные текущие данные и ввод новых"))
        self.label_3.setText(_translate("MW_patient", "Вывод талонов или приёмов"))
        self.pushButton_4.setText(_translate("MW_patient", "Взять талон"))
        self.pushButton_5.setText(_translate("MW_patient", "Посмотреть мой участок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MW_patient = QtWidgets.QMainWindow()
    ui = Ui_MW_patient()
    ui.setupUi(MW_patient)
    MW_patient.show()
    sys.exit(app.exec_())