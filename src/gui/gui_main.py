from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ..video.video import Video
from ..requests.requests import Request
from ..temperature.temperature import Temperature
from .gui_strategy import GuiStrategy
import threading

MAINWINDOW = "MainWindow"
TRANSLATE = QtCore.QCoreApplication.translate
TICK = 100


class Ui_Main(object):

    def __init__(self, W, H):
        
        super().__init__()
        self.__app = QtWidgets.QApplication(sys.argv)

        self.__guiStrategy = GuiStrategy(MAINWINDOW, TRANSLATE)

        # Make MainWindow
        self.__MainWindow = self.__guiStrategy.makeMainWindow(W,H)
 
        #Central Widget
        self.__centralwidget = self.__guiStrategy.makeCentralWidget(self.__MainWindow)

        #StatusBar (하단)
        self.statusbar = self.__guiStrategy.makeStatusBar(self.__MainWindow)

        # Temperature
        self.tp = self.setupTemperature(W,H)

        # Video
        self.vd = self.setupVideo(W,H)

        #Request
        self.req = self.setupRequest(W,H, self.vd, self.tp)

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

        self.FR_Camera = self.__guiStrategy.makeFrame(self.__centralwidget,
            startX= tick_W,
            startY = tick_H,
            W = size,
            H = size)

        self.LB_Camera_Main = self.__guiStrategy.makeLabel(self.FR_Camera,
            0,0,size,size)

        vd = Video(self.LB_Camera_Main)
        vd.setRunning(True)
        vd.start()

        return vd


    def setupTemperature(self,W,H):
        
        half_W = int(W / 2)
        half_H = int(H / 2)
        tick_W = int(W / TICK)
        tick_H = int(H / TICK)

        frame_W = half_W - 2 * (tick_W)
        frame_H = 29 * tick_H
        
        # Temperature Frame
        self.FR_TEMP = self.__guiStrategy.makeFrame(self.__centralwidget, 
            startX = half_W + tick_W, 
            startY = tick_H, 
            W = frame_W, 
            H = frame_H)
        
        self.LB_TP_Main = self.__guiStrategy.makeLabel(self.FR_TEMP,
            frame_W/2 - 28, tick_H, 56, 12, "체온측정 모듈")
        self.LB_TP_Value = self.__guiStrategy.makeLabel(self.FR_TEMP,
            tick_W, 3 * tick_H + 12, 56 ,12, "측정 결과: ")
        self.LB_TP_Status = self.__guiStrategy.makeLabel(self.FR_TEMP, 
            tick_W, 5 * tick_H + 12, 56, 12, "활성화 상태: ")
        
        tp = Temperature("client/src/temperature/temperature.dll")
        tp.checkTemperature()
        return tp

    def setupRequest(self,W,H,vd, tp):

        half_W = int(W / 2)
        half_H = int(H / 2)
        tick_W = int(W / TICK)
        tick_H = int(H / TICK)

        frame_W = half_W - 2 * (tick_W)
        frame_H = 50 * tick_H

        self.FR_TEMP = self.__guiStrategy.makeFrame(self.__centralwidget, 
        startX = half_W + tick_W, 
        startY = H - frame_H - tick_H, 
        W = frame_W, 
        H = frame_H)

        self.LB_TEMP_Main = self.__guiStrategy.makeLabel(self.FR_TEMP,
            frame_W/2 - 28, tick_H, 56, 12, "체온측정")

        req = Request('http://192.168.0.30:5000/match', 3, vd, tp)
        req.sendRequest()

        return req


