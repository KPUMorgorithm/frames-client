from ctypes import cdll
import time
import threading
from queue import PriorityQueue

class Temperature(object):
 
    def __init__( self , libPath):
        self.lib = cdll.LoadLibrary(libPath)
        self.obj = self.lib.Temperature_new()
        self.th = None
        self._temperature = 0.0
    
    def checkTemperature(self):
        th = threading.Thread(target=self.runDuringWake)
        th.start()
        th.join()
        return self._temperature

    def _checkTemperature(self):
        return self.lib.Temperature_check(self.obj)/100
        

    ### TODO: n초 이상 물체 인식시 (한 30도 이상?) 카메라 켜지기
    # def runDuringSleep(self, tick=0.05, threshold=70, standard = 30.0):
    #     now = 0

    #     while True:

    #         if(now>threshold):
    #             return True

    #         if(self.checkTemperature() > standard):
    #             if now<100 : now+=1
    #         else:
    #             if now>0 : now-=0
            
    #         time.sleep(tick)

    ### TODO: 얼굴인식하는동안 리스트에 측정 온도를 집어넣어서 제일 높은 값 출력
    ### 일단은 n틱동안 체온측정해서 최대값 출력하는거로 함
    def runDuringWake(self, tick = 0.05, maxTick = 50):
        temperatureList = []
        for _ in range(maxTick):
            temperatureList.append(self._checkTemperature())
            time.sleep(tick)

        self._temperature = max(temperatureList)
