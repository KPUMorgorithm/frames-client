from ctypes import cdll
import time

class Temperature(object):
 
    def __init__( self , libPath):
        self.lib = cdll.LoadLibrary(libPath)
        self.obj = self.lib.Temperature_new()
        
        self.__temperature = 0.0

    def getTemperature(self):
        return self.__temperature
     
    # def check(self, tick=0.5) :
    #     self.__temperature =  self.lib.Temperature_check(self.obj)/100
    #     print(self.__temperature)
    #     time.sleep(tick)

    def checkTemperature(self):
        return self.lib.Temperature_check(self.obj)/100

    ### TODO: n초 이상 물체 인식시 (한 30도 이상?) 카메라 켜지기
    def runDuringSleep(self, tick=0.05, threshold=70, standard = 30.0):
        now = 0

        while True:

            if(now>threshold):
                return True

            if(self.checkTemperature() > standard):
                if now<100 : now+=1
            else:
                if now>0 : now-=0
            
            time.sleep(tick)

    ### TODO: 얼굴인식하는동안 리스트에 측정 온도를 집어넣어서 제일 높은 값 출력
    ### 일단은 n틱동안 체온측정해서 최대값 출력하는거로 함
    def runDuringWake(self, tick = 0.05, maxTick = 50):
        temperatureList = []
        for i in range(maxTick):
            temperatureList.append(self.checkTemperature())
            time.sleep(tick)
        return max(temperatureList)




if __name__ == '__main__':
 
    f = Temperature(libPath='./temperature.dll')

    if f.runDuringSleep():
        print("체온 측정 시작")
        print(f.runDuringWake())
        
