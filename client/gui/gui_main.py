from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from client.video.video import Video
from client.requests.requests import Request
from .gui_objectmaker import ObjectMaker
import threading

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

        # Video
        self.vd, th = self.setupVideo(W,H)
        th.start()

        #Request
        self.req, reqTh = self.setupRequest(W,H, self.vd)
        reqTh.start()

        QtCore.QMetaObject.connectSlotsByName(self.__MainWindow)


    def startUi(self):
        
        self.__MainWindow.show()
        sys.exit(self.__app.exec_())


    def setupVideo(self,W,H):
        half_W = int(W / 2)
        half_H = int(H / 2)
        tick_W = int(W / TICK)
        tick_H = int(H / TICK)

        size = half_W - 2 * (tick_W)

        self.FR_Camera = OM.makeFrame(self.__centralwidget,
            startX= tick_W,
            startY = tick_H,
            W = size,
            H = size)

        self.LB_Camera_Main = OM.makeLabel(self.FR_Camera,
            0,0,size,size)

        vd = Video(self.LB_Camera_Main)
        vd.setRunning(True)

        th = threading.Thread(target=vd.run)

        return vd, th


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

    def setupRequest(self,W,H,vd):

        half_W = int(W / 2)
        half_H = int(H / 2)
        tick_W = int(W / TICK)
        tick_H = int(H / TICK)

        frame_W = half_W - 2 * (tick_W)
        frame_H = 50 * tick_H

        self.FR_TEMP = OM.makeFrame(self.__centralwidget, 
        startX = half_W + tick_W, 
        startY = H - frame_H - tick_H, 
        W = frame_W, 
        H = frame_H)

        self.LB_TEMP_Main = OM.makeLabel(self.FR_TEMP,
            frame_W/2 - 28, tick_H, 56, 12, "체온측정")

        req = Request('http://192.168.0.30:5000/match', 3, vd)

        th = threading.Thread(target=req.sendRequest)

        return req, th


