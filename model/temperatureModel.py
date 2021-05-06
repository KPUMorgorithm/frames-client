from ctypes import cdll
import time
import threading

class Temperature(object):
 
    def __init__( self , libPath):
        self.lib = cdll.LoadLibrary(libPath)
        self.obj = self.lib.Temperature_new()
        self._temperature = self.lib.Temperature_check(self.obj)/100
        self.highestTemp = self.lib.Temperature_check(self.obj)/100

        th = threading.Thread(target=self._updateTemperature)
        th.start()

        self.checkHighestTemp()

    def _updateTemperature(self):
        while True:
            self._temperature = self.lib.Temperature_check(self.obj)/100
        

    def checkHighestTemp(self, tick = 0.01, maxTick = 100):
        temperatureList = []
        for i in range(maxTick):
            if i == maxTick/2:
                th = threading.Thread(target=self.checkHighestTemp)
                th.start()
            temperatureList.append(self._temperature)
            time.sleep(tick)

        self.highestTemp = max(temperatureList)
