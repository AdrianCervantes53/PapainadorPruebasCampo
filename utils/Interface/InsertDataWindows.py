from PyQt6.QtCore import Qt, pyqtSignal, QDate, QDateTime
from PyQt6.QtWidgets import QWidget, QDialog, QInputDialog, QLineEdit
from datetime import date, datetime
from icecream import ic

from utils.Interface.uiDesigns.addRanchoWindow import Ui_addRanchoWindow
from utils.Interface.uiDesigns.addVariedadWindow import Ui_addVariedadWindow
from utils.Interface.uiDesigns.addParcelaWindow import Ui_addParcelaWindow
from utils.Interface.uiDesigns.addCosechaWindow import Ui_addCosechaWindow
from utils.Interface.Scripts.Validation import validate
from utils.Interface.Scripts.BaseWindowClasses import BaseInsertWindow
from utils.GPS.GpsClass import GpsConnection
from utils.Interface.ObjectDictionaries import ValidationDict

class InsertRanchoWindow(BaseInsertWindow, Ui_addRanchoWindow):
    dialogAction = pyqtSignal(bool, str)
    def __init__(self, screen, dbClass, function, key):
        super().__init__(screen, dbClass, function)
        self.setupUi(self)
        self.errorLabel.hide()
        self.setLineEditDict(ValidationDict[key])
        #self.gps = GpsConnection()

    def setIdxs(self, idCliente):
        self.idCliente = idCliente

    def setCoordinates(self):
        #latitud, longitud = self.gps.getCurrentCords()
        latitud, longitud = "1234.56789", "12345.6789"
        if latitud is not None and longitud is not None:
            self.addLatitudLineEdit.setText(str(latitud))
            self.addLongitudLineEdit.setText(str(longitud))
        else:
            self.errorLabel.setText("Error al obtener coordenadas, verifique conexión del GPS")
            self.errorLabel.show()

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
        #self.distance = GpsObject
        #self.gps = GpsConnection()
    
    def setIdxs(self, idRancho, idVariedad):
        self.idRancho = idRancho
        self.idVariedad = idVariedad
    
    def setCoordinates(self):
        #latitud, longitud = self.gps.getCurrentCords()
        latitud, longitud = "1234.56789", "12345.6789"
        if latitud is not None and longitud is not None:
            self.addLatitudLineEdit.setText(str(latitud))
            self.addLongitudLineEdit.setText(str(longitud))
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
