from client.gui.gui_builder import GuiBuilder
from PyQt5 import QtCore, QtGui, QtWidgets
from client.src.requests.requests import Request
from client.src.requests.resultQueue import ResultQueue

import threading

MAINWINDOW = "Request"
TRANSLATE = QtCore.QCoreApplication.translate
guiBuilder = GuiBuilder(MAINWINDOW, TRANSLATE)

class RequestLayout(QtWidgets.QVBoxLayout):

    def __init__(self, vd, tp, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resultQueue = ResultQueue()

        self.request = Request(vd,tp, self.resultQueue)
        self.request.reqSendFrame(sendCycle=1,timeout=3)

        hBoxTop = guiBuilder.makeHBoxLayoutIn(self)
        hBoxBot = guiBuilder.makeHBoxLayoutIn(self)

        guiBuilder.makeLabelIn(hBoxTop, "검증 상태: ", 
                            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.labelTopRight = guiBuilder.makeLabelIn(hBoxTop, "대기중", 
                            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        guiBuilder.makeLabelIn(hBoxBot, "검증 결과: ",
                            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.labelBotRight = guiBuilder.makeLabelIn(hBoxBot, '대기중2',
                            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.checkQueue()
    
    def setLabelText(self, data : tuple):

        state, result = data
        self.labelTopRight.setText(state)
        self.labelBotRight.setText(result)

        
    def checkQueue(self):
        th = threading.Thread(target=self._checkQueue)
        th.start()
    
    def _checkQueue(self):
        while True:
            if self.resultQueue.isExistData():
                self.setLabelText(self.resultQueue.getData())