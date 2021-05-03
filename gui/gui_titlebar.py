from PyQt5 import QtWidgets
from client.gui.gui_builder import GuiBuilder
from client.gui.gui_setting import SettingWindow


class TitleBar(QtWidgets.QHBoxLayout):

    def __init__(self,parent : QtWidgets.QVBoxLayout, stretch, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.addWidget(QtWidgets.QFrame(), stretch=8)

        BTN_setting = GuiBuilder.makePushButtonIn(
            self, 1, 'client/gui/resource/settings.png', "Setting")

        BTN_setting.clicked.connect(lambda: self.event_BTN_setting())

        BTN_exit = GuiBuilder.makePushButtonIn(
            self, 1, 'client/gui/resource/exit.png', "Exit")

        BTN_exit.setStyleSheet("background-color: red;")
        BTN_exit.clicked.connect(lambda: self.event_BTN_exit())

        parent.addLayout(self,stretch = stretch)
    
    def event_BTN_exit(self):
        self.parent().parent().close()

    def event_BTN_setting(self):
        SettingWindow()