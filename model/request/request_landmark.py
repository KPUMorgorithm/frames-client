from client.model.request.queue_state import CheckedStateData, LowTemperatureStateData, TimeoutStateData, UnknownStateData
import time
import requests
from client.config.config import Config
from client.model.request.request_result_queue import ResultQueue

from client.model.request.request_result_queue import *

class RequestLandmark:
    def __init__(self, resultQueue, config):
        self.__resultQueue : ResultQueue = resultQueue
        self.__config : Config = config
    
    def requestLandmark(self, landmark, temperature, threshold, ip, timeout):
        
        if self.__isNotOverThreshold(temperature, threshold):
            return
        
        data = self.__packData(landmark, temperature)
        res = self.__requestToServer(data,ip,timeout)
        self.__unpackResponse(res, temperature)


    def __isNotOverThreshold(self, temperature, threshold):
        if temperature <= threshold:
            self.__resultQueue.addData(LowTemperatureStateData())
            return True
        return False

    def __packData(self, landmark, temperature):
        return {   
        "landmark" : self.__refineLandmark(landmark),
        "temperature" : temperature,
        "facilityNum" : self.__config.getFacilityNum(),
        "state" : self.__config.getState()
        }

    def __refineLandmark(self, landmark):
        return landmark[0].tolist()

    def __requestToServer(self, data, ip, timeout) :
        try:
            t = time.time()
            res = requests.post(ip, json=data, timeout=timeout)
            print('request time : ', time.time() - t)
            return res

        except requests.exceptions.Timeout:
            self.__resultQueue.addData(TimeoutStateData())
            return None
        
        except Exception as e:
            print(e)
            return None

    def __unpackResponse(self,res : requests.Response, temperature):
        if res is None:
            return
        
        responseData = res.json()['data']
        name = responseData[0]

        if name == "Unknown":
            self.__resultQueue.addData(UnknownStateData())
        else:
            self.__resultQueue.addData(CheckedStateData(temperature, name))


    


