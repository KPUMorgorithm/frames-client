import configparser
from enum import Enum
import subprocess
import threading

class State(Enum):
        DEFAULT = -1
        OUT = 0
        IN = 1

SETTING = 'Setting'
FNUM = 'facilityNum'
STATE = 'state'
UUID = 'uuid'
FNAME = 'facilityName'

class Config():
    __facilityNum : int
    __state : int
    __uuid : str
    __facilityName : str
    __configName : str

    def __init__(self, configName):
        self.__configName = 'client/config/'+configName+'.ini'
        self.iniLoad()
        self.lock = threading.Lock()
        
    def iniLoad(self):
        try:
            config = configparser.ConfigParser()
            config.read(self.__configName)
            self.__facilityNum = int(config[SETTING][FNUM])
            self.__state = int(config[SETTING][STATE])
            self.__uuid = config[SETTING][UUID]
            self.__facilityName = config[SETTING][FNAME]
        except KeyError:
            self.iniMakeDefault()

    def getFacilityNum(self):
        self.lock.acquire()
        fNum = self.__facilityNum
        self.lock.release()
        return fNum
    
    def getState(self):
        self.lock.acquire()
        state = self.__state
        self.lock.release()
        return State(state)

    def getUUID(self):
        self.lock.acquire()
        uuid = self.__uuid
        self.lock.release()
        return uuid

    def getFacilityName(self):
        self.lock.acquire()
        fName = self.__facilityName
        self.lock.release()
        return fName

    def iniMakeDefault(self):
        uuid = subprocess.check_output('/usr/bin/uuid').decode('utf-8').split('\n')[0]
        self._iniSave(0,State.DEFAULT.value, uuid, "")
    
    def iniSave(self, facilityNum, state, facilityName):
        self._iniSave(facilityNum,state,self.__uuid, facilityName)

    def _iniSave(self, facilityNum , state, uuid, facilityName):
        config = configparser.ConfigParser()
        config[SETTING] = {FNUM : facilityNum, STATE : state, UUID : uuid, FNAME : facilityName}

        with open(self.__configName, 'w') as f:
            config.write(f)

        self.iniLoad()    

