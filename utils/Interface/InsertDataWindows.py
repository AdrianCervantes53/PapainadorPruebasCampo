from PyQt6.QtCore import Qt, pyqtSignal, QDate, QDateTime
from PyQt6.QtWidgets import QWidget, QDialog, QInputDialog, QLineEdit
from datetime import date, datetime
from icecream import ic

from .uiDesigns.addRanchoWindow import Ui_addRanchoWindow
from .uiDesigns.addVariedadWindow import Ui_addVariedadWindow
from .uiDesigns.addParcelaWindow import Ui_addParcelaWindow
from .uiDesigns.addCosechaWindow import Ui_addCosechaWindow
from .Scripts.Validation import validate
from .Scripts.BaseWindowClasses import BaseInsertWindow
from .Scripts.Coordinates import getCoordinates
from utils.Interface.ObjectDictionaries import ValidationDict

class InsertRanchoWindow(BaseInsertWindow, Ui_addRanchoWindow):
    dialogAction = pyqtSignal(bool, str)
    def __init__(self, screen, dbClass, function, key):
        super().__init__(screen, dbClass, function)
        self.setupUi(self)
        self.errorLabel.hide()
        self.setLineEditDict(ValidationDict[key])

    def setIdxs(self, idCliente):
        self.idCliente = idCliente

    def setCoordinates(self):
        self.addLongitudLineEdit.setText("1234.56789")
        self.addLatitudLineEdit.setText("12345.67890")

    def finalValidations(self, data: dict) -> None:
        data["Coordenadas"] = str(self.addLatitudLineEdit.text() + " " + self.addLongitudLineEdit.text())
        if self.dataBase.ConsultaNombreRancho(data["Rancho"]):
            self.errorLabel.setText(data["Rancho"] + " ya existe")
            self.errorLabel.show()
        else:
            self.dataBase.InsertarRancho(data, self.idCliente)
            ic("inserting ",data["Rancho"])
            self.accion = True
            self.data = data["Rancho"]
            self.exit()

class InsertVariedadWindow(BaseInsertWindow, Ui_addVariedadWindow):
    dialogAction = pyqtSignal(bool, str)
    def __init__(self, screen, dbClass, function, key):
        super().__init__(screen, dbClass, function)
        self.setupUi(self)
        self.errorLabel.hide()
        self.setLineEditDict(ValidationDict[key])
    
    def finalValidations(self, data: dict) -> None:
        if self.dataBase.ConsultaNombreVariedad(data["Variedad"]):
            self.errorLabel.setText(data["Variedad"] + " ya existe")
            self.errorLabel.show()
        else:
            self.dataBase.InsertarVariedad(data)
            ic("inserting ",data["Variedad"])
            self.accion = True
            self.data = data["Variedad"]
            self.exit()

class InsertParcelaWindow(BaseInsertWindow, Ui_addParcelaWindow):
    dialogAction = pyqtSignal(bool, str)
    def __init__(self, screen, dbClass, function, key):
        super().__init__(screen, dbClass, function)
        self.setupUi(self)
        self.errorLabel.hide()
        self.addFechaDateEdit.setDate(QDate.currentDate())    
        self.setLineEditDict(ValidationDict[key])
    
    def setIdxs(self, idRancho, idVariedad):
        self.idRancho = idRancho
        self.idVariedad = idVariedad

    def setCoordinates(self):
        cords, latitud, longitud = getCoordinates()
        if cords:
            self.addLongitudLineEdit.setText(str(latitud))
            self.addLatitudLineEdit.setText(str(longitud))
        else:
            self.errorLabel.setText("Error al obtener coordenadas, verifique conexión del GPS")
            self.errorLabel.show()
    
    def finalValidations(self, data: dict) -> None:
        fecha = self.addFechaDateEdit.date()
        data["Fecha"] = fecha.toPyDate()
        data["Coordenadas"] = str(self.addLatitudLineEdit.text() + " " + self.addLongitudLineEdit.text())
        if self.dataBase.ConsultaNombreParcela(data["Parcela"], self.idRancho):
            self.errorLabel.setText(data["Parcela"] + " ya existe")
            self.errorLabel.show()
        else:
            self.dataBase.InsertarParcela(data, self.idRancho, self.idVariedad)
            ic("inserting ",data["Parcela"])
            ic(data)
            self.accion = True
            self.data = data["Parcela"]
            self.exit()


class InsertCosechaWindow(BaseInsertWindow, Ui_addCosechaWindow):
    dialogAction = pyqtSignal(bool, str)
    def __init__(self, screen, dbClass, function, key):
        super().__init__(screen, dbClass, function)
        self.setupUi(self)
        self.errorLabel.hide()
        self.addFechaDateEdit.setDateTime(QDateTime.currentDateTime())
        self.setLineEditDict(ValidationDict[key])
    
    def setIdxs(self, idRancho, idParcela, idMaquina):
        self.idRancho = idRancho
        self.idParcela = idParcela
        self.idMaquina = idMaquina

    
    def finalValidations(self, data: dict) -> None:
        fecha = self.addFechaDateEdit.dateTime()
        data["Fecha"] = fecha.toPyDateTime()

        self.dataBase.InsertarCosecha(data, self.idRancho, self.idParcela, self.idMaquina)
        idCosecha = self.dataBase.ConsultaUltimaCosecha(data["Fecha"], self.idRancho, self.idParcela, self.idMaquina)
        ic("inserting new cosecha")
        ic(data)
        self.accion = True
        ic(idCosecha[0])
        self.data = str(idCosecha[0])
        self.exit()
