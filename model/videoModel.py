import cv2

from client.src.singleton_instance import SingletonInstane

class Video(metaclass = SingletonInstane):
    def __init__(self ,cam=cv2.VideoCapture(0)):
        self.frame = None
        self.cam = cam
        self.running = True
        print("Video 모델")

    def stop(self):
        self.running = False

    def getFrame(self):
        return self.frame

    def run(self):
        while self.running:   
            _, self.frame = self.cam.read()
