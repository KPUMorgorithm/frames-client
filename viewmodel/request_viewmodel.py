from client.model.request.queue_state import *
from PyQt5 import QtWidgets

from client.view.request_view import RequestLayout

from client.model.request.request_helper import RequestHelper
from client.model.request.request_result_queue import ResultQueue

from client.model.detection.detection_helper import DetectionHelper

from client.model.temperature.thermal_adapter import TemperatureAdapter

import time

class RequestViewModel:
    resultQueue = ResultQueue()

    LB_text : QtWidgets.QLabel
    GB_labelBox : QtWidgets.QGroupBox

    beforeState : AbstractData

    def __init__(self,view: RequestLayout, vd, tp, config):
        self.LB_text = view.getLB_text()
        self.GB_labelBox = view.getGB_labelBox()
        self.beforeState = None

        self.running = True

        self.__vd = vd
        self.__tp : TemperatureAdapter = tp

        self.__config = config

        self.detectionHelper = DetectionHelper()

    def stopRequest(self):
        self.running = False
        del self.detectionHelper

    def detectFrame(self):
        while self.running:
            temperature = self.__tp.checkTemperature()
            print('temperature = ',temperature)
            isMasked, landmark = self.detectionHelper.detectLandmarkFromFrame(self.__vd.getFrame())
            
            if isMasked:
                self.resultQueue.addDataOfMasked()
            
            else:
                if landmark is None:
                    del landmark
                    time.sleep(1)
                    continue

                RequestHelper.requestLandmarkAndTemperature(self.resultQueue,self.__config,
                                                landmark, temperature)

            self._updateView(self.resultQueue.getData())

    # def checkQueue(self):
        # while self.running:
        #     data = self.resultQueue.getData()
        #     if data is None:
        #         continue
        #     self._updateView(data)

    def _updateView(self, data : AbstractData):
        if(self.beforeState == LowTemperatureStateData and data == LowTemperatureStateData):
            return #체온측정안됐을때

        print("update")        
        self.beforeState = data
        self.GB_labelBox.setStyleSheet(data.qss)
        self.LB_text.setText(data.data)
    