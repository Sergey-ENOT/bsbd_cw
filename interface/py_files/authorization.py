# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../interface/ui_files/authorization.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_auth_choose(object):
    def setupUi(self, auth_choose):
        auth_choose.setObjectName("auth_choose")
        auth_choose.resize(392, 403)
        font = QtGui.QFont()
        font.setPointSize(5)
        auth_choose.setFont(font)
        self.centralwidget = QtWidgets.QWidget(auth_choose)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pB_execute_auth = QtWidgets.QPushButton(self.centralwidget)
        self.pB_execute_auth.setGeometry(QtCore.QRect(10, 310, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pB_execute_auth.setFont(font)
        self.pB_execute_auth.setObjectName("pB_execute_auth")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 50, 131, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rB_choose_admin = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rB_choose_admin.setFont(font)
        self.rB_choose_admin.setObjectName("rB_choose_admin")
        self.verticalLayout.addWidget(self.rB_choose_admin)
        self.rB_choose_doctor = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rB_choose_doctor.setFont(font)
        self.rB_choose_doctor.setObjectName("rB_choose_doctor")
        self.verticalLayout.addWidget(self.rB_choose_doctor)
        self.rB_choose_patient = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rB_choose_patient.setFont(font)
        self.rB_choose_patient.setObjectName("rB_choose_patient")
        self.verticalLayout.addWidget(self.rB_choose_patient)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 180, 371, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_enter_f_arg = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_enter_f_arg.sizePolicy().hasHeightForWidth())
        self.label_enter_f_arg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enter_f_arg.setFont(font)
        self.label_enter_f_arg.setText("")
        self.label_enter_f_arg.setObjectName("label_enter_f_arg")
        self.verticalLayout_2.addWidget(self.label_enter_f_arg)
        self.lineEdit_f_arg = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_f_arg.setFont(font)
        self.lineEdit_f_arg.setObjectName("lineEdit_f_arg")
        self.verticalLayout_2.addWidget(self.lineEdit_f_arg)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_enter_s_arg = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_enter_s_arg.sizePolicy().hasHeightForWidth())
        self.label_enter_s_arg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enter_s_arg.setFont(font)
        self.label_enter_s_arg.setText("")
        self.label_enter_s_arg.setObjectName("label_enter_s_arg")
        self.verticalLayout_3.addWidget(self.label_enter_s_arg)
        self.lineEdit_s_arg = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_s_arg.setFont(font)
        self.lineEdit_s_arg.setInputMask("")
        self.lineEdit_s_arg.setObjectName("lineEdit_s_arg")
        self.verticalLayout_3.addWidget(self.lineEdit_s_arg)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        auth_choose.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(auth_choose)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
        self.menubar.setObjectName("menubar")
        auth_choose.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(auth_choose)
        self.statusbar.setObjectName("statusbar")
        auth_choose.setStatusBar(self.statusbar)

        self.retranslateUi(auth_choose)
        QtCore.QMetaObject.connectSlotsByName(auth_choose)

    def retranslateUi(self, auth_choose):
        _translate = QtCore.QCoreApplication.translate
        auth_choose.setWindowTitle(_translate("auth_choose", "Окно авторизации"))
        self.label.setText(_translate("auth_choose", "Выберите вашу роль"))
        self.pB_execute_auth.setText(_translate("auth_choose", "Авторизоваться"))
        self.rB_choose_admin.setText(_translate("auth_choose", "Администратор"))
        self.rB_choose_doctor.setText(_translate("auth_choose", "Врач"))
        self.rB_choose_patient.setText(_translate("auth_choose", "Пациент"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    auth_choose = QtWidgets.QMainWindow()
    ui = Ui_auth_choose()
    ui.setupUi(auth_choose)
    auth_choose.show()
    sys.exit(app.exec_())
