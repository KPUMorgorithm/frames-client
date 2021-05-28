from PyQt5 import QtWidgets

from client.view.request_view import RequestLayout

from client.model.request.request_helper import RequestHelper
from client.model.request.request_result_queue import ResultQueue

from client.model.detection.detection_helper import DetectionHelper

from client.resource.qss.state_qss_dict import StateStyleSheet

class RequestViewModel:
    resultQueue = ResultQueue()

    LB_text : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox

    cssDict : dict

    beforeState : int

    def __init__(self,view: RequestLayout, vd, tp, config):
        self.cssDict = StateStyleSheet()
        self.LB_text = view.getLB_text()
        self.GB_labelBox = view.getGB_labelBox()
        self.beforeState = -1

        self.running = True

        self.__vd = vd
        self.__tp = tp

        self.__config = config

        self.detectionHelper = DetectionHelper()

    def stopRequest(self):
        self.running = False 
        del self.request
        del self.detectionHelper
        del self

    def detectFrame(self):
        while self.running:
            temperature = 36.5
            # temperature = self.__tp.getTemperature
            frame = self.__vd.getFrame()

            detection = self.detectionHelper.getFaceDetectionFrom(frame)
            if detection is None:
                del frame
                continue
            face = self.detectionHelper.getFaceFrom(detection, frame)
            del frame
            landmark = self.detectionHelper.getLandmarkBy(face)
            del face
            if landmark is None:
                del landmark
                continue

            RequestHelper.requestLandmarkAndTemperature(self.resultQueue,self.__config,
                                            landmark, temperature)


    def checkQueue(self):
        while self.running:
            data = self.resultQueue.getData()
            if data is None:
                continue
            self._updateView(data)

    def _updateView(self, data):
        state, text = data
        if(self.beforeState == 3 and state == 3):
            return #체온측정안됐을때

        print("update")        
        self.beforeState = state
        self.__changeStyleSheet(state)

        self.LB_text.setText(text)
    
    def __changeStyleSheet(self, state):
        self.GB_labelBox.setStyleSheet(self.cssDict[state])