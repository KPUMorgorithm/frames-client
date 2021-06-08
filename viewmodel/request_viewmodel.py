from client.model.request.request_data_state import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

from client.view.request_view import RequestLayout

from client.model.request.request_helper import RequestHelper

from client.model.detection.detection_helper import DetectionHelper

from client.model.temperature.thermal_adapter import TemperatureAdapter

import numpy as np

class RequestViewModel(QObject):

    LB_text : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox


    def __init__(self,view: RequestLayout, vd, tp, config, qrMakeFunction):
        
        super().__init__(view)
        
        self.LB_text = view.getLB_text()
        self.GB_labelBox = view.getGB_labelBox()

        self.running = True

        self.__vd = vd
        self.__vd.requestSignal.connect(self.detectFrame)

        self.__tp : TemperatureAdapter = tp

        self.__config = config

        self.detectionHelper = DetectionHelper()

        self.__qrMakeFunc = qrMakeFunction

    def stopRequest(self):
        self.running = False
        del self.detectionHelper

    @pyqtSlot(np.ndarray)
    def detectFrame(self, frame):

        if self.running == False:
            return

        requestState = None
        temperature = self.__tp.checkTemperature()
        print('temperature = ',temperature)

        face = self.detectionHelper.detectFaceFromFrame(frame)
        
        # if isMasked:
        #     requestState = MaskedStateData()

        # elif landmark is None:
        #     # requestState = UncheckedLandmarkStateData()
        #     pass

        requestState = RequestHelper.requestFaceAndTemperature(self.__config,
                                            face, temperature)

        self._updateView(requestState, frame)


    def _updateView(self, data : AbstractData, frame):

        if data is None:
            print("request None")
            return
    
        print("update")
        print(data.data)        
        self.GB_labelBox.setStyleSheet(data.qss)
        self.LB_text.setText(data.data)

        if isinstance(data, UnknownStateData):
            print('Unknown')
            url = RequestHelper.requestRegister(frame)
            # if url is not None:
            #     self.__qrMakeFunc(url)
            if url is None:
                self.running = False
                self.running = self.__qrMakeFunc("https://naver.com")