from PyQt5 import QtGui, QtCore
from client.model.temperatureModel import Temperature
from client.view.videoView import VideoLabel
from client.model.videoModel import Video
import cv2
import threading

class VideoViewModel:

    view : VideoLabel
    vd : Video
    tp : Temperature

    def __init__(self,view: VideoLabel, vd, tp):
        self.view = view
        self.vd = vd
        self.tp = tp

        self.updateView()

    def updateView(self):
        th = threading.Thread(target=self._updateView)
        th.start()

    def _updateView(self):
        while True:
            frame = self.vd.getFrame()
            if frame is None:
                continue
            
            pixmap = self.makePixmapBy(frame)
            self.drawTemperatureOn(pixmap)
            self.view.setPixmap(pixmap)
    
    def makePixmapBy(self,frame):
        
        w,h = self.view.size().width(), self.view.size().height()
        bytePerLine = frame.shape[2] * w
            
        frame = cv2.resize(frame, dsize=(w,h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)

        qImg = QtGui.QImage(frame.data, w,h, bytePerLine ,QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)

        return pixmap

    def drawTemperatureOn(self, pixmap):
        qp = QtGui.QPainter(pixmap)

        tem = self.tp.highestTemp
        qp.setPen(self._selectPenByTem(tem))
        qp.setFont(QtGui.QFont("Arial", 30))
        try:
            qp.drawText(
                pixmap.rect(), QtCore.Qt.AlignTop | QtCore.Qt.AlignRight, 
                str(tem))            
        except:
            pass
        finally:
            qp.end()
            
        return pixmap
    
    def _selectPenByTem(self, tem):
        if tem < 35:
            color = QtCore.Qt.gray
        elif tem < 37:
            color = QtCore.Qt.green
        elif tem < 37.5:
            color = QtCore.Qt.yellow
        else:
            color = QtCore.Qt.red
        
        pen = QtGui.QPen(color, 5)

        return pen