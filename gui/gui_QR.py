from PyQt5 import QtCore, QtWidgets, QtGui
import qrcode
from client.src.gui.gui_builder import GuiBuilder
from client.src.qr.qrcode import QRBuilder


#How To Use : QRWindow(url)
class QRWindow(QtWidgets.QDialog):

    def __init__(self, url):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        mainVBox = GuiBuilder.makeBoxLayoutIn(self, True)
        
        GuiBuilder.makeLabelIn(mainVBox,"",QtCore.Qt.AlignCenter
            ).setPixmap(QRBuilder.makeQRPixmapBy(url))

        GuiBuilder.makePushButtonIn(mainVBox,1,None, "닫기"
            ).clicked.connect(lambda: self.event_exit())

        self.exec_()

        #TODO n초 뒤에 꺼지게 해야함

    def event_exit(self):
        self.close()

