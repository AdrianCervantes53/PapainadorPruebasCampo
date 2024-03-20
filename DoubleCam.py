
from ultralytics import YOLO 
from icecream import ic

import sys
from threading import Thread
import queue


from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QImage, QPixmap
import cv2
import queue
import time
import sys

from utils.Interface.uiDesigns.temp.EspiropapaUI import Ui_MultithreadInterface
from utils.Camera.realsense_depth_filter import *
class CustomThread(QThread):
    frame_ready = pyqtSignal(int, object)

    def __init__(self, serial, model, id):
        super().__init__()
        self.queue = queue.Queue()
        self.modelo = model
        self.id = id
        self.camara = DepthCamera(serial)
        self.stopFlag = False

    def run(self):
        while not self.stopFlag:
            tiempoFrame = time.time()
            ret, df, frame, _ = self.camara.getFrame()
            if ret:
                results = self.modelo.track(frame, persist=True, verbose=False, classes=[0])
                res_plotted = results[0].plot(labels=False, conf=False, boxes=False)

                fps = int(1 / (time.time() - tiempoFrame))
                cv2.putText(res_plotted, ("fps: " + str(fps)), (int(80), int(440)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

                self.frame_ready.emit(self.id, res_plotted)
                
                time.sleep(0.03)  # Ajustar según sea necesario para controlar la velocidad de procesamiento

    def stop(self):
        self.stopFlag = True
        self.wait()

class Espiropapainador(QDialog, Ui_MultithreadInterface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model1 = YOLO("models/potato_seg3s.pt")
        self.model2 = YOLO("models/potato_seg3s.pt")
        self.serialNumbers = ["215122252177", "234322304889"]
        self.thread1 = CustomThread(self.serialNumbers[0], self.model1, 1)
        self.thread2 = CustomThread(self.serialNumbers[1], self.model2, 2)
        self.thread1.frame_ready.connect(self.updateFrame)
        self.thread2.frame_ready.connect(self.updateFrame)

        h = self.frame1.height()
        w = self.frame1.width()
        self.hs = h/480
        self.ws = w/848
        
    def startVideo(self):
        self.thread1.start()
        self.thread2.start()

    @pyqtSlot(int, object)
    def updateFrame(self, id, frame):
        object = self.frame1 if id == 1 else self.frame2
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (int(frame.shape[1] * self.hs) - 12, int(frame.shape[0] * self.ws) + 12)) 
        height, width, _ = frame.shape
        bytesPerLine = 3 * width
        qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        object.setPixmap(QPixmap.fromImage(qImg))

    def stopVideo(self):
        self.thread1.stop()
        self.thread2.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Espiropapainador()
    window.show()
    sys.exit(app.exec())