from PyQt5 import QtCore, QtWidgets
import sys
from client.src.gui.gui_builder import GuiBuilder
from client.layoutFactory import LayoutFactory

from client.gui.gui_QR import QRWindow

class Ui_Main(object):

    def __init__(self, W, H):
        
        super(Ui_Main, self).__init__()
        self.__app = QtWidgets.QApplication(sys.argv)
        m = Ui_MainWidget(W,H)
        m.show()
        sys.exit(self.__app.exec_())


class Ui_MainWidget(QtWidgets.QWidget):

    def __init__(self, W, H):
        super().__init__()

        self._addContents()

        self.setMinimumSize(W,H)
        self.resize(W,H)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.showFullScreen()
        # QRWindow("https://naver.com")

    def _addContents(self):
        
        vbox = GuiBuilder.makeBoxLayoutIn(self, isVertical = True)
        factory = LayoutFactory()
        factory.makeTitleBarModule(vbox, 0.5)
        factory.makeVideoModule(vbox, stretch=14)
        factory.makeRequestModule(vbox, 5)
        