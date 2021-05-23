import cv2
import numpy as np
import sys

#__net = cv2.dnn.readNet('server/face_detector/deploy.prototxt','server/face_detector/res10_300x300_ssd_iter_140000.caffemodel')

class FaceDetector:
    __net = None

    def __init__(self, prototxtPath, modelPath):
        self.__net = cv2.dnn.readNet(prototxtPath, modelPath)
        if self.__net is None:
            print("Face Detector 클래스 생성 실패, 프로그램 종료")
            sys.exit()

        print("Face Detector 클래스 생성 완료")
    
    def GetDetectionsFromFrame(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300,300), (104.0,177.0,123.0))
        self.__net.setInput(blob)
        detections = self.__net.forward()#순방향 추론
        return detections[0,0]
    
    @staticmethod
    def GetConfidence(detection):
        return detection[2]

    @staticmethod
    def GetFaceLocation(detection, frame):
        (height,width) = np.shape(frame)[:2]
        faceLocation  = detection[3:7] * np.array([width,height,width,height])
        (left, top, right, bottom) = faceLocation.astype("int")
        top = max(0,top.item())
        bottom = min(height-1,bottom.item())
        left = max(0,left.item())
        right = min(width-1,right.item())        

        return (left,top,right,bottom)

    @staticmethod    
    def GetFaceLocationForMD(detection, frame):

        faceLocation = FaceDetector.GetFaceLocation(detection,frame)
        (left, top, right, bottom) = faceLocation
        face = frame[top:bottom,left:right]
        face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
        face = cv2.resize(face, (224, 224))

        return face
