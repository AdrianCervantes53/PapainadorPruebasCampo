from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QDialog, QInputDialog, QLineEdit
from icecream import ic

from .uiDesigns.confirmWindow import Ui_confirmWindow
from .uiDesigns.messageWindow import Ui_messageWindow
from .Scripts.BaseWindowClasses import BaseWindow


class MessageWindow(BaseWindow, Ui_messageWindow):
    def __init__(self, screen, object):
        super().__init__(screen)

        self.setupUi(self)

        self.setFunction(object)

    def updateText(self, title, text):
        self.titleLabel.setText(title)
        self.messageLabel.setText(text)



class ConfirmWindow(BaseWindow, Ui_confirmWindow):
    def __init__(self, title, text, screen, object):
        super().__init__(screen)
        self.setupUi(self)
        
        self.setFunction(object)

        self.titleLabel.setText(title)
        self.questionLabel.setText(text)

    def doDialogAction(self):
        self.accion = True
        self.exit()
    
    def updateText(self, title, text):
        self.titleLabel.setText(title)
        self.questionLabel.setText(text)








