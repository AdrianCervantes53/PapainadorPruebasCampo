from ultralytics import YOLO
import numpy as np
import torch
import cv2
from icecream import ic
import time
from PyQt6.QtCore import QTimer, QThread, pyqtSignal

import math
import queue

#from utils.Camera.Camera import IRS
from utils.DB.potatoDB import *
from utils.DB.datosConexionBD import Datos
from utils.Camera.realsense_depth_filter import *
from utils.Interface.Scripts.MassEstimation import calculateMass, calculateVolume

class Potato(QThread):
    frame_ready = pyqtSignal(int, object, list, float)
    calibres = {"Suprema": 140, "Primera": 110, "Segunda": 80, "Tercera": 60, "Cuarta": 40}
                #                    220+    ,   185-220    ,    150-185   ,     120-150

    def __init__(self, serialNumber, model, id):
        super().__init__()
        self.queue = queue.Queue()
        self.modelo = model
        self.id = id
        self.cameraCreation(serialNumber)
        
        self.stopFlag = False
        self.setParameters()
        self.papa_contada = []
        self.contador = 0
    
    def cameraCreation(self, serialNumber: str):
        self.camara = DepthCamera(serialNumber)
        
    def checkConnection(self):
        ret, _, _, _ = self.camara.getFrame()
        ret, _, _, _ = self.camara.getFrame()
        return ret

    def setParameters(self, conf=0.2, iou=0.85):
        self.conf = conf
        self.iou = iou
    
    def getCategory(self, x):
        for categoria, limite in self.calibres.items():
            if x >= limite:
                return categoria
        return None
    
    def run(self):
        while not self.stopFlag:
            tiempoFrame = time.time()
            ret, depthFrame, frame, _ = self.camara.getFrame()
            if not ret:
                continue
            #results = self.modelo.track(frame, persist=True, verbose=False)
            results = self.frameInference(frame)
            res_plotted, categorias, peso = self.drawInference(frame, depthFrame, results)
            #res_plotted = results[0].plot()

            fps = int(1 / (time.time() - tiempoFrame))
            cv2.putText(res_plotted, ("fps: " + str(fps)), (int(80), int(440)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

            self.frame_ready.emit(self.id, res_plotted, categorias, peso)
            
            time.sleep(0.03) 

    def stop(self):
        self.stopFlag = True
        self.wait()
    
    def frameInference(self, frame, sectionLim=200):
        self.lim = sectionLim
        frame_det = frame[:self.lim, :, :].copy()
        with torch.no_grad():
            results = self.modelo.track(frame_det, conf = self.conf, iou = self.iou, persist=True, verbose = False, show_labels=False, show_conf=False, augment=False)
        return results
    

    
    def drawInference(self, frame, depthFrame, results, showFPS=True, countOffset = 50):
        #datos = {"Total": 0, "Suprema": 0, "Primera": 0, "Segunda": 0, "Tercera": 0, "cuarta": 0, }
        datos = []
        pesoTotal = 0.0

        frame = self.drawBigotes(frame, countOffset)
        if 0 in results[0].boxes.shape or results[0].boxes.id == None:
            pass
        else:
            boxes = results[0].boxes.xywh.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            masks = results[0].masks.data

            for box, track_id, mask in zip(boxes, track_ids, masks):
                m = np.array(mask.cpu())
                resized = cv2.resize(m, (self.camara.w, self.camara.h), interpolation = cv2.INTER_AREA)
                m2 = (resized * 255).clip(0, 255)
                imagen = m2.astype(np.uint8)
                x, y, w, h = box
                contorno, _ = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


                if track_id not in self.papa_contada:
                    
                    x_potato, y_potato, z_potato, pxmm = self.getSize(box, depthFrame)
                    
                    cv2.circle(frame, (int(x), int(y)), 3, (0, 155, 255), thickness = 4)
                    cords = "X" + str(round(float(x_potato))) + " Y" + str(round(float(y_potato)))
                    cv2.putText(frame, cords, (int(x), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1)

                    if (int(y) < self.lim - countOffset):
                        self.papa_contada.append(track_id)
                        self.contador += 1
                        try:
                            
                            area_px = cv2.contourArea(contorno[0])
                            area_mm = (area_px * x_potato * y_potato)/ (int(w) * int(h))
                            minAreaBBox = cv2.minAreaRect(contorno[0])

                            box = cv2.boxPoints(minAreaBBox)
                            box = np.int64(box)
                            cv2.drawContours(frame,[box],0,(0,0,255),2)

                            sizeX_px, sizeY_px = minAreaBBox[1]
                            if sizeX_px > sizeY_px:
                                sizeX_px, sizeY_px = sizeY_px, sizeX_px
                            sizeX_mm = sizeX_px / pxmm
                            sizeY_mm = sizeY_px / pxmm

                            volumen = calculateVolume(sizeX_mm, sizeY_mm)
                            masa = calculateMass(volumen)
                            #ic(f"masa = {masa * 1000} gr")

                            categoria = self.getCategory(sizeY_mm)

                            if categoria:
                                datos.append(categoria)
                                pesoTotal += round(masa, 3)
                            else:
                                ic("ta mu shica")
                        except Exception as e :
                            ic("Error -> insertFlag: ", e)
                else:
                    x_potato, y_potato, z_potato, _ = self.getSize(box, depthFrame)                                
                    cv2.circle(frame, (int(x), int(y)), 3, (150, 255, 100), thickness = 4)
                    cords = "X" + str(round(float(x_potato))) + " Y" + str(round(float(y_potato)))
                    cv2.putText(frame, cords, (int(x), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1)
        return frame, datos, pesoTotal
    
    def getSize(self, box, depthFrame):
        try:
            x, y, w, h = box
            profundidad = depthFrame[int(y/4), int(x/4)]

            if profundidad == 0:
                #ic("ALERTA: Profundidad --> 0")
                profundidad = 300
            
            ancho = profundidad * 2
            pxmm = self.camara.w / ancho

            z_potato = profundidad
            x_potato = w / pxmm
            y_potato = h / pxmm
            return x_potato, y_potato, z_potato, pxmm
        except Exception as e :
            print("Error --> getSize: ", e)
    
    def drawBigotes(self, frame, countOffset):
        cv2.line(frame,(0, self.lim - countOffset), (int(self.camara.w), self.lim - countOffset),(50, 200, 0), 2)
        cv2.line(frame,(0, self.lim), (int(self.camara.w), self.lim),(200, 100, 50), 2)
        return frame