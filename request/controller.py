from PyQt5 import QtCore, QtGui, QtWidgets

from client.request.view import RequestLayout

from client.request.requests import Request
from client.request.resultQueue import ResultQueue

import threading

class RequestController:
    resultQueue = ResultQueue()

    LB_title : QtWidgets.QLabel
    LB_subtitle : QtWidgets.QLabel

    def __init__(self,vd, tp, view: RequestLayout):
        self.LB_title = view.getLB_title()
        self.LB_subtitle = view.getLB_subtitle()
        self._initRequestModule(vd,tp)

    def _initRequestModule(self, vd, tp):       
        request = Request(vd,tp, self.resultQueue)
        request.reqSendFrame(sendCycle=1,timeout=3)
        self._checkQueue()

    def _checkQueue(self):
        th = threading.Thread(target=self.__checkQueue)
        th.start()
    
    def __checkQueue(self):
        while True:
            if self.resultQueue.isExistData():
                self._updateView(self.resultQueue.getData())

    def _updateView(self, data):
        state, title, subtitle = data
        if state == 0: # 성공
            self.LB_title.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #719C70;"
                "font-weight: bold;"
                "font-size: 32px;"
                "margin: 0;"
            )
            self.LB_subtitle.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #719C70;"
                "font-weight: bold;"
                "font-size: 28px;"
                "margin: 0;"
            )
        elif state == 1: # 실패 (서버 연결 실패)
            self.LB_title.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #F24A33;"
                "font-weight: bold;"
                "font-size: 32px;"
                "margin: 0;"
            )
            self.LB_subtitle.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #F24A33;"
                "font-weight: bold;"
                "font-size: 28px;"
                "margin: 0;"
            )
        elif state == 2: # 실패 (마스크)
            self.LB_title.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #F24A33;"
                "font-weight: bold;"
                "font-size: 32px;"
                "margin: 0;"
            )
            self.LB_subtitle.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #F24A33;"
                "font-weight: bold;"
                "font-size: 28px;"
                "margin: 0;"
            )
        else:
            self.LB_title.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #333333;"
                "font-weight: bold;"
                "font-size: 32px;"
                "margin: 0;"
            )
            self.LB_subtitle.setStyleSheet(
                "width: 100%;"
                "color: #FFFFFF;"
                "background-color: #333333;"
                "font-weight: bold;"
                "font-size: 32px;"
                "margin: 0;"
            )

        self.LB_title.setText(title)
        self.LB_subtitle.setText(subtitle)