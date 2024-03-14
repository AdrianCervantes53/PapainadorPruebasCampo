from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLineEdit
from icecream import ic

from utils.Interface.Scripts.Validation import validate


class BaseWindow(QWidget):
    dialogAction = pyqtSignal(bool)
    def __init__(self, screen):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.screenGeometry = screen.availableGeometry()
    
    def showDialog(self) -> None:
        x = (self.screenGeometry.width() - self.width()) // 2
        y = (self.screenGeometry.height() - self.height()) // 2

        self.setGeometry(x, y+20, self.width(), self.height())

        self.show()
    
    def setFunction(self, object) -> None:
        self.dialogAction.connect(object)

    def closeDialog(self) -> None:
        self.accion = False
        self.exit()

    def exit(self) -> None:
        self.dialogAction.emit(self.accion)
        self.close()

class BaseInsertWindow(BaseWindow):
    def __init__(self, screen, dbClass, function):
        super().__init__(screen)
        self.dataBase = dbClass
        self.setFunction(function)
        self.data = ""


    def generateErrorMessage(self, diccionario: dict) -> str:
        agrupado_por_valor = {}

        for clave, valor in diccionario.items():
            if valor not in agrupado_por_valor:
                agrupado_por_valor[valor] = [clave]
            else:
                agrupado_por_valor[valor].append(clave)

        elementos = []
        for valor, claves in agrupado_por_valor.items():
            elementos.append(f"{valor}: {', '.join(claves)}")

        resultado = " - ".join(elementos)
        return resultado
    
    def clearData(self) -> None:
        self.errorLabel.hide()
        for child in self.findChildren(QLineEdit):
            if isinstance(child, QLineEdit):
                child.clear()
    
    def setLineEditDict(self, lineEditDict: dict) -> None:
        for child in self.findChildren(QLineEdit):
            if isinstance(child, QLineEdit):
                nombre = child.objectName()
                if nombre == "qt_spinbox_lineedit": continue
                lineEditDict[nombre[3:-8]][0] = child
        self.lineEditDict = lineEditDict

    def doDialogAction(self) -> None:
        self.accion = False
        errors = {}
        for idx in self.lineEditDict:
            validation, tipo = validate.validateData(self.lineEditDict[idx])
            if not validation:
                errors[idx] = tipo

        if any(errors):
            errorMessage = self.generateErrorMessage(errors)
            self.errorLabel.setText(errorMessage)
            self.errorLabel.show()
        else:
            data = {}
            for idx in self.lineEditDict:
                data[idx] = self.lineEditDict[idx][0].text()
            self.finalValidations(data)
    
    def exit(self) -> None:
        self.dialogAction.emit(self.accion, self.data)
        self.close()