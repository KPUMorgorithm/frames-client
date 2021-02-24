import cv2
import time
import requests
import threading
import numpy as np

class Camera:
    def __init__(self, winname, tick, ip, timeout , cam=cv2.VideoCapture(0)):
        self.winname = winname
        self.cam = cam
        self.started = False
        self.faceMatcher = FaceMatcher(ip, timeout)
        self.frame = None
        self.tick = tick

    def start(self):
        self.started = True
        self._run()
        # threading.Thread(target=self._run, args=()).start()

    def stop(self):
        self.started = False

    def draw(self, isMask, name, face_location):
        ''' 사각형그리는거
        (top, right, bottom, left) = face_location
        cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        '''

        (heigth, width) = np.shape(self.frame)[:2]
        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.rectangle(self.frame, (0,heigth-50), (width,heigth), (0,0,0), cv2.FILLED)
        
        # 한글 인코딩 해야됨
        if isMask:
            name = "Take Off The Mask"
        
        textSize = cv2.getTextSize(name, font, 1, 1)[0]
        textX = int( (width - textSize[0]) / 2 ) 
        textY = int( (heigth -25 ) + textSize[1] / 2 )

        cv2.putText(self.frame, name, (textX,textY), font, 1.0, (255,255,255), 1)
    
    def _run(self):
        tick = 0
        while self.started:
            ret, self.frame = self.cam.read()
            if not ret: break

            self.frame = cv2.flip(self.frame, 1)

            # --- TODO : 다른 쓰레드로 분리해야함 ---

            if tick % self.tick == 0:
                self.faceMatcher.feature(self.frame)
                tick = 0
            tick += 1

            for isMask, name, face_location in self.faceMatcher.faces:
                self.draw(isMask, name, face_location)
            # ---------------------------------

            cv2.imshow(self.winname, self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

class FaceMatcher:
    def __init__(self, ip, timeout):
        self.faces = []
        self.__ip = ip
        self.__timeout = timeout
        
    def feature(self, frame):
        threading.Thread(target=self._feature, args=(frame,)).start()

    def _feature(self, frame):
        t = time.time()
        _, img_encoded = cv2.imencode('.jpg', frame)
        print('encoding time :', time.time() - t)
        t = time.time()
        
        try:
            res = requests.post(self.__ip, 
                            data=img_encoded.tostring(), 
                            headers={'content-type': 'image/jpeg'},
                            timeout=self.__timeout)
            
            print('request time :', time.time() - t)
            self.faces = res.json()['data']
        
        except requests.exceptions.Timeout:
            print(threading.get_ident()," Time Out")
            return
        
        
