import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import cv2
class MaskDetector:
    def __init__(self, modelPath):
        self._model = load_model(modelPath)
        if self._model is None:
            print("Mask Detector 클래스 생성 실패")
        print("Mask Detector 클래스 생성 완료")
        
    def maskDetection(self, face):
        
        face = cv2.resize(face,(224, 224))
    
        face = img_to_array(face)
        face = preprocess_input(face)
        
        face = np.expand_dims(face, axis = 0)

        #return (mask, withoutMask)
        return self._model.predict(face)[0]