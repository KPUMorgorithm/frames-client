import cv2
import time
import requests
import threading

REQ_TICK = 10 # 요청 tick
class Camera:
    def __init__(self, winname, cam=cv2.VideoCapture(0)):
        self.winname = winname
        self.cam = cam
        self.started = False
        self.faceMatcher = FaceMatcher()
        self.frame = None

    def start(self):
        self.started = True
        self._run()
        # threading.Thread(target=self._run, args=()).start()

    def stop(self):
        self.started = False

    def draw(self, name, face_location):
        (top, right, bottom, left) = face_location
        cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
    def _run(self):
        tick = 0
        while self.started:
            ret, self.frame = self.cam.read()
            if not ret: break

            self.frame = cv2.flip(self.frame, 1)

            # --- TODO : 다른 쓰레드로 분리해야함 ---

            if tick % REQ_TICK == 0:
                self.faceMatcher.feature(self.frame)
                tick = 0
            tick += 1
            for name, face_location in self.faceMatcher.faces:
                self.draw(name, face_location)

            # ---------------------------------

            cv2.imshow(self.winname, self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

class FaceMatcher:
    def __init__(self):
        self.faces = []

    def feature(self, frame):
        threading.Thread(target=self._feature, args=(frame,)).start()

    def _feature(self, frame):
        t = time.time()
        _, img_encoded = cv2.imencode('.jpg', frame)
        print('encoding time :', time.time() - t)
        t = time.time()
        res = requests.post('http://127.0.0.1:5000/match', data=img_encoded.tostring(), headers={'content-type': 'image/jpeg'})
        print('request time :', time.time() - t)

        self.faces = res.json()['data']
