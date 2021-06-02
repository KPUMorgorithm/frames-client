import time
from PyQt5 import QtGui, QtCore
from client.model.temperature.thermal_adapter import TemperatureAdapter
from client.view.video_view import VideoLabel
from client.model.video.video_model import Video
import cv2

class VideoViewModel:

    view : VideoLabel
    vd : Video
    tp : TemperatureAdapter

    def __init__(self,view: VideoLabel, vd, tp):
        self.view = view
        self.vd = vd
        self.tp = tp

    def stopVideo(self):
        self.vd.running = False

    def updateView(self):
        while self.vd.running:
            frame = self.vd.getFrame()
            if frame is None:
                continue
            
            frame = self.temperatureOnImage(frame)
            pixmap = self.makePixmapBy(frame)
            self.view.setPixmap(pixmap)
            time.sleep(1/60)
    
    def temperatureOnImage(self, frame):
        temperatureFrame = self.tp.getFrame()
        temY, temX = temperatureFrame.shape[0], temperatureFrame.shape[1]
        temY *= 2
        temX *= 2
        temperatureFrame = cv2.resize(temperatureFrame, dsize=(temX, temY))

        frameY, frameX = frame.shape[0], frame.shape[1]

        frame[0:temY, frameX-temX:frameX] = temperatureFrame
        return frame

    def makePixmapBy(self,frame):
        
        w,h = self.view.size().width(), self.view.size().height()
        bytePerLine = frame.shape[2] * w
            
        frame = cv2.resize(frame, dsize=(w,h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        qImg = QtGui.QImage(frame.data, w,h, bytePerLine ,QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        return pixmap

