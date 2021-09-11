from PyQt5 import QtCore, QtWidgets
from client.src.gui_builder import GuiBuilder

#How To Use : QRWindow(url)
class QRWindow(QtWidgets.QDialog):
    LB_img : QtWidgets.QLabel
    Btn_close : QtWidgets.QPushButton

    def __init__(self, qssPath):
        super().__init__()
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint| QtCore.Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        with open(qssPath,"r") as f:
            self.setStyleSheet(f.read())

        frame = QtWidgets.QFrame(self)
        frame.setMinimumSize(300,350)
        qtRec = frame.frameGeometry()
        qtRec.moveCenter(QtWidgets.QDesktopWidget().geometry().center())
        qtRec.setX(qtRec.x())
        qtRec.setY(qtRec.y())
        frame.move(qtRec.topLeft())

        mainVBox = GuiBuilder.makeBoxLayoutIn(frame, True)
        
        self.LB_img = GuiBuilder.makeLabelIn(mainVBox,"",QtCore.Qt.AlignCenter)
        self.Btn_close = GuiBuilder.makePushButtonIn(mainVBox,1,None, "닫기")
        self.Btn_close.clicked.connect(lambda: self.close())

        # self.showFullScreen()
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def getLbImg(self):
        return self.LB_img

    def getBtnClose(self):
        return self.Btn_close
