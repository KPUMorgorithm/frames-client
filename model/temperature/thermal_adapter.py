from client.model.temperature.thermal import *
from threading import Lock
class TemperatureAdapter:

    def __init__(self):
        self.colorMapType = 0
        self.toggleUnitState = 'C'
        self.minVal = 0
        self.maxVal = 0
        self.lock = Lock()
        startStream()

    def getFrame(self):
        self.lock.acquire()
        frame, self.minVal, self.maxVal = getFrame(self.colorMapType)
        self.lock.release()
        rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgbImage = cv2.transpose(rgbImage)
        rgbImage = cv2.flip(rgbImage, -1)
        return rgbImage
    
    def checkTemperature(self):
        self.lock.acquire()
        minVal, maxVal = self.minVal, self.maxVal
        self.lock.release()

        return readTemp(self.toggleUnitState,'max', minVal, maxVal)