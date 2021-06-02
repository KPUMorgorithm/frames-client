from client.model.request.request_data_state import *
from PyQt5 import QtWidgets

from client.view.request_view import RequestLayout

from client.model.request.request_helper import RequestHelper

from client.model.detection.detection_helper import DetectionHelper

from client.model.temperature.thermal_adapter import TemperatureAdapter

import time

class RequestViewModel:

    LB_text : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox


    def __init__(self,view: RequestLayout, vd, tp, config):
        self.LB_text = view.getLB_text()
        self.GB_labelBox = view.getGB_labelBox()

        self.running = True

        self.__vd = vd
        self.__tp : TemperatureAdapter = tp

        self.__config = config

        self.detectionHelper = DetectionHelper()

    def stopRequest(self):
        self.running = False
        del self.detectionHelper

    def detectFrame(self):

        requestState : AbstractData = None
        frame = None

        while self.running:

            self._updateView(requestState, frame)
            time.sleep(2)

            temperature = self.__tp.checkTemperature()
            frame = self.__vd.getFrame()

            print('temperature = ',temperature)
            isMasked, landmark = self.detectionHelper.detectLandmarkFromFrame(frame)
            
            if isMasked:
                requestState = MaskedStateData()
                continue

            if landmark is None:
                # requestState = UncheckedLandmarkStateData()
                continue

            requestState = RequestHelper.requestLandmarkAndTemperature(self.__config,
                                            landmark, temperature)


    def _updateView(self, data : AbstractData, frame):

        if data is None:
            print("request None")
            return
    
        if isinstance(data, UnknownStateData):
            #Unknown일 때 frame 보내고 QR 출력
            print(frame)

        print("update")        
        self.GB_labelBox.setStyleSheet(data.qss)
        self.LB_text.setText(data.data)
    