import time
import requests
# import cv2
class RequestRegister:

    # def __init__(self, frame):
    #     self.frame = frame

    def requestRegister(self,frame , ip, timeout):

        file = self.__packData(frame)
        res = self.__requestToServer(file,ip,timeout)
        return self.__unpackResponse(res)

    def __packData(self, frame):
        # _, img_encoded = cv2.imencode('.jpg', frame)

        return {'frame' : frame}


    def __requestToServer(self, file, ip, timeout):
        try:
            t = time.time()
            res = requests.post(ip, files=file, timeout=timeout)
            print('request time : ', time.time() - t)
            return res
        
        except requests.exceptions.Timeout:
            return None
        
        except Exception as e:
            print(e)
            return None

    def __unpackResponse(self, res : requests.Response):
        if res is None:
            return None

        responseData = res.json()['data']
        print(responseData)
        return "https://naver.com"
