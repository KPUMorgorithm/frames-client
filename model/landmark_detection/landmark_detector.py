from face_recognition import face_encodings

class LandmarkDetector():
    @staticmethod
    def getLandmarkBy(face):
        endX,endY = face.shape[:2]
        return face_encodings(face,[(0,0,endX,endY)])
