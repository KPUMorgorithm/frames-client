from PyQt5 import QtWidgets

from client.view.requestView import RequestLayout

from client.model.request.requestHelper import Request
from client.model.request.requestResultQueue import ResultQueue

from client.qss.state_qssDict import StateStyleSheet

class RequestViewModel:
    resultQueue = ResultQueue()

    LB_text : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox

    cssDict : dict

    beforeState : int

    def __init__(self,view: RequestLayout, vd, tp, config):
        self.cssDict = StateStyleSheet()
        self.LB_text = view.getLB_text()
        self.GB_labelBox = view.getGB_labelBox()
        self.beforeState = -1
        self._initRequestModule(vd,tp, config)

    def _initRequestModule(self, vd, tp,config ):       
        request = Request(vd,tp, self.resultQueue, config)
        request.reqSendFrame(sendCycle=1,timeout=3)

    def checkQueue(self):
        while True:
            data = self.resultQueue.getData()
            if data is None:
                continue
            self._updateView(data)

    def _updateView(self, data):
        state, text = data
        if(self.beforeState == 3 and state == 3):
            return #체온측정안됐을때

        print("update")        
        self.beforeState = state
        self.__changeStyleSheet(state)

        self.LB_text.setText(text)
    
    def __changeStyleSheet(self, state):
        self.GB_labelBox.setStyleSheet(self.cssDict[state])