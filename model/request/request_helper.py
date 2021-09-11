from client.model.request.request_config_state import State
from client.model.request.request_face import RequestFace
from client.model.request.request_config import RequestConfig
from client.model.request.request_register_url import RequestRegister

CLASSIFISERVER = "http://kpuframes.iptime.org:5000"
WAS = "http://eks-clb-861425180.ap-northeast-2.elb.amazonaws.com"

class RequestHelper:  

    # return data state(model/request/request_data_state)
    @staticmethod
    def requestFaceAndTemperature(config, face, temperature, 
                                    threshold = 30.0, 
                                    ip=CLASSIFISERVER+'/match',
                                    timeout=3):

        return RequestFace(config).requestFaceFrame(
                                    face,temperature,threshold,ip,timeout)
    
    # return str(url)
    @staticmethod
    def requestRegister(frame, ip=WAS+"/api/register", timeout=3):
        return RequestRegister().requestRegister(frame, ip, timeout)

    # return config state(model/request/request_config_state) 
    @staticmethod
    def requestConfig(config, fNum, fName, sIn, sOut, text, timeout=3, ip=WAS+"/device"):
        
        isErr, isFnum, isStateIn = RequestHelper.__checkConfigVar(fNum, fName, sIn, sOut, text)

        if isErr:
            return State.INPUTERROR, None, None, None

        return RequestConfig(config).requestConfig(isFnum,text,sIn,timeout,ip)


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