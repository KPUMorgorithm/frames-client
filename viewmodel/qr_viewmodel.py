# from client.view.qr_view import QRWindow
from PyQt5 import  QtWidgets

import qrcode
from client.model.qr.image import Image

from PyQt5 import QtCore, QtWidgets
from client.src.gui_builder import GuiBuilder


class QRViewModel(QtWidgets.QDialog):

    def __init__(self, qssPath):
        super().__init__()
        
        self.startFunc = None

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint| QtCore.Qt.WindowStaysOnTopHint)
        with open(qssPath,"r") as f:
            self.setStyleSheet(f.read())

        frame = QtWidgets.QFrame(self)
        frame.setMinimumSize(300,350)
        qtRec = frame.frameGeometry()
        qtRec.moveCenter(QtWidgets.QDesktopWidget().geometry().center())
        qtRec.setX(qtRec.x()-30)
        qtRec.setY(qtRec.y()-30)
        frame.move(qtRec.topLeft())

        mainVBox = GuiBuilder.makeBoxLayoutIn(frame, True)
        
        self.LB_img = GuiBuilder.makeLabelIn(mainVBox,"",QtCore.Qt.AlignCenter)
        self.Btn_close = GuiBuilder.makePushButtonIn(mainVBox,1,None, "닫기")
        self.Btn_close.clicked.connect(lambda: self.closeFunc())

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    @QtCore.pyqtSlot(str, object, object)
    def makeQRwindow(self, url, startReq, stopReq):
        stopReq()
        self.startFunc = startReq
        img = qrcode.make(url, image_factory = Image).pixmap()
        self.LB_img.setPixmap(img)
        self.showFullScreen()
    
    def closeFunc(self):
        self.startFunc()
        self.close()
    #TODO n초 뒤에 꺼지게 해야함
