from client.model.request.request_config_state import State
from client.model.request.request_landmark import RequestLandmark
from client.model.request.request_config import RequestConfig

class RequestHelper:  

    @staticmethod
    def requestLandmarkAndTemperature(resultQueue, config, landmark, temperature, 
                                    threshold = 30.0, 
                                    ip='http://192.168.0.30:5000/match',
                                    timeout=3):

        RequestLandmark(resultQueue, config).requestLandmark(
                                    landmark,temperature,threshold,ip,timeout)
    
    @staticmethod
    def requestConfig(config, fNum, fName, sIn, sOut, text, timeout=3, ip=""):
        
        isErr, isFnum, isStateIn = RequestHelper.__checkConfigVar(fNum, fName, sIn, sOut, text)

        if isErr:
            return State.INPUTERROR, None

        # return RequestConfig(config).requestConfig(isFnum,text,isStateIn,timeout,ip)
        return State.ACCEPT, True

    @staticmethod
    def __checkConfigVar(fNum, fName, sIn, sOut, text):
        print(fNum, fName, sIn, sOut)

        if not (fNum^fName and sIn^sOut):
            return True, None, None

        isStateIn = True
        if sOut:
            isStateIn = False

        if fNum and text.isdigit():
            return False, True, isStateIn
        elif fName and text.isalpha():
            return False, False, isStateIn
        else:
            return True, None, None