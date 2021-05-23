from client.model.face_detection.face_detector import FaceDetector
from client.model.mask_detection.mask_detector import MaskDetector
from client.model.landmark_detection.landmark_detector import LandmarkDetector

class DetectionHelper:
    def __init__(self):
        self.fd = FaceDetector('client/model/face_detection/deploy.prototxt','client/src/face_detection/res10_300x300_ssd_iter_140000.caffemodel')
        self.md = MaskDetector('client/model/mask_detection/mask_detector.model')
    
    def getFaceDetectionIn(self, frame, threshold):
        detections = self.fd.GetDetectionsFromFrame(frame)
        detection, confidence = None, 0

        for d in detections:
            c = self.fd.getConfidence(d)
            #TODO 프레임 크기 일정이상 요구할수도 있음 
            if c < threshold:
                continue
            if confidence < c:
                detection = d


        return detection
    
    def getFaceBy(self, detection, frame):
        (left,top,right,bottom) = self.fd.getFaceLocation(detection,frame)
        face = frame[top:bottom,left:right]
        return face

    def isMasked(self, face):
        mask, withoutMask = self.md.maskDetection(face)
        if(mask>withoutMask):
            return True
        else:
            return False

    def getLandmarkBy(face):
        return LandmarkDetector.getLandmarkBy(face)
