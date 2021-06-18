from PyQt5 import QtWidgets
from client.src.gui_builder import GuiBuilder


class TitleBarLayout(QtWidgets.QHBoxLayout):

    Btn_setting = QtWidgets.QPushButton
    Btn_exit = QtWidgets.QPushButton

    LB_fName : QtWidgets.QLabel
    LB_fState : QtWidgets.QLabel

    def __init__(self,parent : QtWidgets.QVBoxLayout, stretch, *args, **kwargs):
        super().__init__(*args, **kwargs)

        frame = QtWidgets.QFrame()
        self.addWidget(frame, stretch=8)
        hBox = GuiBuilder.makeBoxLayoutIn(frame,False)
        self.LB_fName = GuiBuilder.makeLabelIn(hBox,"산학융합관")
        self.LB_fName.setStyleSheet("font-size: 20px; ")
        self.LB_fState = GuiBuilder.makeLabelIn(hBox,"입장")
        self.LB_fState.setStyleSheet("font-size: 20px; ")

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