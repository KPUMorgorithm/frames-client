import configparser
from enum import Enum
import subprocess

class State(Enum):
        DEFAULT = -1
        OUT = 0
        IN = 1

SETTING = 'Setting'
FNUM = 'facilityNum'
STATE = 'state'
UUID = 'uuid'

class SingletonInstane(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonInstane, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
        

class Config(metaclass = SingletonInstane):
    __facilityNum : int
    __state : int
    __uuid : str
    __configName : str

    def __init__(self, configName):
        self.__configName = 'client/'+configName+'.ini'
        self.iniLoad()
        print("Config 생성됨(싱글톤 확인용)")

    def iniLoad(self):
        try:
            config = configparser.ConfigParser()
            config.read(self.__configName)
            self.__facilityNum = int(config[SETTING][FNUM])
            self.__state = int(config[SETTING][STATE])
            self.__uuid = config[SETTING][UUID]

        except KeyError:
            self.iniMakeDefault()


    def setStateIn(self):
        self._iniSave(self.__facilityNum, State.IN.value)
    
    def setStateOut(self):
        self._iniSave(self.__facilityNum, State.OUT.value)

    def setFacilityNum(self, fNum):
        self._iniSave(fNum, self.__state)

    def getFacilityNum(self):
        return self.__facilityNum
    
    def getState(self):
        return self.__state

    def getUUID(self):
        return self.__uuid

    def iniMakeDefault(self):
        uuid = subprocess.check_output('/usr/bin/uuid').decode('utf-8').split('\n')[0]
        self._iniSave(0,State.DEFAULT.value, uuid)
    
    def _iniSave(self, facilityNum , state, uuid):
        config = configparser.ConfigParser()
        config[SETTING] = {FNUM : facilityNum, STATE : state, UUID : uuid}

        with open(self.__configName, 'w') as f:
            config.write(f)

        self.iniLoad()    



# class Config(__Config, metaclass=SingletonInstane):
#   pass
