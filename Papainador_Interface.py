from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QDialog
from PyQt6.QtGui import QImage, QPixmap, QFont, QFontMetrics
from PyQt6.QtCore import Qt, QTimer, QRect
from PyQt6 import QtWidgets
import pyqtgraph as pg
from time import localtime
from datetime import datetime
from icecream import ic

import cv2
import numpy as np

import socket
import sys
import os

from utils.Interface.uiDesigns.Potato_Interface2 import Ui_Papainador
from utils.PotatoDetector import Potato
from utils.Interface.PopupWindows import ConfirmWindow, MessageWindow
from utils.Interface.InsertDataWindows import InsertRanchoWindow, InsertVariedadWindow, InsertParcelaWindow, InsertCosechaWindow
from utils.Interface.Scripts.Graph import GraphClass
from utils.Interface.Scripts.Brightness import Brisho
from utils.GPS.Coordinates import getCoordinates
from utils.Interface.Scripts.Validation import validate


class Papainador(QDialog, Ui_Papainador):
    #estandares = ['Suprema', 'Primera', 'Segunda', 'Tercera', 'Cuarta']
    idMaquina = 1
    twoCams = False

    def __init__(self):
        super(Papainador, self).__init__()

        #Quitar bordes a la ventana
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(1920, 1080)
        self.setupUi(self)
        
        self.showNormal()

        #Crear objetos para el brillo de la pantalla y la grafica de rendimiento de papas
        self.graphObject = GraphClass(self.graphFrame)
        self.brisho = Brisho()
        self.brisho.updateSlider(self.brightSlider)

        serialNumbers = ["215122252177", "234322304889"]
        self.papa = Potato(serialNumbers)
        #crear ventanas secundarias con su respectivo texto y funciones
        screen = QApplication.primaryScreen()
        self.confirmPowerOff = ConfirmWindow("Apagar", "¿Seguro que quiere Apagar la Computadora?", screen, self.handlePowerOffResult)
        self.confirmReboot = ConfirmWindow("Restart", "¿Seguro que quiere Reiniciar la Computadora?", screen, self.handleRebootResult)
        self.confirmLogout = ConfirmWindow("Cerrar sesión", "¿Seguro que quiere Cerrar sesión?", screen, self.handleDialogResult)
        self.cameraDisconnected = ConfirmWindow("Cámara desconectada", "No se encontro ninguna cámara\n"
                                                "¿Reintentar conexion?", screen, self.handleDisconnection)
        self.addNewRancho = InsertRanchoWindow(screen, self.papa.ConexionBD, self.handleRanchoAddition, "Rancho")
        self.addNewVariedad = InsertVariedadWindow(screen, self.papa.ConexionBD, self.handleVariedadAddition, "Variedad")
        self.addNewParcela = InsertParcelaWindow(screen, self.papa.ConexionBD, self.handleParcelaAddition, "Parcela")
        self.addNewCosecha = InsertCosechaWindow(screen, self.papa.ConexionBD, self.handleCosechaAddition, "Cosecha")

        self.statusMessage = MessageWindow(screen, self.enableScreen)


        #Crear timers para la lectura de frames, runtime, grafica y reloj
        fps = 10
        self.ms = int(1000/fps)
        self.timerFrame = QTimer(self)
        self.timerFrame.timeout.connect(self.updateFrame)
        
        if self.twoCams:
            self.timerFrame2 = QTimer(self)
            self.timerFrame2.timeout.connect(self.updateFrame2)

        self.timerGraph = QTimer(self)
        self.timerGraph.timeout.connect(self.graphData)
        self.timerRuntime = QTimer(self)
        self.timerRuntime.timeout.connect(self.updateRunTime)
        self.localTime = QTimer(self)
        self.localTime.timeout.connect(self.updateLocalTime)
        self.localTime.start(1000)

        self.mainStackedWidget.setStyleSheet("QStackedWidget::QToolButton { border: 0px; }")
        self.showStackedWidget.setStyleSheet("QStackedWidget::QToolButton { border: 0px; }")
        self.showStackedWidget.setStyleSheet("border: none;")
        self.settingsStackedWidget.setStyleSheet("QStackedWidget::QToolButton { border: 0px; }")
        self.loginMsgLabel.hide()
        self.logoutButton.hide()
        self.mainStackedWidget.setCurrentIndex(3)

        self.activeButtonColor = "rgb(216, 216, 216)"
        self.inactiveButtonColor = "rgb(90, 90, 90)"
        self.buttonIndexes = [self.frameButton, self.videoButton, self.graphButton, self.mapButton]
        self.updateButtonIndex(1)
        self.ret = False
        

    ######################## Login Panel events ########################
    #loginButton button event
    def loginButtonClick(self):

        userVal, _ = validate.validateData(tuple([self.userEditText, "string"]))
        passwordVal, _ = validate.validateData(tuple([self.passwordEditText, "string"]))

        user = self.papa.ConexionBD.ConsultaLogin(self.userEditText.text(), self.passwordEditText.text()) if userVal and passwordVal else None
        if user is not None:
            self.user = user.NombreUsuario
            self.idUser = user.idUsuario
            cliente = self.papa.ConexionBD.ConsultaCliente(self.idUser)
            self.cliente = cliente.NombreCliente
            self.idCliente = cliente.idCliente
            self.userLabel.setText(cliente.NombreCliente) 
            self.loginInit()
        else:
            self.loginMsgLabel.show()

    #Inicializar interfaz despues del login
    def loginInit(self):
        self.loginWidgetUpdates()

        self.ret = False    
        self.status = False
        self.wifi = False
        self.gps = False

        self.currentDataFlag = False
        self.loadDefaultData()
        self.tryCamConnection()
        

        self.loadRanchoData()

        self.logoutButton.show()
        self.mainStackedWidget.setCurrentIndex(0)
        self.showStackedWidget.setCurrentIndex(1)
        self.updateButtonIndex(1)

    def loginWidgetUpdates(self):        
        self.setStyleSheet("background-color: rgb(46, 47, 58);")

        self.selectDataButton.setEnabled(False)
        self.topBarLayout.setEnabled(True)
        self.topBar.setEnabled(True)
        self.controlGroupBox.setEnabled(True)
        self.dataGroupBox.setEnabled(True)
        self.configurationButton.setEnabled(True)
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(False)


    #Mostrar ventana de logout
    def logoutButtonClick(self):
        self.setEnabled(False)
        self.confirmLogout.showDialog()

    def handleDialogResult(self, accion):
        self.setEnabled(True)
        if accion:
            if self.ret:
                self.stopVideo()
            self.logoutWidgetUpdates()
            
            self.lastFrame.clear()

    def logoutWidgetUpdates(self):
        self.papa.papa_contada.clear()
        self.userEditText.clear()
        self.passwordEditText.clear()
        self.ranchoComboBox.clear()
        self.parcelaComboBox.clear()
        self.variedadComboBox.clear()
        self.idpruebaComboBox.clear()
        self.graphObject.clearGraph()

        self.logoutButton.hide()
        self.loginMsgLabel.hide()

        self.mainStackedWidget.setCurrentIndex(3)
        self.updateButtonIndex(1)

        self.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.topBar.setEnabled(False)
        self.dataGroupBox.setEnabled(False)
        self.controlGroupBox.setEnabled(False)
        self.idpruebaComboBox.setEnabled(False)
        self.configurationButton.setEnabled(False)

        self.ranchoLabel.setText("None")
        self.parcelaLabel.setText("None")
        self.variedadLabel.setText("None")
        self.cosechaLabel.setText("None")
        self.userLabel.setText("Username")
        self.runTimeLabel.setText("0")
    
    ######################## Side Panel Events ########################
    #powerOff button event
    def powerOff(self):
        self.setEnabled(False)
        self.confirmPowerOff.showDialog()
    
    def handlePowerOffResult(self, accion):
        self.setEnabled(True)
        if accion:
            ic("Turning Off...")
            if self.ret:
                self.stopVideo()        
            self.close()

    # =-=-=-=-=-=-=-=> dataPanel events
    def runConfiguration(self):
        self.mainStackedWidget.setCurrentIndex(2)
        self.dataStackedWidget.setCurrentIndex(0)
        self.homeButton.show()

    #actualizar contador de papas
    def updateContador(self):
        self.contadorLabel.setText(str(self.papa.contador))
            

    #  control panel events
    def startVideo(self):

        ret = self.papa.checkConnection()
        if self.status and ret:             #Inicia video si detecta la camara y puede leer frames, sino intenta reconexion
            ic("video started")

            self.papa.ConexionBD.InsertarNuevaPasada(self.idCosecha, datetime.now())
            self.idPasada = self.papa.ConexionBD.ConsultaUltimaPasada(self.idCosecha)
            self.loadGraphComboBoxData()

            cords, latitud, longitud = getCoordinates()
            
            self.timerFrame.start(self.ms)
            if self.twoCams:
                self.timerFrame2.start(self.ms)

            
            self.timerGraph.start(1000)

            self.runTime = 0
            
            self.timerRuntime.start(1000)
            
            self.stopButton.setEnabled(True)
            self.startButton.setEnabled(False)
            self.configurationButton.setEnabled(False)
            self.lastFrame.clear()
            self.papa.idPasada = self.idPasada
            self.graphData()
            #self.papa.idPrueba = 1

            h = self.mainFrame.height()
            w = self.mainFrame.width()

            self.hs = h/480
            self.ws = w/848
            self.ret = True
            self.updateStatus()
        else:
            self.status = False
            self.setEnabled(False)
            self.cameraDisconnected.showDialog()

    def handleDisconnection(self, accion):
        self.setEnabled(True)
        if accion:
            self.tryCamConnection()

    #Para el video junto con todos los timers y resetea el runtime
    def stopVideo(self):
        self.papa.ConexionBD.FinalizarPasada(self.idPasada, datetime.now())
        if self.ret:
            self.timerFrame.stop()
            if self.twoCams:
                self.timerFrame2.stop()
            self.timerGraph.stop()
            self.timerRuntime.stop()
            self.runTime = 0
            self.ret = False
        self.updateStatus()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.configurationButton.setEnabled(True)
        height, width, _ = self.frame.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.frame.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        self.lastFrame.setPixmap(QPixmap.fromImage(qImg))
        self.mainFrame.clear()
        

    ################################################ Main Stacked Widget events ################################################

    ######################## mainPage events ########################

    #main panel events
    def updateFrame(self):
        #self.ret, frame = self.papa.mainGUI()
        self.ret, depthFrame, frame, _ = self.papa.camara1.getFrame()
        if self.ret and self.status:
            
            results = self.papa.frameInference(frame)
            frame = self.papa.drawInference(frame, depthFrame, results)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            self.frame = cv2.resize(frame, (int(frame.shape[1] * self.hs) - 12, int(frame.shape[0] * self.ws) + 12)) 
            height, width, _ = self.frame.shape
            
            bytesPerLine = 3 * width
            qImg = QImage(self.frame.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
            self.mainFrame.setPixmap(QPixmap.fromImage(qImg))
            self.updateContador()
        else:
            self.status = False
            self.stopVideo()
            #self.updateStatus()
    
    def updateFrame2(self):
        #self.ret, frame = self.papa.mainGUI()
        self.ret, depthFrame, frame, _ = self.papa.camara2.getFrame()
        if self.ret and self.status:
            results = self.papa.frameInference2(frame)
            frame = self.papa.drawInference(frame, depthFrame, results)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            self.frame1 = cv2.resize(frame, (int(frame.shape[1] * self.hs) - 12, int(frame.shape[0] * self.ws) + 12)) 
            height, width, _ = self.frame1.shape
            
            bytesPerLine = 3 * width
            qImg = QImage(self.frame1.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
            self.lastFrame.setPixmap(QPixmap.fromImage(qImg))
            self.updateContador()
        else:
            self.status = False
            self.stopVideo()
            #self.updateStatus()

    def lastFrameView(self):
        self.updateButtonIndex(0)

    def liveVideoView(self):
        self.updateButtonIndex(1)

    def graphicsView(self):
        self.updateButtonIndex(2)

    def loadGraphComboBoxData(self):
        self.idpruebaComboBox.clear()
        self.pruebas = self.papa.ConexionBD.ConsultaPasada(self.idCosecha)
        for prueba in self.pruebas:
            self.idpruebaComboBox.addItem(f"ID: {prueba.idPasada}")
        self.idpruebaComboBox.setCurrentIndex(self.idpruebaComboBox.count() - 1)

    def loadGraph(self):
        self.totalPapasLabel.clear()
        idx = int(self.idpruebaComboBox.currentIndex())
        self.idPasada = self.pruebas[idx].idPasada
        self.graphData()

    def graphData(self):
        data = self.papa.ConexionBD.ConsultaDatosPasada(self.idPasada)
        self.graphObject.graph(data)
        self.totalPapasLabel.setText(str(data.CantidadObservada))

    def updateRunTime(self):
        self.runTime += 1
        self.runTimeLabel.setText(str(self.runTime))

    def mapView(self):
        self.updateButtonIndex(3)

    def updateButtonIndex(self, indexNew):
        indexOld = self.showStackedWidget.currentIndex()
        if indexOld != indexNew:
            self.showStackedWidget.setCurrentIndex(indexNew)
            self.buttonIndexes[indexOld].setEnabled(True)
            self.buttonIndexes[indexNew].setEnabled(False)

    #mainSW view
    def homeView(self):
        self.mainStackedWidget.setCurrentIndex(0)

    ######################## Settings Page events ########################
    def updateBrightness(self):
        self.brisho.updateValue(self.brightSlider)

    def settingsView(self):
        self.mainStackedWidget.setCurrentIndex(1)
        self.settingsStackedWidget.setCurrentIndex(0)
        self.returnButton.hide()

    def systemView(self):
        self.settingsStackedWidget.setCurrentIndex(1)
        self.returnButton.show()

    def adminView(self):
        self.settingsStackedWidget.setCurrentIndex(2)
        self.returnButton.show()

    def contactView(self):
        pass
    ############ Settings Page events ############
    def tryCamConnection(self):
        msgFlag = self.status
        if not self.status:
            self.papa.cameraCreation()
            self.status = self.papa.camara1.status
        self.updateStatus()
        if msgFlag != self.status:
            #self.setEnabled(False)
            #self.cameraDisconnected.showDialog()
            pass

    def tryGpsConnection(self):
        self.gps = not self.gps
        self.updateStatus()

    def tryWifiConnection(self):
        self.wifi = not self.wifi
        self.updateStatus()

    def rebootSystem(self):
        self.setEnabled(False)
        self.confirmReboot.showDialog()

    def handleRebootResult(self, accion):
        self.setEnabled(True)
        if accion:
            ic("Restarting...")
            self.close()
            

    ######################## Data Page events ########################
    def loadDefaultData(self):
        data = self.papa.ConexionBD.ConsultaDefaultData(self.idCliente)
        if data is None:
            self.defaultDataFlag = False
            self.defaultDataButton.setEnabled(False)
            self.ranchoDefaultLabel.setText("No Data")
            self.parcelaDefaultLabel.setText("No Data")
            self.variedadDefaultLabel.setText("No Data")
            self.cosechaDefaultLabel.setText("No Data")
        else:
            self.defaultDataFlag = True
            self.defaultDataButton.setEnabled(True)
            self.ranchoDefaultLabel.setText(data.Rancho)
            self.variedadDefaultLabel.setText(data.Variedad)
            self.parcelaDefaultLabel.setText(data.Parcela)
            self.cosechaDefaultLabel.setText(str(data.idCosecha))
            self.defaultData = data


    def saveDefaultData(self):
        if self.currentDataFlag:
            data = {
                "idRancho": self.idRancho,
                "Rancho": self.rancho,
                "idVariedad": self.idVariedad,
                "Variedad": self.variedad,
                "idParcela": self.idParcela,
                "Parcela": self.parcela,
                "idCosecha": self.idCosecha
            }
            if self.defaultDataFlag:
                self.papa.ConexionBD.UpdateDefaultdata(self.idCliente, data)
            else:
                self.papa.ConexionBD.InsertarDefaultData(self.idCliente, data)
            self.loadDefaultData()
        else:
            ic("mostrar ventana, no actual data")

    def setDefaultData(self):
        self.idCosecha = 1
        defaultData = {
                "Rancho": self.defaultData.Rancho,
                "Variedad": self.defaultData.Variedad,
                "Parcela": self.defaultData.Parcela,
                "Cosecha": str(self.defaultData.idCosecha)
            }
        #defaultData = ['Rancho 1', 'Blanca', 'Paparcela 1', str(self.idCosecha)]
        self.idRancho = self.defaultData.idRancho
        self.idVariedad = self.defaultData.idVariedad
        self.idParcela = self.defaultData.idParcela
        self.idCosecha = self.defaultData.idCosecha
        self.setData(defaultData)
    
    def selectData(self):
        data = {
                "Rancho": self.rancho,
                "Variedad": self.variedad,
                "Parcela": self.parcela,
                "Cosecha": str(self.idCosecha)
            }
        self.setData(data)

    def setData(self, data):
        self.currentDataFlag = True
        self.mainStackedWidget.setCurrentIndex(0)
        self.idpruebaComboBox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.loadGraphComboBoxData()

        self.ranchoLabel.setText(data["Rancho"])
        self.variedadLabel.setText(data["Variedad"])
        self.parcelaLabel.setText(data["Parcela"])
        self.cosechaLabel.setText(data["Cosecha"])

    def loadRanchoData(self):
        self.variedadComboBox.setEnabled(False)
        self.parcelaComboBox.setEnabled(False)
        self.cosechaComboBox.setEnabled(False)

        self.addParcelaButton.setEnabled(False)
        self.addCosechaButton.setEnabled(False)

        self.ranchos = self.papa.ConexionBD.ConsultaRancho(self.idCliente)
        for rancho in self.ranchos:
            self.ranchoComboBox.addItem(f"{rancho.NombreRancho}, {rancho.Localidad}")

    def loadVariedadData(self):
        idx = int(self.ranchoComboBox.currentIndex())
        self.rancho = self.ranchos[idx].NombreRancho
        self.idRancho = self.ranchos[idx].idRancho
        #self.rancho = self.ranchoComboBox.currentText().split(',')[0]
        self.variedadComboBox.clear()
        self.parcelaComboBox.clear()
        self.cosechaComboBox.clear()
        self.variedadComboBox.setEnabled(True)
        self.parcelaComboBox.setEnabled(False)
        self.cosechaComboBox.setEnabled(False)
        self.selectDataButton.setEnabled(False)

        self.addParcelaButton.setEnabled(False)
        self.addCosechaButton.setEnabled(False)
        
        self.variedades = self.papa.ConexionBD.ConsultaVariedad()
        for variedad in self.variedades:
            self.variedadComboBox.addItem(f"{variedad.Nombre}")

    def loadParcelaData(self):
        self.parcelaComboBox.clear()
        self.cosechaComboBox.clear()
        self.parcelaComboBox.setEnabled(True)
        self.cosechaComboBox.setEnabled(False)
        self.selectDataButton.setEnabled(False)

        self.addParcelaButton.setEnabled(True)
        self.addCosechaButton.setEnabled(False)

        idx = int(self.variedadComboBox.currentIndex())
        self.variedad = self.variedades[idx].Nombre
        self.idVariedad = self.variedades[idx].idVariedad

        self.parcelas = self.papa.ConexionBD.ConsultaParcela(self.idRancho, self.idVariedad)
        for parcela in self.parcelas:
            self.parcelaComboBox.addItem(f"{parcela.NombreParcela}")

    def loadCosechaData(self):
        
        self.cosechaComboBox.clear()
        self.cosechaComboBox.setEnabled(True)
        self.selectDataButton.setEnabled(False)

        self.addCosechaButton.setEnabled(True)

        idx = int(self.parcelaComboBox.currentIndex())
        self.parcela = self.parcelas[idx].NombreParcela
        self.idParcela = self.parcelas[idx].idParcela

        self.cosechas = self.papa.ConexionBD.ConsultaCosecha(self.idRancho, self.idParcela, self.idMaquina)
        for cosecha in self.cosechas:
            self.cosechaComboBox.addItem(f"{cosecha.idCosecha}")


    def allDataSelected(self):
        idx = int(self.cosechaComboBox.currentIndex())
        self.idCosecha = self.cosechas[idx].idCosecha
        #self.parcela = self.parcelaComboBox.currentText()
        self.selectDataButton.setEnabled(True)

    def selectDataView(self):
        self.dataStackedWidget.setCurrentIndex(1)

    def defaultDataView(self):
        self.dataStackedWidget.setCurrentIndex(0)


    #################Clear text
    def addRancho(self):
        self.setEnabled(False)
        self.addNewRancho.clearData()
        self.addNewRancho.setIdxs(self.idCliente)
        self.addNewRancho.showDialog()
    
    def addVariedad(self):
        self.setEnabled(False)
        self.addNewVariedad.clearData()
        self.addNewVariedad.showDialog()
    
    def addParcela(self):
        self.setEnabled(False)
        self.addNewParcela.clearData()
        self.addNewParcela.setIdxs(self.idRancho, self.idVariedad)
        self.addNewParcela.showDialog()
    
    def addCosecha(self):
        self.setEnabled(False)
        self.addNewCosecha.clearData()
        self.addNewCosecha.setIdxs(self.idRancho, self.idParcela, self.idMaquina)
        self.addNewCosecha.showDialog()
    
    def handleRanchoAddition(self, accion, data):
        self.setEnabled(True)
        if accion:
            self.ranchoComboBox.clear()
            self.loadRanchoData()
            self.setEnabled(False)
            self.statusMessage.updateText(f"'{data}' agregado", f"Se agrego: '{data}' \n satisfactoriamente a Ranchos")
            self.statusMessage.showDialog()

    def handleVariedadAddition(self, accion, data):
        self.setEnabled(True)
        if accion:
            self.variedadComboBox.clear()
            self.loadVariedadData()
            self.setEnabled(False)
            self.statusMessage.updateText(f"'{data}' agregado", f"Se agrego: '{data}' \n satisfactoriamente a Variedades")
            self.statusMessage.showDialog()
                 
    def handleParcelaAddition(self, accion, data):
        self.setEnabled(True)
        if accion:
            self.parcelaComboBox.clear()
            self.loadParcelaData()
            self.setEnabled(False)
            self.statusMessage.updateText(f"'{data}' agregado", f"Se agrego: '{data}' \n satisfactoriamente a Parcelas")
            self.statusMessage.showDialog()

    def handleCosechaAddition(self, accion, data):
        self.setEnabled(True)
        if accion:
            self.cosechaComboBox.clear()
            self.loadCosechaData()
            self.setEnabled(False)
            self.statusMessage.updateText(f"Cosecha No.'{data}' agregado", f"Se agrego: Cosecha No.'{data}' \n satisfactoriamente a Cosechas")
            self.statusMessage.showDialog()

    ################################################ TOP BAR EVENTS ################################################

    def updateLocalTime(self):
        t = localtime()
        minutos = str(t.tm_min) if t.tm_min // 10 >= 1 else "0" + str(t.tm_min)
        horas = str(t.tm_hour) if t.tm_hour // 10 >= 1 else "0" + str(t.tm_hour)

        self.timeLabel.setText(horas + ":" + minutos)

    #update topBar Icons
    def updateStatus(self):

        ###CAM###
        if self.status:
            if self.ret:
                self.labelCamera.setStyleSheet("QLabel {\n"
                    "image: url(Recursos/Icons/camOn.svg);\n"
                    "background-color: rgba(0, 0, 0, 0);\n}"
                    "QLabel:disabled {\n"
                    "background-color: rgb(53, 73, 70);\n"
                    "image: url(Recursos/Icons/camDis.svg);\n"
                    "}")
                self.camStatusLabel.setStyleSheet("background-color: rgb(76, 165, 34);\n"
                    "border-radius:20px;")
            else:
                self.labelCamera.setStyleSheet("QLabel {\n"
                    "image: url(Recursos/Icons/camCon.svg);\n"
                    "background-color: rgba(0, 0, 0, 0);\n}"
                    "QLabel:disabled {\n"
                    "background-color: rgb(53, 73, 70);\n"
                    "image: url(Recursos/Icons/camDis.svg);\n"
                    "}")
                self.camStatusLabel.setStyleSheet("background-color: rgb(9, 90, 150);\n"
                    "border-radius:20px;")
        else:
            self.labelCamera.setStyleSheet("QLabel {\n"
                "image: url(Recursos/Icons/camOff.svg);\n"
                "background-color: rgba(239, 239, 239,0);\n"
                "}\n"
                "QLabel:disabled {\n"
                "background-color: rgb(53, 73, 70);\n"
                "image: url(Recursos/Icons/camDis.svg);\n"
                "}")
        
        if self.gps:
            self.labelGps.setStyleSheet("QLabel {\n"
                "image: url(Recursos/Icons/gpsOn.svg);\n"
                "background-color: rgba(0, 0, 0, 0);\n}"
                "QLabel:disabled {\n"
                "    background-color: rgb(53, 73, 70);\n"
                "    image: url(Recursos/Icons/gpsDis.svg);\n"
                "}")
            self.gpsStatusLabel.setStyleSheet("background-color: rgb(76, 165, 34);\n"
                "border-radius:20px;")
        else:
            self.labelGps.setStyleSheet("QLabel {\n"
                "    image: url(Recursos/Icons/gpsOff.svg);\n"
                "    background-color: rgba(245, 245, 245,0);\n"
                "}\n"
                "QLabel:disabled {\n"
                "    background-color: rgb(53, 73, 70);\n"
                "    image: url(Recursos/Icons/gpsDis.svg);\n"
                "}")
            self.gpsStatusLabel.setStyleSheet("background-color: rgb(223, 57, 45);\n"
                "border-radius:20px;")
        
        if self.wifi:
            self.labelWifi.setStyleSheet("QLabel {\n"
                    "image: url(Recursos/Icons/wifiOn.svg);\n"
                    "background-color: rgba(0, 0, 0, 0);\n"
                    "}\n"
                    "QLabel:disabled {\n"
                    "    background-color: rgba(0, 0, 0, 0);\n"
                    "    image: url(Recursos/Icons/wifiDis.svg);\n"
                    "}")
            self.wifiStatusLabel.setStyleSheet("background-color: rgb(76, 165, 34);\n"
                "border-radius:20px;")
        else:
            self.labelWifi.setStyleSheet("QLabel {\n"
            "    image: url(Recursos/Icons/wifiOff.svg);\n"
            "    background-color: rgba(0, 0, 0,0);\n"
            "}\n"
            "QLabel:disabled {\n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "    image: url(Recursos/Icons/wifiDis.svg);\n"
            "}")
            self.wifiStatusLabel.setStyleSheet("background-color: rgb(223, 57, 45);\n"
                "border-radius:20px;")
    
    def enableScreen(self):
        self.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Papainador()
    window.show()
    sys.exit(app.exec())
