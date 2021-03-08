from ctypes import cdll
import time

class Temperature(object):
 
    def __init__( self , libPath):
        self.lib = cdll.LoadLibrary(libPath)
        self.obj = self.lib.Temperature_new()
        
        self.__temperature = 0.0

    def getTemperature(self):
        return self.__temperature
     
    def check(self, tick=0.5) :
        self.__temperature =  self.lib.Temperature_check(self.obj)/100
        print(self.__temperature)
        time.sleep(tick)

    ### TODO: n초 이상 물체 인식시 (한 30도 이상?) 카메라 켜지기
    ### TODO: 얼굴인식하는동안 리스트에 측정 온도를 집어넣어서 제일 높은 값 출력



if __name__ == '__main__':
 
    f = Temperature(libPath='./temperature.dll')

    while True:
        f.check(tick=0.5)
        
