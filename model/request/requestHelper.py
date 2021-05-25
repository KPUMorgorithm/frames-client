from client.config.config import Config
import requests
import time

from client.model.request.requestResultQueue import ResultQueue

class Request:
    def __init__(self, rq, config,threshold = 30.0):
        self.__resultQueue : ResultQueue = rq
        self.__config : Config = config
        self.__threshold = threshold

    def requestLandmarkAndTemperature(self, landmark,temperature, timeout=3, ip='http://192.168.0.30:5000/match'):
        
        if(temperature <= self.__threshold):
            self.__resultQueue.addDataWhenLowTemperature()
            return

        try:        
            data = {
                    "landmark" : landmark,
                    "temperature" : temperature,
                    "facilityNum" : self.__config.getFacilityNum(),
                    "state" : self.__config.getState()
                    }
            t = time.time()
            res = requests.post(ip,
                        data = data,
                        timeout=timeout)
            print('request time : ', time.time() - t)
            
            name = res.json()['data']

            self.__resultQueue.addDataWhenChecked(temperature,name)

        except requests.exceptions.Timeout:
            self.__resultQueue.addDataWhenTimeout()
            return

        except Exception as e:
            print(e)