from client.model.request.queue_state import *
from queue import Queue
from threading import Lock

class ResultQueue(Queue):

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

    def addData(self, data : AbstractData):
        self.put(data)

    def isExistData(self):
        if self.empty():
            return False
        return True

    def getData(self) -> tuple:
        if self.empty() :
            return None
        
        with Lock():
            return self.get()
    
    def addDataOfMasked(self):
        self.addData(MaskedStateData())