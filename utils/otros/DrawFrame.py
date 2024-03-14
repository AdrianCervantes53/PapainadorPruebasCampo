import cv2
import numpy as np

class FrameSize:
    def __init__(self, source, *args):
        print("source ", source)
        if source == 0:
            self.w, self.h = (848, 480)
        elif source == 1:
            self.w, self.h = (640, 480)
        else:
            print(args)
            self.w, self.h = args[0][1], args[0][0]
            
class Detection(FrameSize):
    def __init__(self, source):
        super().__init__(source)
        
    def DrawEllipse(self, frame, bbox, color):
        x, y, w, h = bbox
        cv2.circle(frame, (int(x), int(y)), 3, color = color, thickness = 4)
        cv2.ellipse(frame, (int(x), int(y)), (int(w*0.45), int(h*0.45)), startAngle = 0, endAngle = 360, color = color, thickness = 1)
        return frame
    
    def DrawRectangle(self, frame, bbox, color):
        return frame
    
    def DrawCircle(self, frame, bbox, color):
        x, y, w, h = bbox
        r = (w + h)/4
        cv2.circle(frame, (int(x), int(y)), 3, color = color, thickness = 4)
        cv2.circle(frame, (int(x), int(y)), radius = int(r), color = color, thickness = 1)
        #cv2.minEnclosingCircle(contour)
        return frame
    

class Segmentation(FrameSize):
    def __init__(self, source, *args):
        super().__init__(source)
        self.thick = 1
        
    def DrawSegmentation(self, frame, mask, color, alpha = 0.5):
        '''
        Parameters
        ----------
        frame : BGR Image
            Frame en el que se dibujara la mascara.
        mask : Binary image
            Mascara con valores binarios y mismo tamaño que el frame.
        color : np.array([B, G, R]), dtype = np.uint8
            Color de la mascara en formato BGR.
        alpha : float -> 0.0 - 1.0, optional
            Transparencia de la mascara 
            (0 = Totalmente transparente
             1 = Totalmente solido). The default is 0.5.

        Returns
        -------
        frame : BGR Image
            DESCRIPTION.

        '''
        try:
            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            mask = mask.astype(float) / 255.0
            mask = cv2.resize(mask, (self.w, self.h))
            frame = frame * (1 - mask * alpha) + color * mask * alpha
            frame = frame.astype(np.uint8)
            return frame
        
        except Exception as e :
            print("Error -> Draw mask: ", e)
            return frame   
    
    def Ellipse(self, frame, cnt, color):
        if len(cnt) > 5:
            ellipse = cv2.fitEllipse(cnt)
            cv2.ellipse(frame, ellipse, color, self.thick)
        return frame
    
    def Rectangle(self, frame, cnt, color):
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, color, self.thick)
        return frame
    
    def Circle(self, frame, cnt, color):
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(frame, center, radius, color, self.thick)
        return frame
