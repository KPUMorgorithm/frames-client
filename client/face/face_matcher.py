import time
import requests
import threading

class FaceMatcher:
    def __init__(self, ip, timeout):
        self.faces = []
        self.__ip = ip
        self.__timeout = timeout
        
    def feature(self, frame):
        threading.Thread(target=self._feature, args=(frame,)).start()

    def _feature(self, img_encoded):        
        try:
            t = time.time()

            res = requests.post(self.__ip, 
                            data=img_encoded.tostring(), 
                            headers={'content-type': 'image/jpeg'},
                            timeout=self.__timeout)            
            
            print('request time :', time.time() - t)
            self.faces = res.json()['data']
        
        except requests.exceptions.Timeout:
            print(threading.get_ident()," Time Out")
            return
    
    