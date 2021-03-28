import cv2
import requests
import threading
import time
import cv2

class Request:
    def __init__(self, ip, timeout, label):
        self.__ip = ip
        self.__timeout = timeout
        self.reqLabel = label
    
    def sendRequest(self, frame):
        _, img_encoded = cv2.imencode('.jpg', frame)
        
        try:
            t = time.time()

            res = requests.post(self.__ip,
                                data = img_encoded.tostring(),
                                headers={'content-type': 'image/jpeg'},
                                timeout=self.__timeout)
            
            print('request time : ', time.time() - t)

            req = res.json()['data']
            ### someting
            
        except requests.exceptions.Timeout:
            print('Thread ID:',threading.get_ident()," Time Out")
            return
