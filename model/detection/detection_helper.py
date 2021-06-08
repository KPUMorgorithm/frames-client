from client.model.detection.face_detection.face_detector import FaceDetector

class DetectionHelper:
    def __init__(self):
        self.fd = FaceDetector('client/model/detection/face_detection/deploy.prototxt','client/model/detection/face_detection/res10_300x300_ssd_iter_140000.caffemodel')
        print("DetectionHelper 생성")

    def __del__(self):
        print("DetectionHelper 삭제")

    #return type: None or face Frame(ndarray)
    def detectFaceFromFrame(self, frame,threshold=0.6):

        detection = self.__getFaceDetectionFrom(frame, threshold)

        if detection is None:
            return None

        face = self.__getFaceFrom(detection, frame)
        
        if self.__isEnoughSize(face):
            return face
        else:
            return None

    #return type: 1-dimension ndarray
    def __getFaceDetectionFrom(self, frame, threshold):
        detections = self.fd.getDetectionsFromFrame(frame)
        detection, confidence = None, 0

        for d in detections:
            c = self.fd.getConfidence(d)
            if c < threshold:
                continue
            if confidence < c:
                detection = d

        return detection
    
    def __getFaceFrom(self, detection, frame):
        (left,top,right,bottom) = self.fd.getFaceLocation(detection,frame)
        face = frame[top:bottom,left:right]
        return face

    def __isEnoughSize(self, frame):
        w,h = frame.shape[:2]
        if w+h>300:
            return True
        print(f"not Enough size = {w+h}")
        return False