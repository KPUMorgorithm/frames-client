# 시작할때 .ini 세팅을 불러옴
# 세팅을 싱글톤으로 받아 저장
# 세팅을 바탕으로 리퀘스트를 보냄

import configparser
from enum import Enum

class __Config():
    # 세팅값: 건물 번호, 입/출입 지정
    __facilityNum : int
    __state : int
    __configName : str

    FNUM = 'facilityNum'
    STATE = 'state'

    class State(Enum):
        DEFAULT = -1
        OUT = 0
        IN = 1

    def __init__(self, configName):
        self.__configName = configName+'.ini'
        self.iniLoad()

    def iniLoad(self):
        try:
            config = configparser.ConfigParser()
            config.read(self.__configName)
            self.__facilityNum = int(config['Setting'][self.FNUM])
            self.__state = int(config['Setting'][self.STATE])

        except KeyError:
            self.iniMakeDefault()


    def setStateIn(self):
        self._iniSave(self.__facilityNum, self.State.IN.value)
    
    def setStateOut(self):
        self._iniSave(self.__facilityNum, self.State.OUT.value)

    def setFacilityNum(self, fNum):
        self._iniSave(fNum, self.__state)

    def getFacilityNum(self):
        return self.__facilityNum
    
    def getState(self):
        return self.__state

    def iniMakeDefault(self):
        self._iniSave(0,self.State.DEFAULT.value)
    
    def _iniSave(self, facilityNum , state):
        config = configparser.ConfigParser()
        config['Setting'] = {self.FNUM : facilityNum, self.STATE : state}

        with open(self.__configName, 'w') as f:
            config.write(f)

        self.iniLoad()    


class SingletonInstane:
  __instance = None

  @classmethod
  def __getInstance(cls):
    return cls.__instance

  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__getInstance
    return cls.__instance

class Config(__Config, SingletonInstane):
  pass


''' 
Config.instance('config')

a = Config.instance()
b = Config.instance()
print(b.getState())
a.setStateIn()
print(b.getState())
b.setStateOut()
print(a.getState())
'''