import threading
from client.model.request.request_data_state import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from threading import *
from client.view.request_view import RequestLayout

from client.model.request.request_helper import RequestHelper

from client.model.detection.detection_helper import DetectionHelper

from client.model.temperature.thermal_adapter import TemperatureAdapter

import numpy as np


class RequestViewModel(QObject):

    LB_text : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox

    reqSignal = pyqtSignal(object, object, object)

    qrSignal = pyqtSignal(str, object, object)

    def __init__(self,view: RequestLayout, vd, tp, config):
        
        super().__init__(view)
        
        self.LB_text = view.getLB_text()
        self.GB_labelBox = view.getGB_labelBox()

        self.doing = False
        self.mu = threading.Lock()

        self.running = True

        self.__vd = vd
        self.__vd.requestSignal.connect(self.detectFrame)

        self.__tp : TemperatureAdapter = tp

        self.__config = config

        self.detectionHelper = DetectionHelper()

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

        if self.doing == True:
            return

        threading.Thread(target=self._reqState, args=(face, temperature, frame)).start()

    def _reqState(self, face, temperature, frame):

        self.mu.acquire()
        self.doing = True        
        self.mu.release()


        requestState = None
        requestState = RequestHelper.requestFaceAndTemperature(self.__config,
                                            face, temperature)
        
        
        if requestState is None:
            print("request None")
            self.doing = False 
            return
    
        print("update")
        print(requestState.data)        
        self.GB_labelBox.setStyleSheet(requestState.qss)
        self.LB_text.setText(requestState.data)

        if isinstance(requestState, UnknownStateData):
            print('Unknown')
            ok, url = RequestHelper.requestRegister(frame)
            if ok:
                self.running = False
                self.qrSignal.emit(url, self.startReq, self.stopReq)
                self.running = True


        self.mu.acquire()
        self.doing = False
        self.mu.release()

        
