import time
import requests
from client.config.config import Config
from client.model.request.request_config_state import State

class RequestConfig:
    
    def __init__(self,config):
        self.__config : Config = config

    def requestConfig(self, isFnum, text, isStateIn, timeout ,ip):
        data = self.__packData(isFnum,text,isStateIn)
        print(data)
        state, res = self.__requestToServer(data, ip, timeout)

        if state is not None:
            return state

        return self.__unpackResponse(res), isStateIn


    def __packData(self, isFnum, text, isStateIn):
        return { 
            "uuid" : self.__config.getUUID(),
            "isFnum" : isFnum,
            "text" : text,
            "isStateIn" : isStateIn
        }
    
    def __requestToServer(self, data, ip, timeout):
        try:
            t = time.time()
            res = requests.post(ip, data=data, timeout=timeout)
            print('request time : ', time.time() - t)
            return None, res

        except requests.exceptions.Timeout:
            return State.SERVERERROR, None
        
        except Exception as e:
            print(e)
            return State.EXCEPTION, None
    
    def __unpackResponse(self, res : requests.Response):
        responseData = res.json()['data']
        
        #TODO: True False 판별

        return State.ACCEPT