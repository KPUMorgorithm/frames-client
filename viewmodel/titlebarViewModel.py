from typing import Callable
from client.view.titlebarView import TitleBarLayout
from PyQt5 import QtWidgets

from client.view.qrView import QRWindow
from client.viewmodel.qrViewModel import QRViewModel

import time

class TitleBarViewModel:
    view : TitleBarLayout

    Btn_setting : QtWidgets.QPushButton
    Btn_exit : QtWidgets.QPushButton

    Btn_test : QtWidgets.QPushButton

    closeFunc : Callable

    def __init__(self, view : TitleBarLayout, settingFunc, closeFunc):
        self.view = view
        self.Btn_setting = view.getBtnSetting()
        self.Btn_exit = view.getBtnExit()
        self.closeFunc = closeFunc

        self.connectEvent(settingFunc)
        self.evnet_BTN_test()

    def connectEvent(self,settingFunc):
        self.Btn_exit.clicked.connect(lambda: self.event_BTN_exit())
        self.Btn_setting.clicked.connect(settingFunc)

    def event_BTN_exit(self):
        self.closeFunc()
        time.sleep(1)
        self.view.parent().parent().close()


    def evnet_BTN_test(self):
        view = QRWindow()
        self.view.Btn_Test.clicked.connect(lambda: QRViewModel(view, "https://naver.com"))