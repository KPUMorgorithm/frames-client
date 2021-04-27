import cv2
import threading
from PyQt5 import QtGui

class Video:
    def __init__(self, label, cam=cv2.VideoCapture(0)):
        self.label = label
        self.frame = None
        self.cam = cam
        self.th = None
        self.running = False

    def start(self):
        self.running = True
        self.th = threading.Thread(target=self.run)
        self.th.start()

    def stop(self):
        self.running = False

    def setRunning(self, bool):
        self.running = bool

    def getFrame(self):
        return self.frame

    def run(self):
        while self.running:
            
            ret, self.frame = self.cam.read()
            
            if not ret:
                print("Cannot read frame")
                continue
            
            w,h = self.label.size().width(), self.label.size().height()
            bytePerLine = self.frame.shape[2] * w
            
            self.frame = cv2.resize(self.frame, dsize=(w,h))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.frame = cv2.flip(self.frame, 1)

            qImg = QtGui.QImage(self.frame.data, w,h, bytePerLine ,QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            #self.label.setPixmap(pixmap)
            self.label.pixmapEvent(pixmap)