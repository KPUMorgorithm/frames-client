from PyQt5 import QtWidgets
from client.src.gui_builder import GuiBuilder


class TitleBarLayout(QtWidgets.QHBoxLayout):

    Btn_setting = QtWidgets.QPushButton
    Btn_exit = QtWidgets.QPushButton

    def __init__(self,parent : QtWidgets.QVBoxLayout, stretch, *args, **kwargs):
        super().__init__(*args, **kwargs)

        frame = QtWidgets.QFrame()
        self.addWidget(frame, stretch=8)
        hBox = GuiBuilder.makeBoxLayoutIn(frame,False)
        GuiBuilder.makeLabelIn(hBox,"산학융합관").setStyleSheet("font-size: 20px; ")
        GuiBuilder.makeLabelIn(hBox,"입장").setStyleSheet("font-size: 20px;")


        self.Btn_Test = GuiBuilder.makePushButtonIn(
            self, 1, None, "QR"
        )
        
        self.Btn_setting = GuiBuilder.makePushButtonIn(
            self, 1, 'client/resource/settings.png', "Setting")

        self.Btn_exit = GuiBuilder.makePushButtonIn(
            self, 1, 'client/resource/exit.png', "Exit")
        self.Btn_exit.setStyleSheet("background-color: red;")


        parent.addLayout(self,stretch = stretch)
    
    def getBtnSetting(self):
        return self.Btn_setting

    def getBtnExit(self):
        return self.Btn_exit

    def getBtnQR(self):
        return self.Btn_Test