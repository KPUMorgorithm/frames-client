from PyQt5 import QtCore, QtWidgets
from client.src.gui.gui_builder import GuiBuilder

#How To Use : QRWindow(url)
class QRWindow(QtWidgets.QDialog):
    LB_img : QtWidgets.QLabel
    Btn_close : QtWidgets.QPushButton

    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        mainVBox = GuiBuilder.makeBoxLayoutIn(self, True)
        
        self.LB_img = GuiBuilder.makeLabelIn(mainVBox,"",QtCore.Qt.AlignCenter)
        self.Btn_close = GuiBuilder.makePushButtonIn(mainVBox,1,None, "닫기")
        

    def getLbImg(self):
        return self.LB_img

    def getBtnClose(self):
        return self.Btn_close
