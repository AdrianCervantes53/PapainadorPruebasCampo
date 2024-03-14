import cv2
import numpy as np
from ultralytics import YOLO
import torch
import pyrealsense2

import time
from datetime import datetime

from utils.Camera.realsense_depth_filter import *
from utils.DB.potatoDB import *
from utils.DB.datosConexionBD import Datos


class Potato:     #[0->IntelRS : 1->Webcam,  bigotes de gato(h/v),  conectar con servidor SQL]
    calibres = {"Suprema": 80, "Primera": 70, "Segunda": 60, "Tercera": 50, "Cuarta": 40, "Quinta": 30, "Sexta": 20}

    def __init__(self, quickStart = True, startData = [0, "h", True]):
        self.startData = startData
        self.quickStart = quickStart
        if startData[2]:
            self.ConexionBD = Creacion(Datos)
        self.model = self.modelo()
        self.camara = self.SeleccionarCam()
        self.papa_contada = []
        self.SeleccinarBigotes()
        self.lim1 = 185
        self.lim2 = 400
        
        self.contador = 0
            
            
    def SeleccionarCam(self):
        '''
        Description
        ---------
        Funcion que pregunta al usuario que camara utilizara para configurar parametros iniciales

        Returns
        -------
        None.

        '''
        if self.quickStart == False:
            print("Que camara desea usar")
            self.cam = int(input("Intel RealSense --> 0   Webcam --> 1: "))
        else:
            self.cam = self.startData[0]
        try:
            while 1:
                if self.cam == 0: 
                    
                    camara = DepthCamera()
                    ret, depth_frame, frame, _ = camara.get_frame()
                    self.w, self.h = (848, 480)
                    break
                else:
                    ret, frame, camara = self.ConexionCam()  
                    break
            self.cx = int((self.w)/2)
            self.cy = int((self.h)/2) 

            if ret == 1:
                print("Cámara conectada y configurada")
            else:
                print("Cámara no conectada")
                exit()
            return camara
        except:
            print("No cam")
            return 0
        
    def ConexionCam(self):
        '''
        
            Descripcion
            -------
            Funcion utilizada para conectar la camara.

            Returns
            -------
            ret : Bool
                Devuelve True si se detecta algun frame y false en caso contrario.
            frame : Array
                Guarda la matriz de NxM del frame en un arreglo.
            camara : Objeto
                Genera el objeto Camara para acceder a sus metodos get y set.

            '''
        camara = cv2.VideoCapture(0)
        camara= self.CamSettings(camara)
        ret, frame = camara.read()
        
        return ret, frame, camara

    def CamSettings(self,camara):
        '''
        Descripcion
        -------
        Funcion para la configuarcion de la camara

        Parameters
        ----------
        camara : Objeto
            Obtiene el objeto camara como parametro para trabajar con el.

        Returns
        -------
        camara : Objeto
            Es el objeto Camara para acceder a sus metodos get y set.
        '''
        
        #camara.set(cv2.CAP_PROP_FPS, 30)
        #camara.set(cv2.CAP_PROP_FRAME_WIDTH, 640)#840
        #camara.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)#400
        w = camara.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = camara.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.h = int(h)
        self.w = int(w)
        print("Width:",self.w)
        print("Height: ",self.h)
        return camara
    
    def SeleccinarBigotes(self):
        if self.quickStart == False:
            print("Orientacion bigotes de gato")
            self.bigotes = input("vertical --> v   horizontal --> h: ")
        else:
            self.bigotes = self.startData[1]
    
    def modelo(self):
        '''Cargar el modelo de tracking potato_detectorX.onnx
        Descripcion
        -------
        Carga el modelo segun la direccion y configura el umbral de confianza y el iou, ya sea que los ingrese el
        el usuario o utilize los valores por default
        
        Parameters
        -------
        conf: umbral de confianza del objeto detectado
        
        iou: (intersection over union) maxima area de interseccion permitida a los objetos para considerarlos como detección

        Returns
        ------
        modelo
        '''
        BASE_PATH = "models/"
        model_path="potato_seg3s.pt"
        model=YOLO(BASE_PATH + model_path, task = 'segment')
        self.conf = 0.2
        self.iou = 0.85
        print(f"Parametros por defecto: conf = {self.conf}, iou = {self.iou}")
        if self.quickStart == False:
            ajustes = input("Configurar parametros de predicción (y/n): ")
            ansr = ajustes.casefold()
            while 1:
                if ansr == "y" :
                    print("Ajustes".center(50, "*"))
                    self.conf = float(input("Confidence Threshold(0-1): "))
                    self.iou = float(input("NMS IoU threshold (0-1): "))
                    print("\n")
                    break
    
                if ansr == "n" :
                    print("Ajustes".center(50, "*"))
                    print("Ajustes Predeterminados Seleccionados...\n")
                    print("\n")
                    break
                ajustes = input("Escribir \'y\' o \'n\': ")
                ansr = ajustes.casefold()
        
        print('modelo cargado y configurado')
        #import pyopencl as cl

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        #platform = cl.get_platforms()[1]  # Asume que la GPU de Intel está en la primera plataforma
        #device2 = platform.get_devices()[1]  # Asume que la GPU de Intel está en el primer dispositivo de la plataforma
        #context = cl.Context([device2])
        #torch.set_default_tensor_type('torch.FloatTensor')
        #device = torch.device('cpu') 
        #print("Device: ", device2)
        model.to(device)
        
        return model
    
    def getDepth(self, depth_frame, point):
        ''' Funcion que recibe un punto y calcula su profundidad aplicandole el offset, si la profundidad en ese pixel es 0,
        se busca el pixel mas cercano de profundidad que haya sido medido correctamente.
        
        Parameters
        ----------
        depth_frame : 
            Matriz de profundidad.
        point :
            Punto en (x, y) al que se le calculara su profundidad
        offset :
            Distancia en px que se genera entre la imagen RGB y la matriz de profundidad. The default is 0.

        Returns
        -------
        profundidad : TYPE
            regresa la coordenada z correspondiente al punto (x, y).

        '''
        try:
            for i in range(2):
                i = int(i)
                dframe_aux = depth_frame[point[1] - i : point[1] + i + 1, point[0] - i : point[0] + i + 1]
                if (dframe_aux.shape)[1] != 0:
                    max_value = np.amax(dframe_aux)
                    if max_value != 0:
                        break
                    else:
                        pass
                    #print(f"No depth values on iteration {i}")
                    #print("Valor Max:", max_value)
                return 0
            profundidad = max_value
            #print("prof",profundidad)
            return profundidad
        except Exception as e :
            print("Error --> getDepth: ", e)
            return 0
    
    def getSize(self, box, depth_frame):
        '''
        Parameters
        ----------
        box : list
            Contiene la posicion y tamaño de la bbox  x, y, w, h.
        depth_frame : array
            Contiene la matriz de profundidad de la imagen.

        Returns
        -------
        x_potato : float
            Tamaño de la papa en X.
        y_potato : float
            Tamaño de la papa en Y.
        z_potato : float
            Tamaño de la papa en Z.
        pxmm : float
            Relacion de cantidad de pixeles por centimetro en la imagen.

        '''
        try:
            x, y, w, h = box
            #print("depth: ",depth_frame.shape)
            profundidad = depth_frame[int(y/4), int(x/4)]
            #profundidad = self.getDepth(depth_frame, (int(x/4), int(y/4)))
            #print("Profundidad", profundidad)
            if profundidad == 0:
                #print("Ay")
                profundidad = 300
            
            ancho = profundidad * 2
            pxmm = self.w / ancho
            #print("mm por pixel en x",pxmm)
            #offset = int(5.9 * pxmm)
            
            #alto = (profundidad / math.tan(65)) * 2
            #pxmmy = self.h / alto
            #print("mm por pixel en y",pxmmy)
            #print("dif", pxmm + pxmmy)
            
            #z_potato = self.getDepth(depth_frame, (int(x), int(y)))
            z_potato = profundidad
            x_potato = w / pxmm
            y_potato = h / pxmm
            #print(f"X = {x_potato * 0.1} cm  Y = {y_potato * 0.1} cm  Z = {z_potato * 0.1} cm")
            return x_potato, y_potato, z_potato, pxmm
        except Exception as e :
            print("Error --> getSize: ", e)
    
    def drawBigotes(self, frame):
        if self.bigotes == "v":
            cv2.line(frame,(self.cx - self.lim1, 0),(self.cx - self.lim1, int(self.h)),(255, 0, 0), 2)
            cv2.line(frame,(self.cx + self.lim2, 0),(self.cx + self.lim2, int(self.h)),(255, 0, 0), 2)
        
        elif self.bigotes == "h":
            cv2.line(frame,(0, self.lim1), (int(self.w), self.lim1),(50, 200, 0), 2)
            cv2.line(frame,(0, self.lim2+1), (int(self.w), self.lim2+1),(200, 100, 50), 2)
            #cv2.line(frame,(0, self.cy + int(self.lim2/1)),(int(self.w), self.cy + int(self.lim2/1.5)),(255, 0, 0), 2)
        return frame
    
    def getCategory(self, x):
        for categoria, limite in self.calibres.items():
            if x >= limite:
                return categoria
        return None
    
    def mainGUI(self):
        
        #camara = self.SeleccionarCam()
        #papa_contada = []
        if self.camara != 0:
            if self.cam == 0:
                ret, depth_frame, frame, _ = self.camara.get_frame()
                frame_det = frame[:self.lim2, :, :].copy()
            else:
                ret, frame = self.camara.read()   
            if ret:  
                tiempoFrame = time.time()
                with torch.no_grad():
                    results = self.model.track(frame_det, conf = self.conf, iou = self.iou, persist=True, verbose = False, show_labels=False, show_conf=False, augment=False)
                
                if 0 in results[0].boxes.shape or results[0].boxes.id == None:
                    pass
                else:
                    #frame = results[0].plot()
                    boxes = results[0].boxes.xywh.cpu()
                    track_ids = results[0].boxes.id.int().cpu().tolist()
                    masks = results[0].masks.data

                    for box, track_id, mask in zip(boxes, track_ids, masks):
                        m = np.array(mask.cpu())
                        resized = cv2.resize(m, (self.w, self.h), interpolation = cv2.INTER_AREA)
                        m2 = (resized * 255).clip(0, 255)
                        imagen = m2.astype(np.uint8)
                        x, y, w, h = box
                        contorno, _ = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


                        if track_id not in self.papa_contada:
                            
                            x_potato, y_potato, z_potato, pxmm = self.getSize(box, depth_frame)
                            
                            cv2.circle(frame, (int(x), int(y)), 3, (0, 155, 255), thickness = 4)
                            cords = "X" + str(round(float(x_potato), 2)) + " Y" + str(round(float(y_potato), 2))
                            cv2.putText(frame, cords, (int(x), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1)

                            #if ((int(x) > self.cx - self.lim1) and (int(x) < self.cx + self.lim2) and self.bigotes == "v") or ((int(y) > self.cy - int(self.lim1/1.5)) and (int(y) < self.cy + int(self.lim2/1.5)) and self.bigotes == "h"):
                            if ((int(x) > self.lim1) and (int(x) < self.lim2) and self.bigotes == "v") or ((int(y) < self.lim1) and self.bigotes == "h"):
                                self.papa_contada.append(track_id)
                                self.contador += 1
                                if True:
                                    try:
                                        self.ConexionBD.Incremento("CantidadObservada", self.idPrueba)
                                        area_px = cv2.contourArea(contorno[0])
                                        area_mm = (area_px * x_potato * y_potato)/ (int(w) * int(h))
                                        minAreaBBox = cv2.minAreaRect(contorno[0])
                                        sizeX_px, sizeY_px = minAreaBBox[1]
                                        if sizeX_px > sizeY_px:
                                            sizeX_px, sizeY_px = sizeY_px, sizeX_px
                                        sizeX_mm = sizeX_px / pxmm
                                        sizeY_mm = sizeY_px / pxmm
                                        
                                        categoria = self.getCategory(sizeX_mm)

                                        if categoria:
                                            self.ConexionBD.Incremento(categoria, self.idPrueba)
                                        else:
                                            print("ta mu shica")
                                        
                                    except Exception as e :
                                        print("Error -> insertFlag: ", e)
                                    
                        else:
                            x_potato, y_potato, z_potato, _ = self.getSize(box, depth_frame)                                
                            cv2.circle(frame, (int(x), int(y)), 3, (150, 255, 100), thickness = 4)
                            cords = "X" + str(round(float(x_potato), 2)) + " Y" + str(round(float(y_potato), 2))
                            cv2.putText(frame, cords, (int(x), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1)
                            
                #frame = results[0].plot()
                frame = self.drawBigotes(frame)
                fps = int(1/(time.time() - tiempoFrame))
                cv2.putText(frame, ("fps: " + str(fps)), (int(80), int(self.h - 40)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)
                return ret, frame
            else:
                ret = False , frame
        else:
            return False, None

    
    def main(self):

        countFlag = True
        detectionFlag = False
        segmentFlag = False
        insertFlag = False
        
        model = self.modelo()
        camara = self.SeleccionarCam()
        if camara == 0:
            exit()
        self.SeleccinarBigotes()
        self.DrawSeg = Segmentation(self.startData[0])
        
        #self.lim1 = 300
        #self.lim2 = 100
        depth_frame = np.full((self.h, self.w), 650, dtype=np.uint8)
        colorNoContado = (0, 50, 250)
        colorContado = (50, 250, 0)
        key = 0
        contador = 0
        papa_contada = []
        
        model = self.model
        conf = self.conf
        iou = self.iou
        #cv2.namedWindow("Potato", cv2.WINDOW_NORMAL)
        cv2.namedWindow("GPA potato detector", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        while True:
            tiempoFrame = time.time()
            if self.cam == 0:
                ret, depth_frame, frame, _ = self.camara.get_frame()
                frame_det = frame[:self.lim2, :, :].copy()

            else:
                ret, frame = self.camara.read()   
            if ret:    
                
                #with torch.no_grad():
                results = model.track(frame, conf = conf, iou = iou, persist=True, verbose = True) #verbose = False

                #Extraer datos de papas contadas como su BBox, Mascara y TrackID

                if 0 in results[0].boxes.shape or results[0].boxes.id == None:
                    pass
                else:
                    boxes = results[0].boxes.xywh.cpu()
                    track_ids = results[0].boxes.id.int().cpu().tolist()
                    masks = results[0].masks.data
                    frame = self.drawBigotes(frame)
                    
                    if segmentFlag:
                        mask0 = mask1 = convexMask = np.zeros((self.h, self.w),dtype=np.uint8) #Mascara para papas no contadas (mask0) y papas contadas (mask1)
                    
            
                    for box, track_id, mask in zip(boxes, track_ids, masks):
                        m = np.array(mask.cpu())
                        resized = cv2.resize(m, (self.w, self.h), interpolation = cv2.INTER_AREA)
                        m2 = (resized * 255).clip(0, 255)
                        imagen = m2.astype(np.uint8)
                        #print(type(imagen))
                        x, y, w, h = box
                        ###
                        contorno, _ = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                        #contorno = cv2.convexHull(contorno[0])
# =============================================================================
#                         try:
#                             cv2.drawContours(frame, contorno[0], -1, (255,200,150),3)
#                         except:
#                             print("len: ",len(contorno[0]))
# =============================================================================

                        
                        if track_id not in papa_contada:
                            
                            x_potato, y_potato, z_potato, pxmm = self.getSize(box, depth_frame)
                            
                            if segmentFlag:
                                mask0 = mask0 + imagen
                            if detectionFlag:
                                frame = self.DrawSeg.Ellipse(frame, contorno[0], colorNoContado)
                            
                            cv2.circle(frame, (int(x), int(y)), 3, (0, 155, 255), thickness = 4)
                            #cords = "X" + str(round(float(x_potato), 2)) + " - Y" + str(round(float(y_potato), 2))
                            #cv2.putText(frame, cords, (int(x), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1)

                            if countFlag:
                                if ((int(x) > self.lim1) and (int(x) < self.lim2) and self.bigotes == "v") or ((int(y) < self.lim1) and self.bigotes == "h"):
                                    
                                    papa_contada.append(track_id)
                                    contador += 1
                                    
                                    if insertFlag:
                                        try:
                                            self.ConexionBD.Incremento("CantidadObservada", 5)
                                            
                                            #hull convex
                                            #area_px = np.sum(imagen == 255)
                                            area_px = cv2.contourArea(contorno[0])
# =============================================================================
#                                             print("area1: ", area_px)
#                                             print("area2: ", area_px2)
#                                             print("difAreas: ", area_px-area_px2)
# =============================================================================
                                            area_mm = (area_px * x_potato * y_potato)/ (int(w) * int(h))
                                            minAreaBBox = cv2.minAreaRect(contorno[0])
                                            
                                            sizeX_px, sizeY_px = minAreaBBox[1]
                                            if sizeX_px > sizeY_px:
                                                sizeX_px, sizeY_px = sizeY_px, sizeX_px
                                            
                                            sizeX_mm = sizeX_px / pxmm
                                            sizeY_mm = sizeY_px / pxmm

                                            
                                            
                                        except Exception as e :
                                            print("Error -> insertFlag: ", e)
                                    
                        else:
                            x_potato, y_potato, z_potato, _ = self.getSize(box, depth_frame)
                            
                            if segmentFlag:
                                mask1 = mask1 + imagen
                            if detectionFlag:
                                frame = self.DrawSeg.Ellipse(frame, contorno[0], colorContado)
                                
                            cv2.circle(frame, (int(x), int(y)), 3, (150, 255, 100), thickness = 4)
                            #cords = "X" + str(round(float(x_potato), 2)) + " - Y" + str(round(float(y_potato), 2))
                            #cv2.putText(frame, cords, (int(x), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1)
                            
                            
                            
                    if segmentFlag:
                        frame = self.DrawSeg.DrawSegmentation(frame, mask0, colorNoContado)
                        frame = self.DrawSeg.DrawSegmentation(frame, mask1, colorContado)

                cv2.putText(frame, str(contador), (int(self.w - 80), int(self.h - 40)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)
                
                fps = int(1/(time.time() - tiempoFrame))
                #print("Fps: ", fps)
                cv2.putText(frame, ("fps: " + str(fps)), (int(80), int(self.h - 40)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)
                
                cv2.imshow("GPA potato detector", frame)
                    
                key = cv2.waitKey(1)
                if key == 113:       #q
                    print("Cerrando programa...")
                    break
                elif key == 100:    #d
                    countFlag = not countFlag
                    print("Deteccion: ", countFlag)    
                elif key == 115:    #s
                    segmentFlag = not segmentFlag
                    print("segmentFlag: ", segmentFlag)
                elif key == 105:    #i
                    if insertFlag:
                        print("Insertar papas = False")
                    else:
                        #date = datetime.now()
                        #tiempoInicial = date.strftime(formato)
                    
# =============================================================================
#                         idPruebaPapas = self.session.query(func.max(Usuario.idUsuario)).scalar()
#                         
#                         print("Ultimo idPruebaPapas: ", idPruebaPapas)
#                         idPruebaPapas = idPruebaPapas + 1
# =============================================================================
                        print("Insertar papas = True")
                    insertFlag = not insertFlag

                    
                elif key == 112:    #p
                    detectionFlag = not detectionFlag
                    print("Show Detection: ", detectionFlag)
# =============================================================================
#                     tipo += 1
#                     if tipo > 3:
#                         tipo = 0 
#                     self.SeleccionarDeteccion(tipo)
# =============================================================================
                        
                elif key == 102:    #f

                    R = self.ConexionBD.ConsultaCosecha()
                    
                    ides = [row.idCosecha for row in R]
                    print("id's Cosecha", ides)

                    print("Insertar fila en PruebaPapas")
                    sel = int(input("Ingrese una id de cosecha: "))
                    while sel not in ides:
                        sel = int(input("Ingrese una idCosecha valida: "))
                    #self.ConexionBD.NuevaPruebaPapas(idCosecha = sel)
                    
                
        
        if self.cam == 0:
            self.camara.release
        else:
            self.camara.release()
        cv2.destroyAllWindows()
        print("Potatos:",len(papa_contada))
        


if __name__ == "__main__": 
    try:
        from otros.DrawFrame import Segmentation
        detector = Potato()
        detector.main()
    except Exception as e :
        print("ErrorOutMain: ", e)
        cv2.destroyAllWindows()