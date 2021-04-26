from client.gui.gui_builder import GuiBuilder
from PyQt5 import QtCore, QtGui, QtWidgets
from client.src.requests.requests import Request

MAINWINDOW = "MainWindow"
TRANSLATE = QtCore.QCoreApplication.translate
guiBuilder = GuiBuilder(MAINWINDOW, TRANSLATE)

class RequestLayout(QtWidgets.QVBoxLayout):

    def __init__(self, vd, tp, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.request = Request(vd,tp)
        self.request.reqSendFrame()
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
    
    def setLabelText(self, target, text):
        label : QtWidgets.QLabel = None

        if target == 'Top':
            label = self.labelTopRight
        elif target == 'Bot':
            label = self.labelBotRight
        else:
            return

        label.setText(text)
    
