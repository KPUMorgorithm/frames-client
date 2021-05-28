from collections import deque
from ctypes import cdll
import time
from threading import Lock

from client.src.singleton_instance import SingletonInstane

class Temperature(object, metaclass = SingletonInstane):
 
    def __init__( self , libPath):
        self.lib = cdll.LoadLibrary(libPath)
        self.obj = self.lib.Temperature_new()
        self.highestTemp = self.lib.Temperature_check(self.obj)/100

    def checkHighestTemp(self, tick = 0.01, maxTick = 100):
        temperatureList = deque(maxlen = maxTick)
        cnt = 0
        
        while True:
            if cnt == maxTick:
                with Lock():
                    self.highestTemp = max(temperatureList)
                cnt = 0
            temperatureList.append(self.lib.Temperature_check(self.obj)/100)
            cnt += 1
            time.sleep(tick)

        # if temp > 28:
        #     self.highestTemp = round(36+max(temperatureList)/100,2)
        # else:
        #     self.highestTemp = temp
        
        # self.highestTemp = max(temperatureList)
        
