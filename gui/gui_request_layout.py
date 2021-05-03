from client.gui.gui_builder import GuiBuilder
from PyQt5 import QtCore, QtGui, QtWidgets
from client.src.requests.requests import Request
from client.src.requests.resultQueue import ResultQueue

import threading


class RequestLayout(QtWidgets.QVBoxLayout):

    resultQueue = ResultQueue()
    LB_state : QtWidgets.QLabel
    LB_result : QtWidgets.QLabel

    def __init__(self, vd, tp, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._initLayout()
        self._initRequestModule(vd,tp)
        
        
    def _initLayout(self):

        guiBuilder = GuiBuilder("Request")
        hBoxTop = guiBuilder.makeHBoxLayoutIn(self)
        hBoxBot = guiBuilder.makeHBoxLayoutIn(self)
        guiBuilder.makeLabelIn(hBoxTop, "검증 상태: ", 
                            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.LB_state = guiBuilder.makeLabelIn(hBoxTop, "...", 
                            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        guiBuilder.makeLabelIn(hBoxBot, "검증 결과: ",
                            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.LB_result = guiBuilder.makeLabelIn(hBoxBot, "...",
                            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    
    def _initRequestModule(self, vd, tp):
        
        request = Request(vd,tp, self.resultQueue)
        request.reqSendFrame(sendCycle=1,timeout=3)
        self._checkQueue()

    def _setLabelTextBy(self, data : tuple):

        state, result = data
        self.LB_state.setText(state)
        self.LB_result.setText(result)
        
    def _checkQueue(self):
        th = threading.Thread(target=self.__checkQueue)
        th.start()
    
    def __checkQueue(self):
        while True:
            if self.resultQueue.isExistData():
                self._setLabelTextBy(self.resultQueue.getData())