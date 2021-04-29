from client.gui.gui_builder import GuiBuilder
from PyQt5 import QtCore, QtGui, QtWidgets
from client.src.requests.requests import Request
from client.src.requests.resultQueue import ResultQueue

import threading

MAINWINDOW = "MainWindow"
TRANSLATE = QtCore.QCoreApplication.translate
guiBuilder = GuiBuilder(MAINWINDOW, TRANSLATE)

class RequestLayout(QtWidgets.QVBoxLayout):

    def __init__(self, vd, tp, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resultQueue = ResultQueue()

        self.request = Request(vd,tp, self.resultQueue)
        self.request.reqSendFrame(sendCycle=1,timeout=3)

        hBoxTop = QtWidgets.QHBoxLayout()
        hBoxBot = QtWidgets.QHBoxLayout()

        labelTopLeft = guiBuilder.makeLabel(self, "검증 상태: ")
        self.labelTopRight = guiBuilder.makeLabel(self.parent(),'대기중')
        labelBotLeft = guiBuilder.makeLabel(self.parent(), '검증 결과: ')
        self.labelBotRight = guiBuilder.makeLabel(self.parent(), '대기중2')

        labelTopLeft.setAlignment(QtCore.Qt.AlignRight)
        self.labelTopRight.setAlignment(QtCore.Qt.AlignLeft)
        labelBotLeft.setAlignment(QtCore.Qt.AlignRight)
        self.labelBotRight.setAlignment(QtCore.Qt.AlignLeft)

        hBoxTop.addWidget(labelTopLeft)
        hBoxTop.addWidget(self.labelTopRight)
        hBoxBot.addWidget(labelBotLeft)
        hBoxBot.addWidget(self.labelBotRight)
        
        self.addLayout(hBoxTop)
        self.addLayout(hBoxBot)

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