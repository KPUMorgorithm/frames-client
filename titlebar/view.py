from PyQt5 import QtWidgets
from client.src.gui.gui_builder import GuiBuilder


class TitleBarLayout(QtWidgets.QHBoxLayout):

    Btn_setting = QtWidgets.QPushButton
    Btn_exit = QtWidgets.QPushButton

    def __init__(self,parent : QtWidgets.QVBoxLayout, stretch, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.addWidget(QtWidgets.QFrame(), stretch=8)

        self.Btn_setting = GuiBuilder.makePushButtonIn(
            self, 1, 'client/titlebar/resource/settings.png', "Setting")

        self.Btn_exit = GuiBuilder.makePushButtonIn(
            self, 1, 'client/titlebar/resource/exit.png', "Exit")
        self.Btn_exit.setStyleSheet("background-color: red;")

        parent.addLayout(self,stretch = stretch)
    
    def getBtnSetting(self):
        return self.Btn_setting

    def getBtnExit(self):
        return self.Btn_exit