# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../interface/ui_files/start_reception.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_start_reception(object):
    def setupUi(self, Form_start_reception):
        Form_start_reception.setObjectName("Form_start_reception")
        Form_start_reception.resize(812, 511)
        self.pushButton_record_reception = QtWidgets.QPushButton(Form_start_reception)
        self.pushButton_record_reception.setGeometry(QtCore.QRect(590, 450, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_record_reception.setFont(font)
        self.pushButton_record_reception.setObjectName("pushButton_record_reception")
        self.layoutWidget = QtWidgets.QWidget(Form_start_reception)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_enter_n_t = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_enter_n_t.sizePolicy().hasHeightForWidth())
        self.label_enter_n_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enter_n_t.setFont(font)
        self.label_enter_n_t.setAlignment(QtCore.Qt.AlignCenter)
        self.label_enter_n_t.setObjectName("label_enter_n_t")
        self.verticalLayout.addWidget(self.label_enter_n_t)
        self.lineEdit_enter_n_t = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_enter_n_t.sizePolicy().hasHeightForWidth())
        self.lineEdit_enter_n_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_enter_n_t.setFont(font)
        self.lineEdit_enter_n_t.setObjectName("lineEdit_enter_n_t")
        self.verticalLayout.addWidget(self.lineEdit_enter_n_t)
        self.pushButton_find_ticket = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_find_ticket.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_find_ticket.setFont(font)
        self.pushButton_find_ticket.setObjectName("pushButton_find_ticket")
        self.verticalLayout.addWidget(self.pushButton_find_ticket)
        self.layoutWidget1 = QtWidgets.QWidget(Form_start_reception)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 10, 471, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_surname_p = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_surname_p.setFont(font)
        self.label_surname_p.setAlignment(QtCore.Qt.AlignCenter)
        self.label_surname_p.setObjectName("label_surname_p")
        self.verticalLayout_2.addWidget(self.label_surname_p)
        self.lineEdit_surname_p = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_surname_p.setFont(font)
        self.lineEdit_surname_p.setReadOnly(True)
        self.lineEdit_surname_p.setObjectName("lineEdit_surname_p")
        self.verticalLayout_2.addWidget(self.lineEdit_surname_p)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_name_p = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_p.setFont(font)
        self.label_name_p.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_p.setObjectName("label_name_p")
        self.verticalLayout_3.addWidget(self.label_name_p)
        self.lineEdit_name_p = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_name_p.setFont(font)
        self.lineEdit_name_p.setReadOnly(True)
        self.lineEdit_name_p.setObjectName("lineEdit_name_p")
        self.verticalLayout_3.addWidget(self.lineEdit_name_p)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_patr_p = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_patr_p.setFont(font)
        self.label_patr_p.setAlignment(QtCore.Qt.AlignCenter)
        self.label_patr_p.setObjectName("label_patr_p")
        self.verticalLayout_4.addWidget(self.label_patr_p)
        self.lineEdit_patr_p = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_patr_p.setFont(font)
        self.lineEdit_patr_p.setReadOnly(True)
        self.lineEdit_patr_p.setObjectName("lineEdit_patr_p")
        self.verticalLayout_4.addWidget(self.lineEdit_patr_p)
        self.verticalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_date_b_p = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_date_b_p.setFont(font)
        self.label_date_b_p.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date_b_p.setObjectName("label_date_b_p")
        self.verticalLayout_5.addWidget(self.label_date_b_p)
        self.dateEdit_date_b_p = QtWidgets.QDateEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_date_b_p.setFont(font)
        self.dateEdit_date_b_p.setObjectName("dateEdit_date_b_p")
        self.verticalLayout_5.addWidget(self.dateEdit_date_b_p)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(Form_start_reception)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 190, 790, 248))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_res_reception = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_res_reception.setFont(font)
        self.label_res_reception.setAlignment(QtCore.Qt.AlignCenter)
        self.label_res_reception.setObjectName("label_res_reception")
        self.verticalLayout_12.addWidget(self.label_res_reception)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_complains = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_complains.setFont(font)
        self.label_complains.setAlignment(QtCore.Qt.AlignCenter)
        self.label_complains.setObjectName("label_complains")
        self.verticalLayout_6.addWidget(self.label_complains)
        self.textEdit_complains = QtWidgets.QTextEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_complains.setFont(font)
        self.textEdit_complains.setObjectName("textEdit_complains")
        self.verticalLayout_6.addWidget(self.textEdit_complains)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_diagnosis = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_diagnosis.setFont(font)
        self.label_diagnosis.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diagnosis.setObjectName("label_diagnosis")
        self.verticalLayout_7.addWidget(self.label_diagnosis)
        self.textEdit_diagnosis = QtWidgets.QTextEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_diagnosis.setFont(font)
        self.textEdit_diagnosis.setObjectName("textEdit_diagnosis")
        self.verticalLayout_7.addWidget(self.textEdit_diagnosis)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_therapy = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_therapy.setFont(font)
        self.label_therapy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_therapy.setObjectName("label_therapy")
        self.verticalLayout_8.addWidget(self.label_therapy)
        self.textEdit_therapy = QtWidgets.QTextEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_therapy.setFont(font)
        self.textEdit_therapy.setObjectName("textEdit_therapy")
        self.verticalLayout_8.addWidget(self.textEdit_therapy)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.pushButton_select_history = QtWidgets.QPushButton(Form_start_reception)
        self.pushButton_select_history.setGeometry(QtCore.QRect(10, 450, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_select_history.setFont(font)
        self.pushButton_select_history.setObjectName("pushButton_select_history")

        self.retranslateUi(Form_start_reception)
        QtCore.QMetaObject.connectSlotsByName(Form_start_reception)

    def retranslateUi(self, Form_start_reception):
        _translate = QtCore.QCoreApplication.translate
        Form_start_reception.setWindowTitle(_translate("Form_start_reception", "Окно ведения приема"))
        self.pushButton_record_reception.setText(_translate("Form_start_reception", "Создать запись о приеме"))
        self.label_enter_n_t.setText(_translate("Form_start_reception", "Введите № талона"))
        self.pushButton_find_ticket.setText(_translate("Form_start_reception", "Найти талон"))
        self.label.setText(_translate("Form_start_reception", "Данные о пациенте"))
        self.label_surname_p.setText(_translate("Form_start_reception", "Фамилия"))
        self.label_name_p.setText(_translate("Form_start_reception", "Имя"))
        self.label_patr_p.setText(_translate("Form_start_reception", "Отчество"))
        self.label_date_b_p.setText(_translate("Form_start_reception", "Дата рождения"))
        self.label_res_reception.setText(_translate("Form_start_reception", "Результат приема"))
        self.label_complains.setText(_translate("Form_start_reception", "Жалобы"))
        self.label_diagnosis.setText(_translate("Form_start_reception", "Диагноз"))
        self.label_therapy.setText(_translate("Form_start_reception", "Лечение"))
        self.pushButton_select_history.setText(_translate("Form_start_reception", "Вывести историю приемов"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_start_reception = QtWidgets.QWidget()
    ui = Ui_Form_start_reception()
    ui.setupUi(Form_start_reception)
    Form_start_reception.show()
    sys.exit(app.exec_())