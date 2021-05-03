from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from .gui_video_label import VideoLabel
from .gui_request_layout import RequestLayout
from .gui_builder import GuiBuilder

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
        
        vbox = GuiBuilder.makeBoxLayoutIn(self, isVertical = True)

        LB_vd = VideoLabel(self)

        vbox.addWidget(LB_vd, stretch = 2)
        vbox.addLayout(RequestLayout(LB_vd.getVideo(),LB_vd.getTemperautre(),self), 
                        stretch = 1)

        self.setMinimumSize(W,H)
        self.resize(W,H)
        


