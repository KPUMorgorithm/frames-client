from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ..video.video import Video
from ..requests.requests import Request
from ..temperature.temperature import Temperature
from .gui_builder import GuiBuilder
import threading

MAINWINDOW = "MainWindow"
TRANSLATE = QtCore.QCoreApplication.translate
TICK = 100

class VideoLabel(QtWidgets.QLabel):

    def __init__(self, *args, **kwargs):
        super(VideoLabel, self).__init__(*args, **kwargs)
    
    def pixmapEvent(self, pixmap):
        qp = QtGui.QPainter(pixmap)
        pen = QtGui.QPen(QtCore.Qt.red, 30)
        qp.setPen(pen)
        try:
            qp.drawText(
                pixmap.rect(), QtCore.Qt.AlignTop | QtCore.Qt.AlignRight, 
                'gdgdgdgd')
        except:
            pass
        finally:
            self.setPixmap(pixmap)
            qp.end()
    

class Ui_MainWidget(QtWidgets.QWidget):

    def __init__(self, W, H):
        super().__init__()

        self.__guiBuilder = GuiBuilder(MAINWINDOW, TRANSLATE)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.setContentsMargins(5,5,5,5)
        vbox.setSpacing(5)

        FR_video = self.__guiBuilder.makeFrame(self)
        FR_recognition = self.__guiBuilder.makeFrame(self)
        LB_Camera_Main = VideoLabel('asdf',self)
        LB_Camera_Main.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        LB_Camera_Main.setScaledContents(True)

        vbox.addWidget(LB_Camera_Main, stretch = 2)
        vbox.addWidget(FR_recognition, stretch = 1)

        self.setMinimumSize(W,H)
        self.resize(W,H)

        vd = Video(LB_Camera_Main)
        vd.setRunning(True)
        vd.start()
        

class Ui_Main(object):

    def __init__(self, W, H):
        
        super(Ui_Main, self).__init__()
        self.__app = QtWidgets.QApplication(sys.argv)
        '''
        self.__guiBuilder = GuiBuilder(MAINWINDOW, TRANSLATE)

        # Make MainWindow
        self.__MainWindow = self.__guiBuilder.makeMainWindow(W,H)
 
        #Central Widget
        self.__centralwidget = self.__guiBuilder.makeCentralWidget(self.__MainWindow)

        #StatusBar (하단)
        self.statusbar = self.__guiBuilder.makeStatusBar(self.__MainWindow)

        # Temperature
        self.tp = self.setupTemperature(W,H)

        # Video
        self.vd = self.setupVideo(W,H)

        #Request
        self.req = self.setupRequest(W,H, self.vd, self.tp)

        QtCore.QMetaObject.connectSlotsByName(self.__MainWindow)
        '''
        m = Ui_MainWidget(W,H)
        m.show()
        sys.exit(self.__app.exec_())

    def startUi(self):
        pass
        #self.__MainWindow.show()


    def setupVideo(self,W,H):
        half_W = int(W / 2)
        half_H = int(H / 2)
        tick_W = int(W / TICK)
        tick_H = int(H / TICK)

        size = half_W - 2 * (tick_W)

        self.FR_Camera = self.__guiBuilder.makeFrame(self.__centralwidget,
            startX= tick_W,
            startY = tick_H,
            W = size,
            H = size)

        self.LB_Camera_Main = self.__guiBuilder.makeLabel(self.FR_Camera,
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
        self.FR_TEMP = self.__guiBuilder.makeFrame(self.__centralwidget, 
            startX = half_W + tick_W, 
            startY = tick_H, 
            W = frame_W, 
            H = frame_H)
        
        self.LB_TP_Main = self.__guiBuilder.makeLabel(self.FR_TEMP,
            frame_W/2 - 28, tick_H, 56, 12, "체온측정 모듈")
        self.LB_TP_Value = self.__guiBuilder.makeLabel(self.FR_TEMP,
            tick_W, 3 * tick_H + 12, 56 ,12, "측정 결과: ")
        self.LB_TP_Status = self.__guiBuilder.makeLabel(self.FR_TEMP, 
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

        self.FR_TEMP = self.__guiBuilder.makeFrame(self.__centralwidget, 
        startX = half_W + tick_W, 
        startY = H - frame_H - tick_H, 
        W = frame_W, 
        H = frame_H)

        self.LB_TEMP_Main = self.__guiBuilder.makeLabel(self.FR_TEMP,
            frame_W/2 - 28, tick_H, 56, 12, "체온측정")

        req = Request('http://192.168.0.30:5000/match', 3, vd, tp)
        req.sendRequest()

        return req


