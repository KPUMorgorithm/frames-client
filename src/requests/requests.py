import cv2
import requests
import threading
import time

class Request:
    def __init__(self, ip, timeout, vd):
        self.__ip = ip
        self.__timeout = timeout
        self.__vd = vd
    
    def sendRequest(self):
        try:
            _, img_encoded = cv2.imencode('.jpg', self.__vd.getFrame())

            t = time.time()

            res = requests.post(self.__ip,
                                data = img_encoded.tostring(),
                                headers={'content-type': 'image/jpeg'},
                                timeout=self.__timeout)
            
            print('request time : ', time.time() - t)

            req = res.json()['data']

            for isMask, name, face_location in req:
                ## Something TODO
                print(name)
                
            time.sleep(3)

        except requests.exceptions.Timeout as e:
            print('Error :',e,'Thread ID:',threading.get_ident()," Time Out")
            return

        except cv2.error as e:
            print('Error :',e,"cv2 error")

        finally:
            threading.Timer(3,self.sendRequest).start()