from face_recognition import face_encodings
from face_recognition import face_locations

class LandmarkDetector():
    @staticmethod
    def getLandmarkBy(face):

        location = face_locations(face, number_of_times_to_upsample=0, model="cnn")
        if location == []:
            return None
        
        
        print("특징점 추출 완료")
        return face_encodings(face, location, model="large")

    # @staticmethod
    # def test(frame):
    #     # print(frame.shape[:1])
    #     # frame
    #     # print(rgb_frame)
    #     rgb_frame = frame[:, :, ::-1]
    #     locations = face_locations(rgb_frame, number_of_times_to_upsample=0)
    #     # print('location',locations)

    #     ecd = face_encodings(rgb_frame, locations)
    #     # print(ecd)
    #     return ecd