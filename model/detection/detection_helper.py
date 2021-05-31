from client.model.detection.face_detection.face_detector import FaceDetector
from client.model.detection.mask_detection.mask_detector import MaskDetector
from client.model.detection.landmark_detection.landmark_detector import LandmarkDetector

class DetectionHelper:
    def __init__(self):
        self.fd = FaceDetector('client/model/detection/face_detection/deploy.prototxt','client/model/detection/face_detection/res10_300x300_ssd_iter_140000.caffemodel')
        # self.md = MaskDetector('client/model/detection/mask_detection/mask_detector.model')
        print("DetectionHelper 생성")

    def __del__(self):
        print("DetectionHelper 삭제")

    def detectLandmarkFromFrame(self, frame,threshold=0.6):
        detection = self.__getFaceDetectionFrom(frame, threshold)

        if detection is None:
            del frame
            return

        face = self.__getFaceFrom(detection, frame)

        return self.__getLandmarkBy(face)

    def __getFaceDetectionFrom(self, frame, threshold):
        detections = self.fd.getDetectionsFromFrame(frame)
        detection, confidence = None, 0

        for d in detections:
            c = self.fd.getConfidence(d)
            #TODO 프레임 크기 일정이상 요구할수도 있음 
            if c < threshold:
                continue
            if confidence < c:
                detection = d
        return detection
    
    def __getFaceFrom(self, detection, frame):
        (left,top,right,bottom) = self.fd.getFaceLocation(detection,frame)
        face = frame[top:bottom,left:right]
        del frame
        return face

    def __isMasked(self, face):
        mask, withoutMask = self.md.maskDetection(face)
        if(mask>withoutMask):
            return True
        else:
            return False

    def __getLandmarkBy(self, face):
        return LandmarkDetector.getLandmarkBy(face)
