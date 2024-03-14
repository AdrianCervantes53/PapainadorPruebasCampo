# Form implementation generated from reading ui file 'utils/Interface/uiDesigns/addCosechaWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_addCosechaWindow(object):
    def setupUi(self, addCosechaWindow):
        addCosechaWindow.setObjectName("addCosechaWindow")
        addCosechaWindow.resize(979, 508)
        addCosechaWindow.setStyleSheet("border-radius: 15px;\n"
"background-color: rgba(61, 255, 181,0);")
        self.gridLayout = QtWidgets.QGridLayout(addCosechaWindow)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.logoutGroupBox = QtWidgets.QGroupBox(parent=addCosechaWindow)
        self.logoutGroupBox.setStyleSheet("background-color: rgb(76, 165, 34);\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"\n"
"")
        self.logoutGroupBox.setTitle("")
        self.logoutGroupBox.setObjectName("logoutGroupBox")
        self.logoutGroupBoxLayout = QtWidgets.QGridLayout(self.logoutGroupBox)
        self.logoutGroupBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.logoutGroupBoxLayout.setSpacing(0)
        self.logoutGroupBoxLayout.setObjectName("logoutGroupBoxLayout")
        spacerItem = QtWidgets.QSpacerItem(192, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.logoutGroupBoxLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.titleLabel = QtWidgets.QLabel(parent=self.logoutGroupBox)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(30)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.logoutGroupBoxLayout.addWidget(self.titleLabel, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.logoutGroupBoxLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.logoutGroupBoxLayout.setColumnStretch(0, 30)
        self.logoutGroupBoxLayout.setColumnStretch(1, 40)
        self.logoutGroupBoxLayout.setColumnStretch(2, 20)
        self.gridLayout.addWidget(self.logoutGroupBox, 0, 0, 1, 1)
        self.closeDialogButton = QtWidgets.QPushButton(parent=addCosechaWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeDialogButton.sizePolicy().hasHeightForWidth())
        self.closeDialogButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(24)
        font.setBold(False)
        self.closeDialogButton.setFont(font)
        self.closeDialogButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(76, 165, 34);\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(190, 67, 42);\n"
"}")
        self.closeDialogButton.setObjectName("closeDialogButton")
        self.gridLayout.addWidget(self.closeDialogButton, 0, 1, 1, 1)
        self.logoutOptionsGroupBox = QtWidgets.QGroupBox(parent=addCosechaWindow)
        self.logoutOptionsGroupBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(216, 216, 216);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.logoutOptionsGroupBox.setTitle("")
        self.logoutOptionsGroupBox.setObjectName("logoutOptionsGroupBox")
        self.acceptDialogButton = QtWidgets.QPushButton(parent=self.logoutOptionsGroupBox)
        self.acceptDialogButton.setGeometry(QtCore.QRect(590, 360, 331, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptDialogButton.sizePolicy().hasHeightForWidth())
        self.acceptDialogButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(True)
        self.acceptDialogButton.setFont(font)
        self.acceptDialogButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(116, 116, 116);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(76, 165, 34);\n"
"}")
        self.acceptDialogButton.setObjectName("acceptDialogButton")
        self.cancelDialogButton = QtWidgets.QPushButton(parent=self.logoutOptionsGroupBox)
        self.cancelDialogButton.setGeometry(QtCore.QRect(70, 360, 331, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelDialogButton.sizePolicy().hasHeightForWidth())
        self.cancelDialogButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(True)
        self.cancelDialogButton.setFont(font)
        self.cancelDialogButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(116, 116, 116);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(190, 67, 42);\n"
"}")
        self.cancelDialogButton.setObjectName("cancelDialogButton")
        self.groupBox = QtWidgets.QGroupBox(parent=self.logoutOptionsGroupBox)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 931, 321))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.fechaLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.fechaLabel.setGeometry(QtCore.QRect(30, 180, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.fechaLabel.setFont(font)
        self.fechaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fechaLabel.setObjectName("fechaLabel")
        self.notaLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.notaLabel.setGeometry(QtCore.QRect(30, 100, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.notaLabel.setFont(font)
        self.notaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.notaLabel.setObjectName("notaLabel")
        self.addNotaLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.addNotaLineEdit.setGeometry(QtCore.QRect(290, 100, 601, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addNotaLineEdit.setFont(font)
        self.addNotaLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addNotaLineEdit.setText("")
        self.addNotaLineEdit.setMaxLength(40)
        self.addNotaLineEdit.setObjectName("addNotaLineEdit")
        self.subtitleLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.subtitleLabel.setGeometry(QtCore.QRect(190, 20, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        font.setBold(True)
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.errorLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.errorLabel.setGeometry(QtCore.QRect(30, 260, 881, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(255, 19, 19);")
        self.errorLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.addFechaDateEdit = QtWidgets.QDateTimeEdit(parent=self.groupBox)
        self.addFechaDateEdit.setGeometry(QtCore.QRect(290, 180, 341, 51))
        self.addFechaDateEdit.setStyleSheet("QDateTimeEdit{\n"
"    font: 18pt \"Arial Rounded MT Bold\";\n"
"padding-left: 15px;\n"
"border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"}\n"
"QAbstractSpinBox::up-button {\n"
"image: url(Recursos/Icons/upArrowB.svg);\n"
"border-top-right-radius: 10px;\n"
"}\n"
"QAbstractSpinBox::up-button:hover {\n"
"background-color: rgb(136, 136, 136);\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"QAbstractSpinBox::up-button:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color: rgb(156, 156, 156);\n"
"}\n"
"QAbstractSpinBox::down-button {\n"
"image: url(Recursos/Icons/downArrowB.svg);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}\n"
"QAbstractSpinBox::down-button:hover {\n"
"background-color: rgb(136, 136, 136);\n"
"}\n"
"QAbstractSpinBox::down-button:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color: rgb(156, 156, 156);\n"
"}\n"
"")
        self.addFechaDateEdit.setObjectName("addFechaDateEdit")
        self.gridLayout.addWidget(self.logoutOptionsGroupBox, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 92)
        self.gridLayout.setColumnStretch(1, 7)
        self.gridLayout.setRowStretch(0, 13)
        self.gridLayout.setRowStretch(1, 87)

        self.retranslateUi(addCosechaWindow)
        self.closeDialogButton.clicked.connect(addCosechaWindow.closeDialog) # type: ignore
        self.cancelDialogButton.clicked.connect(addCosechaWindow.closeDialog) # type: ignore
        self.acceptDialogButton.clicked.connect(addCosechaWindow.doDialogAction) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(addCosechaWindow)
        addCosechaWindow.setTabOrder(self.closeDialogButton, self.addNotaLineEdit)
        addCosechaWindow.setTabOrder(self.addNotaLineEdit, self.cancelDialogButton)
        addCosechaWindow.setTabOrder(self.cancelDialogButton, self.acceptDialogButton)

    def retranslateUi(self, addCosechaWindow):
        _translate = QtCore.QCoreApplication.translate
        addCosechaWindow.setWindowTitle(_translate("addCosechaWindow", "Form"))
        self.titleLabel.setText(_translate("addCosechaWindow", "Agregar Nueva Cosecha"))
        self.closeDialogButton.setText(_translate("addCosechaWindow", "X"))
        self.acceptDialogButton.setText(_translate("addCosechaWindow", "Agregar"))
        self.cancelDialogButton.setText(_translate("addCosechaWindow", "Cancelar"))
        self.fechaLabel.setText(_translate("addCosechaWindow", "Inicio de cosecha:"))
        self.notaLabel.setText(_translate("addCosechaWindow", "Nota de la cosecha:"))
        self.addNotaLineEdit.setPlaceholderText(_translate("addCosechaWindow", "Ej. Terreno plano, temperatura 35°"))
        self.subtitleLabel.setText(_translate("addCosechaWindow", "Ingrese los datos de la Cosecha"))
        self.errorLabel.setText(_translate("addCosechaWindow", "Invalid Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addCosechaWindow = QtWidgets.QWidget()
    ui = Ui_addCosechaWindow()
    ui.setupUi(addCosechaWindow)
    addCosechaWindow.show()
    sys.exit(app.exec())