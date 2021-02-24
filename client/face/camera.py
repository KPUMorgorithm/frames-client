import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from client.face.face_matcher import FaceMatcher

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

    def _run(self):
        tick = 0
        while self.started:
            ret, self.frame = self.cam.read()
            if not ret: break

            self.frame = cv2.flip(self.frame, 1)

            # --- TODO : 다른 쓰레드로 분리해야함 ---

            if tick % self.tick == 0:                        
                _, img_encoded = cv2.imencode('.jpg', self.frame)
                self.faceMatcher.feature(img_encoded)
                tick = 0
            tick += 1

            for isMask, name, face_location in self.faceMatcher.faces:
                self.draw(isMask, name, face_location)
            # ---------------------------------

            cv2.imshow(self.winname, self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    def draw(self, isMask, name, face_location):
        ''' 사각형그리는거
        (top, right, bottom, left) = face_location
        cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        '''
        (heigth, width) = np.shape(self.frame)[:2]
        if isMask:
            name = "마스크를 탈의해주세요"
        
        self.makeTextBox(name, heigth, width)

    def makeTextBox(self, name,heigth, width, fontSize = 20, recSize = 50):
        
        font = ImageFont.truetype("/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf", fontSize)
        textSize = font.getsize(name)
        textX = int( (width - textSize[0]) / 2 ) 
        textY = int( (recSize - textSize[1]) / 2 )
        
        img = Image.fromarray(np.full((50,width,3), (0,0,0), np.uint8))
        draw = ImageDraw.Draw(img)

        draw.text((textX,textY), name, font=font, fill="white")

        textImage = np.array(img)
        (textH, textW) = np.shape(textImage)[:2]

        self.frame[heigth-textH:heigth, width-textW:width] = textImage
    
        
