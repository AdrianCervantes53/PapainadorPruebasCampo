from utils.Camera.realsense_depth_filter import *

class IRS():
    def __init__(self):
        self.w, self.h = (848, 480)
        self.tryConnection()

    def tryConnection(self):
        self.irs = DepthCamera()

    def checkConnection(self):
        ret, _, _, _ = self.irs.get_frame()
        return ret
    
    def getFrame(self):
        return self.irs.get_frame()
    #ret, depth_frame, frame, _ = 

    def release(self):
        self.irs.release()
