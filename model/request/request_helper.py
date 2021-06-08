from client.model.request.request_config_state import State
from client.model.request.request_face import RequestFace
from client.model.request.request_config import RequestConfig
from client.model.request.request_register_url import RequestRegister
class RequestHelper:  

    # return data state(model/request/request_data_state)
    @staticmethod
    def requestFaceAndTemperature(config, face, temperature, 
                                    threshold = 30.0, 
                                    ip='http://192.168.0.30:5000/match',
                                    timeout=3):

        return RequestFace(config).requestFaceFrame(
                                    face,temperature,threshold,ip,timeout)
    
    # return str(url)
    @staticmethod
    def requestRegister(frame, ip="http://dowo.pw/register", timeout=3):
        return RequestRegister().requestRegister(frame, ip, timeout)

    # return config state(model/request/request_config_state) 
    @staticmethod
    def requestConfig(config, fNum, fName, sIn, sOut, text, timeout=3, ip="http://dowo.pw"):
        
        isErr, isFnum, isStateIn = RequestHelper.__checkConfigVar(fNum, fName, sIn, sOut, text)

        if isErr:
            return State.INPUTERROR, None

        return RequestConfig(config).requestConfig(isFnum,text,isStateIn,timeout,ip)


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