from client.model.temperature.thermal import *
import threading
class TemperatureAdapter:

    def __init__(self):
        self.colorMapType = 0
        self.toggleUnitState = 'C'
        self.minVal = 0
        self.maxVal = 0
        self.lock = threading.Lock()
        startStream()

    def getFrame(self):
        self.lock.acquire()
        frame, self.minVal, self.maxVal = getFrame(self.colorMapType)
        self.lock.release()
        rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return rgbImage
    
    def checkTemperature(self):
        self.lock.acquire()
        minVal, maxVal = self.minVal, self.maxVal
        self.lock.release()

        return readTemp(self.toggleUnitState,'max', minVal, maxVal)