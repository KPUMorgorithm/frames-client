from client.model.request.request_data_state import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from client.view.request_view import RequestLayout

from client.model.request.request_helper import RequestHelper

from client.model.detection.detection_helper import DetectionHelper

from client.model.temperature.thermal_adapter import TemperatureAdapter

import numpy as np

class RequestViewModel(QObject):

    LB_text : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox

    reqSignal = pyqtSignal(object, object, object)


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

        self.reqSignal.connect(self.reqState)

    def stopRequest(self):
        self.running = False
        del self.detectionHelper

    def stopReq(self):
        self.running = False
    
    def startReq(self):
        self.running = True

    @pyqtSlot(np.ndarray)
    def detectFrame(self, frame):
        if self.running == False:
            return

        temperature = self.__tp.checkTemperature()

        print('temperature = ',temperature)

        face = self.detectionHelper.detectFaceFromFrame(frame)

        self.reqSignal.emit(face, temperature, frame)

    @pyqtSlot(object, object, object)
    def reqState(self, face, temperature, frame):
        requestState = None
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
            ok, url = RequestHelper.requestRegister(frame)
            if ok:
                self.running = False
                self.__qrMakeFunc(url)
                self.running = True