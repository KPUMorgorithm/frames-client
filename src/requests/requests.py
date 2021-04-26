import cv2
import requests
import threading
import time

class Request:
    def __init__(self, vd, tp, timeout=1, ip='http://192.168.0.30:5000/match'):
        self.__ip = ip
        self.__timeout = timeout
        self.__vd = vd
        self.__tp = tp
    
    def reqSendFrame(self):
        th = threading.Thread(target=self._reqSendFrame)
        th.start()

    def _reqSendFrame(self):
        try:
            _, img_encoded = cv2.imencode('.jpg', self.__vd.getFrame())

            t = time.time()


            #TODO: hightemperature, facilityNum, state를 보내야 한다.
            res = requests.post(self.__ip,
                                data = img_encoded.tostring(),
                                headers={'content-type': 'image/jpeg'},
                                timeout=self.__timeout)
            
            print('request time : ', time.time() - t)

            #TODO: response로 이름을 받는다
            req = res.json()['data']

            for isMask, name, face_location in req:
                #TODO: label에 표시해준다, 큐를 공유하는게 좋을 것 같다
                print(name)
                # self._sendDataLog(name)
                
        except requests.exceptions.Timeout as e:
            #TODO: 서버 상태가 좋지 않음을 라벨에 공유해준다
            print('Error :',e)
            return

        except cv2.error as e:
            print('Error :',e,"cv2 error")

        finally:
            #TODO: 인자로 전송 주기를 받는다
            threading.Timer(1,self._reqSendFrame).start()
    
    # def _sendDataLog(self, name):
    #     data = {"temperature" : self.__tp.checkTemperature(),
    #             "name" : name,
    #             "memberNum" : 1,
    #             "facilityNum" : 1,
    #             "state" : 1
    #             }
    #     res = requests.post('http://192.168.0.30:5000/addLog',
    #                         data = data)
        
    #     req = res.json()['log']

    #     print(req)