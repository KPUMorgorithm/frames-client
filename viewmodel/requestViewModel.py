from PyQt5 import QtWidgets

from client.view.requestView import RequestLayout

from client.model.request.requestHelper import Request
from client.model.request.requestResultQueue import ResultQueue

from client.qss.state_qssDict import StateStyleSheet

import threading

class RequestViewModel:
    resultQueue = ResultQueue()

    LB_title : QtWidgets.QLabel
    LB_subtitle : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox

    cssDict : dict

    beforState : int

    def __init__(self,view: RequestLayout, vd, tp, config):
        self.cssDict = StateStyleSheet()
        self.LB_title = view.getLB_title()
        self.LB_subtitle = view.getLB_subtitle()
        self.GB_labelBox = view.getGB_labelBox()
        self.beforState = -1
        self._initRequestModule(vd,tp, config)

    def _initRequestModule(self, vd, tp,config ):       
        request = Request(vd,tp, self.resultQueue, config)
        request.reqSendFrame(sendCycle=1,timeout=3)
        self._checkQueue()

    def _checkQueue(self):
        th = threading.Thread(target=self.__checkQueue)
        th.start()
    
    def __checkQueue(self):
        while True:
            data = self.resultQueue.getData()
            if data is None:
                continue
            self._updateView(data)


    def _updateView(self, data):
        state, title, subtitle = data
        if(self.beforState == 3 and state == 3):
            return
        print("update")        
        self.beforState = state
        self.__changeStyleSheet(state)

        self.LB_title.setText(title)
        self.LB_subtitle.setText(subtitle)
    
    def __changeStyleSheet(self, state):
        self.GB_labelBox.setStyleSheet(self.cssDict[state])
        self.LB_subtitle.setStyleSheet("font-size: 28px;")