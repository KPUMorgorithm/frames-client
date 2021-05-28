import cv2
from client.src.singleton_instance import SingletonInstane

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

class Video(metaclass = SingletonInstane):
    def __init__(self):
        self.frame = None
        self.cam = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
        self.running = True
        print("Video Model 생성됨")
    
    def __del__(self):
        print("Video Model 삭제됨")

    def stop(self):
        self.running = False
        self.cam.release()

    def getFrame(self):
        return self.frame

    def run(self):
        while self.running:   
            _, frame = self.cam.read()
            frame = cv2.flip(frame, 1)
            self.frame = frame
            