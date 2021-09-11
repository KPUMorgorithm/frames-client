from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from client.model.temperature.thermal_adapter import TemperatureAdapter
from client.view.video_view import VideoLabel
from client.model.video.video_model import Video
import cv2
import numpy as np

class VideoViewModel(QObject):

    view : VideoLabel
    vd : Video
    tp : TemperatureAdapter

    pixmapSignal = pyqtSignal(QtGui.QPixmap)

    def __init__(self,view, vd, tp):
        
        super().__init__(view)

        self.view : VideoLabel = view
        self.vd  : Video = vd
        self.tp = tp
        
        self.vd.signal.connect(self.updateView)
        self.pixmapSignal.connect(self.view.setPixmap)

    @pyqtSlot(np.ndarray)
    def updateView(self, frame):
        # frame = self.temperatureOnImage(frame.copy())
        frame = self.temperatureOnImage(frame)
        pixmap = self.__makePixmapBy(frame)

        self.pixmapSignal.emit(pixmap)

    
    def temperatureOnImage(self, frame):
        temperatureFrame = self.tp.getFrame()
        temY, temX = temperatureFrame.shape[0], temperatureFrame.shape[1]
        temY *= 2
        temX *= 2
        temperatureFrame = cv2.resize(temperatureFrame, dsize=(temX, temY))

        frameY, frameX = frame.shape[0], frame.shape[1]

        frame[0:temY, frameX-temX:frameX] = temperatureFrame
        return frame

    def __makePixmapBy(self,frame):
        
        w,h = self.view.size().width(), self.view.size().height()
        bytePerLine = frame.shape[2] * w
            
        frame = cv2.resize(frame, dsize=(w,h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        qImg = QtGui.QImage(frame.data, w,h, bytePerLine ,QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        return pixmap

