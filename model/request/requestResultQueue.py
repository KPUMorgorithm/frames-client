from queue import Queue
from threading import Lock

class ResultQueue(Queue):

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

    def isExistData(self):
        if self.empty():
            return False
        return True
    
    def __addDatainQueueBy(self, data : tuple):
        with Lock():
            self.put(data)
            self.join()

    def addDataWhenChecked(self,temperature, name):
        #TODO: Unknown일 땐?
        self.__addDatainQueueBy((0, str(temperature), name)) # 성공

    def addDataWhenTimeout(self):
        self.__addDatainQueueBy((1, "서버와의 연결에 실패했습니다.", "관리자에게 문의해주세요.")) # 실패 (서버 연결 실패)
    
    def addDataWhenMasked(self):
        self.__addDatainQueueBy((2, "마스크를 탈의해주세요.", "")) # 실패 (마스크)

    def addDataWhenLowTemperature(self):
        self.__addDatainQueueBy((3, "  ", "체온이 측정되지 않았습니다")) # 실패 (체온미측정)
        
    def getData(self) -> tuple:
        # if self.isExistData():
        #     return self.get()
        with Lock():
            item = self.get()
            if item is None:
                return
            self.task_done()
            return item