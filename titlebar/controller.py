from client.titlebar.view import TitleBarLayout
from PyQt5 import QtWidgets

class TitleBarController:
    view : TitleBarLayout

    Btn_setting : QtWidgets.QPushButton
    Btn_exit : QtWidgets.QPushButton

    def __init__(self, view : TitleBarLayout, settingFunc):
        self.view = view
        self.Btn_setting = view.getBtnSetting()
        self.Btn_exit = view.getBtnExit()

        self.connectEvent(settingFunc)

    def connectEvent(self,settingFunc):
        self.Btn_exit.clicked.connect(lambda: self.event_BTN_exit())
        self.Btn_setting.clicked.connect(settingFunc)

    def event_BTN_exit(self):
        self.view.parent().parent().close()
