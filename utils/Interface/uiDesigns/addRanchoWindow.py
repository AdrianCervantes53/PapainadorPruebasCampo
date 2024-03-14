# Form implementation generated from reading ui file 'utils/Interface/uiDesigns/addRanchoWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_addRanchoWindow(object):
    def setupUi(self, addRanchoWindow):
        addRanchoWindow.setObjectName("addRanchoWindow")
        addRanchoWindow.resize(979, 1080)
        addRanchoWindow.setStyleSheet("border-radius: 15px;\n"
"background-color: rgba(61, 255, 181,0);")
        self.gridLayout = QtWidgets.QGridLayout(addRanchoWindow)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.logoutGroupBox = QtWidgets.QGroupBox(parent=addRanchoWindow)
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
        self.closeDialogButton = QtWidgets.QPushButton(parent=addRanchoWindow)
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
        self.logoutOptionsGroupBox = QtWidgets.QGroupBox(parent=addRanchoWindow)
        self.logoutOptionsGroupBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(216, 216, 216);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.logoutOptionsGroupBox.setTitle("")
        self.logoutOptionsGroupBox.setObjectName("logoutOptionsGroupBox")
        self.acceptDialogButton = QtWidgets.QPushButton(parent=self.logoutOptionsGroupBox)
        self.acceptDialogButton.setGeometry(QtCore.QRect(580, 880, 331, 81))
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
        self.cancelDialogButton.setGeometry(QtCore.QRect(110, 880, 331, 81))
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
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 931, 831))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.addDireccionLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.addDireccionLineEdit.setGeometry(QtCore.QRect(350, 490, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addDireccionLineEdit.setFont(font)
        self.addDireccionLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addDireccionLineEdit.setText("")
        self.addDireccionLineEdit.setMaxLength(50)
        self.addDireccionLineEdit.setObjectName("addDireccionLineEdit")
        self.estadoLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.estadoLabel.setGeometry(QtCore.QRect(80, 300, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.estadoLabel.setFont(font)
        self.estadoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.estadoLabel.setObjectName("estadoLabel")
        self.ranchoNameLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.ranchoNameLabel.setGeometry(QtCore.QRect(80, 100, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.ranchoNameLabel.setFont(font)
        self.ranchoNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ranchoNameLabel.setObjectName("ranchoNameLabel")
        self.paisLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.paisLabel.setGeometry(QtCore.QRect(80, 200, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.paisLabel.setFont(font)
        self.paisLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.paisLabel.setObjectName("paisLabel")
        self.localidadLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.localidadLabel.setGeometry(QtCore.QRect(80, 400, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.localidadLabel.setFont(font)
        self.localidadLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.localidadLabel.setObjectName("localidadLabel")
        self.addRanchoLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.addRanchoLineEdit.setGeometry(QtCore.QRect(350, 100, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addRanchoLineEdit.setFont(font)
        self.addRanchoLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addRanchoLineEdit.setText("")
        self.addRanchoLineEdit.setMaxLength(50)
        self.addRanchoLineEdit.setObjectName("addRanchoLineEdit")
        self.addPaisLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.addPaisLineEdit.setGeometry(QtCore.QRect(350, 200, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addPaisLineEdit.setFont(font)
        self.addPaisLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addPaisLineEdit.setText("")
        self.addPaisLineEdit.setMaxLength(30)
        self.addPaisLineEdit.setObjectName("addPaisLineEdit")
        self.addLocalidadLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.addLocalidadLineEdit.setGeometry(QtCore.QRect(350, 400, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addLocalidadLineEdit.setFont(font)
        self.addLocalidadLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addLocalidadLineEdit.setText("")
        self.addLocalidadLineEdit.setMaxLength(50)
        self.addLocalidadLineEdit.setObjectName("addLocalidadLineEdit")
        self.direccionLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.direccionLabel.setGeometry(QtCore.QRect(80, 490, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.direccionLabel.setFont(font)
        self.direccionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.direccionLabel.setObjectName("direccionLabel")
        self.addEstadoLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.addEstadoLineEdit.setGeometry(QtCore.QRect(350, 300, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addEstadoLineEdit.setFont(font)
        self.addEstadoLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addEstadoLineEdit.setText("")
        self.addEstadoLineEdit.setMaxLength(40)
        self.addEstadoLineEdit.setObjectName("addEstadoLineEdit")
        self.subtitleLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.subtitleLabel.setGeometry(QtCore.QRect(200, 20, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        font.setBold(True)
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.errorLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.errorLabel.setGeometry(QtCore.QRect(30, 770, 881, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(255, 19, 19);")
        self.errorLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.coordsGroupBox = QtWidgets.QGroupBox(parent=self.groupBox)
        self.coordsGroupBox.setGeometry(QtCore.QRect(50, 570, 831, 191))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        self.coordsGroupBox.setFont(font)
        self.coordsGroupBox.setStyleSheet("QGroupBox{\n"
"border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"}\n"
"QGroupBox::title {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"border-bottom: 3px solid;\n"
"border-right: 3px solid;\n"
"border-bottom-right-radius: 10px;\n"
"border-color:rgb(156, 156, 156);\n"
"}\n"
"")
        self.coordsGroupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.coordsGroupBox.setFlat(False)
        self.coordsGroupBox.setCheckable(False)
        self.coordsGroupBox.setObjectName("coordsGroupBox")
        self.latitudLabel = QtWidgets.QLabel(parent=self.coordsGroupBox)
        self.latitudLabel.setGeometry(QtCore.QRect(30, 40, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.latitudLabel.setFont(font)
        self.latitudLabel.setStyleSheet("border: none;")
        self.latitudLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.latitudLabel.setObjectName("latitudLabel")
        self.addLatitudLineEdit = QtWidgets.QLineEdit(parent=self.coordsGroupBox)
        self.addLatitudLineEdit.setGeometry(QtCore.QRect(130, 40, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addLatitudLineEdit.setFont(font)
        self.addLatitudLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addLatitudLineEdit.setText("")
        self.addLatitudLineEdit.setMaxLength(10)
        self.addLatitudLineEdit.setObjectName("addLatitudLineEdit")
        self.longitudLabel = QtWidgets.QLabel(parent=self.coordsGroupBox)
        self.longitudLabel.setGeometry(QtCore.QRect(440, 40, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.longitudLabel.setFont(font)
        self.longitudLabel.setStyleSheet("border: none;")
        self.longitudLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.longitudLabel.setObjectName("longitudLabel")
        self.addLongitudLineEdit = QtWidgets.QLineEdit(parent=self.coordsGroupBox)
        self.addLongitudLineEdit.setGeometry(QtCore.QRect(570, 40, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.addLongitudLineEdit.setFont(font)
        self.addLongitudLineEdit.setStyleSheet("border: 3px solid;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);\n"
"padding-left: 5px;")
        self.addLongitudLineEdit.setText("")
        self.addLongitudLineEdit.setMaxLength(10)
        self.addLongitudLineEdit.setObjectName("addLongitudLineEdit")
        self.setCoordsButton = QtWidgets.QPushButton(parent=self.coordsGroupBox)
        self.setCoordsButton.setGeometry(QtCore.QRect(190, 130, 461, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setCoordsButton.sizePolicy().hasHeightForWidth())
        self.setCoordsButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(True)
        self.setCoordsButton.setFont(font)
        self.setCoordsButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(156, 156, 156);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 87, 105);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.setCoordsButton.setObjectName("setCoordsButton")
        self.gridLayout.addWidget(self.logoutOptionsGroupBox, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 90)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 90)

        self.retranslateUi(addRanchoWindow)
        self.closeDialogButton.clicked.connect(addRanchoWindow.closeDialog) # type: ignore
        self.cancelDialogButton.clicked.connect(addRanchoWindow.closeDialog) # type: ignore
        self.acceptDialogButton.clicked.connect(addRanchoWindow.doDialogAction) # type: ignore
        self.setCoordsButton.clicked.connect(addRanchoWindow.setCoordinates) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(addRanchoWindow)
        addRanchoWindow.setTabOrder(self.closeDialogButton, self.addRanchoLineEdit)
        addRanchoWindow.setTabOrder(self.addRanchoLineEdit, self.addPaisLineEdit)
        addRanchoWindow.setTabOrder(self.addPaisLineEdit, self.addEstadoLineEdit)
        addRanchoWindow.setTabOrder(self.addEstadoLineEdit, self.addLocalidadLineEdit)
        addRanchoWindow.setTabOrder(self.addLocalidadLineEdit, self.addDireccionLineEdit)
        addRanchoWindow.setTabOrder(self.addDireccionLineEdit, self.cancelDialogButton)
        addRanchoWindow.setTabOrder(self.cancelDialogButton, self.acceptDialogButton)

    def retranslateUi(self, addRanchoWindow):
        _translate = QtCore.QCoreApplication.translate
        addRanchoWindow.setWindowTitle(_translate("addRanchoWindow", "Form"))
        self.titleLabel.setText(_translate("addRanchoWindow", "Agregar Nuevo Rancho"))
        self.closeDialogButton.setText(_translate("addRanchoWindow", "X"))
        self.acceptDialogButton.setText(_translate("addRanchoWindow", "Agregar"))
        self.cancelDialogButton.setText(_translate("addRanchoWindow", "Cancelar"))
        self.addDireccionLineEdit.setPlaceholderText(_translate("addRanchoWindow", "Ej. Camino Rancho la Alegría "))
        self.estadoLabel.setText(_translate("addRanchoWindow", "Estado:"))
        self.ranchoNameLabel.setText(_translate("addRanchoWindow", "Nombre del Rancho:"))
        self.paisLabel.setText(_translate("addRanchoWindow", "País:"))
        self.localidadLabel.setText(_translate("addRanchoWindow", "Localidad:"))
        self.addRanchoLineEdit.setPlaceholderText(_translate("addRanchoWindow", "Ej. Rancho la Alegría"))
        self.addPaisLineEdit.setPlaceholderText(_translate("addRanchoWindow", "Ej. México"))
        self.addLocalidadLineEdit.setPlaceholderText(_translate("addRanchoWindow", "Ej. León de los Aldama"))
        self.direccionLabel.setText(_translate("addRanchoWindow", "Dirección:"))
        self.addEstadoLineEdit.setPlaceholderText(_translate("addRanchoWindow", "Ej. Guanajuato"))
        self.subtitleLabel.setText(_translate("addRanchoWindow", "Ingrese los datos del Rancho"))
        self.errorLabel.setText(_translate("addRanchoWindow", "Invalid Data"))
        self.coordsGroupBox.setTitle(_translate("addRanchoWindow", "Coordenadas"))
        self.latitudLabel.setText(_translate("addRanchoWindow", "Latitud"))
        self.addLatitudLineEdit.setPlaceholderText(_translate("addRanchoWindow", "Ej. 2447.08700"))
        self.longitudLabel.setText(_translate("addRanchoWindow", "Longitud:"))
        self.addLongitudLineEdit.setPlaceholderText(_translate("addRanchoWindow", "Ej. 12100.52210"))
        self.setCoordsButton.setText(_translate("addRanchoWindow", "Utilizar coordenadas actuales"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addRanchoWindow = QtWidgets.QWidget()
    ui = Ui_addRanchoWindow()
    ui.setupUi(addRanchoWindow)
    addRanchoWindow.show()
    sys.exit(app.exec())