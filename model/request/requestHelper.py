from client.config.config import Config
import cv2
import requests
import threading
import time

from client.model.request.requestResultQueue import ResultQueue

class Request:
    def __init__(self, vd, tp, rq, config, ip='http://192.168.0.30:5000/match'):
        self.__ip = ip
        self.__vd = vd
        self.__tp = tp
        self.__resultQueue : ResultQueue = rq
        self.__config : Config = config
        self.__threshold = 30.0
        self.running = True

    def reqSendFrame(self, sendCycle, timeout):
        th = threading.Thread(target=self._reqSendFrame, args=(sendCycle,timeout))
        th.start()

    def _reqSendFrame(self,sendCycle, timeout):
        try:
            # with threading.Lock():
            #     temperature = self.__tp.highestTemp
            temperature = 36.5

            if(temperature <= self.__threshold):
                raise Exception('Low Temperature')
            
            _, img_encoded = cv2.imencode('.jpg', self.__vd.getFrame())
            t = time.time()

            # TODO: tobytes가 맞나..?
            file = {'frame' : ('frame.jpg', img_encoded.tobytes(), 'image/jpeg')}

            data = {
                "temperature" : temperature,
                "facilityNum" : self.__config.getFacilityNum(),
                "state" : self.__config.getState()
                }

            res = requests.post(self.__ip,
                                files= file,
                                data = data,
                                timeout=timeout)
            
            print('request time : ', time.time() - t)

            req = res.json()['data']

            for withoutMask, name in req:

                if withoutMask:
                    self.__resultQueue.addDataWhenChecked(temperature,name)
                else :
                    self.__resultQueue.addDataWhenMasked()

        except requests.exceptions.Timeout as e:
            self.__resultQueue.addDataWhenTimeout()
            return

        except cv2.error as e:
            print('Error :',e,"cv2 error")

        except Exception as e:
            print(e)
            self.__resultQueue.addDataWhenLowTemperature()

        finally:
            if self.running:
                threading.Timer(sendCycle,self._reqSendFrame, args=(sendCycle,timeout)).start()