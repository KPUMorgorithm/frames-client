import cv2
import requests
import threading
import time

class Request:
    def __init__(self, vd, tp, ip='http://192.168.0.30:5000/match'):
        self.__ip = ip
        self.__vd = vd
        self.__tp = tp
    
    def reqSendFrame(self, sendCycle, timeout):
        th = threading.Thread(target=self._reqSendFrame, args=(sendCycle,timeout))
        th.start()

    def _reqSendFrame(self,sendCycle, timeout):
        try:
            _, img_encoded = cv2.imencode('.jpg', self.__vd.getFrame())
            t = time.time()

            file = {'frame' : ('frame.jpg', img_encoded, 'image/jpeg')}

            data = {
                "temperature" : self.__tp.highestTemp,
                "facilityNum" : 1,
                "state" : 1
                }

            res = requests.post(self.__ip,
                                files= file,
                                data = data,
                                timeout=timeout)
            
            print('request time : ', time.time() - t)

            req = res.json()['data']

            for withoutMask, name in req:
                #TODO: label에 표시해준다, 큐를 공유하는게 좋을 것 같다
                print(f"withoutMask = {withoutMask}, name = {name}")
                
        except requests.exceptions.Timeout as e:
            #TODO: 서버 상태가 좋지 않음을 라벨에 공유해준다
            print('Error :',e)
            return

        except cv2.error as e:
            print('Error :',e,"cv2 error")

        finally:
            threading.Timer(sendCycle,self._reqSendFrame, args=(sendCycle,timeout)).start()