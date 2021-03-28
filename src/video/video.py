import cv2
import threading
from PyQt5 import QtGui

class Video:
    def __init__(self, label, cam=cv2.VideoCapture(0)):
        self.label = label
        self.size = label.width()
        self.frame = None
        self.cam = cam
        self.running = False

    def start(self):
        self.running = True
        th = threading.Thread(target=self.__run)
        th.start()
        self.__run()

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
            self.frame = cv2.resize(self.frame, dsize=(self.size,self.size))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.frame = cv2.flip(self.frame, 1)

            qImg = QtGui.QImage(self.frame.data, 
                self.size, self.size, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.label.setPixmap(pixmap)