from client.titlebar.view import TitleBarLayout
from PyQt5 import QtWidgets
from client.gui.gui_setting import SettingWindow

class TitleBarController:
    view : TitleBarLayout

    Btn_setting : QtWidgets.QPushButton
    Btn_exit : QtWidgets.QPushButton

    def __init__(self, view : TitleBarLayout):
        self.view = view
        self.Btn_setting = view.getBtnSetting()
        self.Btn_exit = view.getBtnExit()

        self.connectEvent()

    def connectEvent(self):
        self.Btn_exit.clicked.connect(lambda: self.event_BTN_exit())
        self.Btn_setting.clicked.connect(lambda: self.event_BTN_setting())

    def event_BTN_exit(self):
        self.view.parent().parent().close()

    def event_BTN_setting(self):
        SettingWindow()