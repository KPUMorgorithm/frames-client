import cv2
import threading

class Video:
    def __init__(self, cam=cv2.VideoCapture(0)):
        self.frame = None
        self.cam = cam
        self.running = False

        self.start()

    def start(self):
        self.running = True
        th = threading.Thread(target=self.run)
        th.start()

    def stop(self):
        self.running = False

    def setRunning(self, bool):
        self.running = bool

    def getFrame(self):
        return self.frame

    def run(self):
        while self.running:   
            _, self.frame = self.cam.read()
