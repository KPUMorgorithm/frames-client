from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from .gui_objectmaker import ObjectMaker

MAINWINDOW = "MainWindow"
TRANSLATE = QtCore.QCoreApplication.translate
TICK = 100

OM = ObjectMaker(MAINWINDOW, TRANSLATE)

class Ui_Main(object):

    def __init__(self, W, H):
        
        super().__init__()
        self.__app = QtWidgets.QApplication(sys.argv)

        # Make MainWindow
        self.__MainWindow = OM.makeMainWindow(W,H)
 
        #Central Widget
        self.__centralwidget = OM.makeCentralWidget(self.__MainWindow)

        #StatusBar (하단)
        self.statusbar = OM.makeStatusBar(self.__MainWindow)

        # SetUp Ui
        self.setupTemperature(W,H)

        QtCore.QMetaObject.connectSlotsByName(self.__MainWindow)

    def setupVideo(W,H):
        print("TODO")
        #TODO: CameraImage input
        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setGeometry(QtCore.QRect(10, 10, 512, 512))
        #self.graphicsView.setObjectName("graphicsView")

    def setupTemperature(self,W,H):
        
        half_W = int(W / 2)
        half_H = int(H / 2)
        tick_W = int(W / TICK)
        tick_H = int(H / TICK)

        frame_W = half_W - 2 * (tick_W)
        frame_H = 29 * tick_H
        
        # Temperature Frame
        self.FR_TEMP = OM.makeFrame(self.__centralwidget, 
            startX = half_W + tick_W, 
            startY = tick_H, 
            W = frame_W, 
            H = frame_H)
        
        self.LB_TEMP_Main = OM.makeLabel(self.FR_TEMP,
            frame_W/2 - 28, tick_H, 56, 12, "체온측정")
        self.LB_TEMP_Value = OM.makeLabel(self.FR_TEMP,
            tick_W, 3 * tick_H + 12, 56 ,12, "Value")
        self.LB_TEMP_Status = OM.makeLabel(self.FR_TEMP, 
            tick_W, 5 * tick_H + 12, 56, 12, "Status")

        

    def startUi(self):
        
        self.__MainWindow.show()
        sys.exit(self.__app.exec_())

