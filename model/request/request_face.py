import time
import requests
import cv2
from client.config.config import Config
from client.model.request.request_data_state import *

class RequestFace:
    def __init__(self, config):
        self.__returnState : AbstractData = None
        self.__config : Config = config
    
    # return data state(model/request/request_data_state)
    def requestFaceFrame(self, face, temperature, threshold, ip, timeout):
        
        if face is None:
            return

        if self.__isNotOverThreshold(temperature, threshold):
            return LowTemperatureStateData()

        file, data = self.__packData(face, temperature)
        res = self.__requestToServer(file,data,ip,timeout)
        self.__unpackResponse(res, temperature)
        return self.__returnState


    def __isNotOverThreshold(self, temperature, threshold):
        if temperature <= threshold:
            return True
        return False

    def __packData(self, face, temperature):
        
        _, img_encoded = cv2.imencode('.jpg', face)

        file = {'face':('face.jpg', img_encoded.tobytes(), 'image/jpeg')}
        
        data= {   
        "temperature" : temperature,
        "facilityNum" : self.__config.getFacilityNum(),
        "state" : self.__config.getState()
        }

        return file, data

    # def __refineLandmark(self, landmark):
    #     return landmark[0].tolist()

    def __requestToServer(self, file, data, ip, timeout) :
        try:
            t = time.time()
            res = requests.post(ip, files=file, data=data, timeout=timeout)
            print('request time : ', time.time() - t)
            return res

        except requests.exceptions.Timeout:
            self.__returnState = TimeoutStateData()
            print('timeout')
            return None
        
        except Exception as e:
            print(e)
            return None

    def __unpackResponse(self,res : requests.Response, temperature):
        if res is None:
            return
        
        responseData = res.json()['data']
        print(responseData)
        isMasked, name = responseData[0], responseData[1]

        if isMasked:
            self.__returnState = MaskedStateData()
            return

        if name == "Unknown":
            self.__returnState = UnknownStateData()
        else:
            self.__returnState = CheckedStateData(temperature, name)


    


