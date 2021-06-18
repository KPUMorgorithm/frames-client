import time
import requests
from client.config.config import Config
from client.model.request.request_config_state import State

class RequestConfig:
    
    def __init__(self,config):
        self.__config : Config = config

    def requestConfig(self, isFnum, text, isStateIn, timeout ,ip):
        
        if isFnum:
            ip = ip+"/device"
        else:
            ip = ip+"/facility"
        
        data = self.__packData(isFnum,text,isStateIn)

        requestState, res = self.__requestToServer(data, ip, timeout)

        if requestState is not None:
            return requestState, res, isStateIn

        requestState, requestValue = self.__unpackResponse(res)

        return requestState, requestValue, isStateIn


    def __packData(self, isFnum, text, isStateIn):
        if isFnum:
            return { 
                "deviceId" : self.__config.getUUID(),
                "bno" : int(text),
                "state" : bool(isStateIn)
            }
        else:
            return {
                "deviceId" : self.__config.getUUID(),
                "facilityName" : text,
                "state" : bool(isStateIn)
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
            return State.EXCEPTION, e
    
    def __unpackResponse(self, res : requests.Response):
        print(res)
        responseData = res.text
        print(responseData)
        
        if res.ok:
            #TODO: True False 판별, 3은 bno와 같은 값
            return State.ACCEPT, 3
        
        return State.REJECT, None
        