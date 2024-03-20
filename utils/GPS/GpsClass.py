from PyQt6.QtCore import QTimer, QThread, pyqtSignal
from icecream import ic

import serial
import math

from utils.GPS.calculateDistance import CoordinateDistance

class GpsConnection(QThread):
    nextBlock = pyqtSignal(tuple, tuple)
    def __init__(self, puerto = 'COM4', baudrate = 38400) -> None:
        super().__init__()
        self.distance = CoordinateDistance()
        self.active = self.connect(puerto, baudrate)
        self.block = False
        self.stopFlag = False

    def connectGps(self, puerto: str ='COM4', baudrate: int = 38400) -> bool:
        try:
            self.ser= serial.Serial(puerto, baudrate)
            return True
        except serial.SerialException as e:
            ic(f"Error al conectar gps: {e}")
            return False    
    def getLatLong(self) -> tuple[float, float]:
        lectura = self.ser.readline().decode('utf-8').strip()
        lectura = lectura.split(",")
        latitud = float(lectura[2])
        longitud = float(lectura[4])
        lat = self.distance.convertToDegrees(latitud, 2)
        long = self.distance.convertToDegrees(longitud, 3)
        return lat, long
    
    def getCurrentCords(self):
        return self.lat, self.long

    def run(self):
        latInicial, longInicial = self.getLatLong()
        self.nextBlock.emit(latInicial, longInicial)
        self.distance.setStartPoints(latInicial, longInicial)
        self.distance.setRatio(latInicial)
        while not self.stopFlag:

            self.lat, self.long = self.getLatLong()
            distancia = self.distance.calculateDistance(self.lat, self.long)
            if distancia > 5:
                self.nextBlock.emit(self.lat, self.long)
                self.distance.setStartPoints((latInicial, longInicial), (self.lat, self.long))
            
    def stopGps(self):
        self.stopFlag = True
        self.wait()