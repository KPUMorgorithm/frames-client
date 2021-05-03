from PyQt5 import QtCore, QtGui, QtWidgets
from client.gui.gui_builder import GuiBuilder
from client.setting import Config

class SettingWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.__config = Config()
        self.initUI()
        
        # self.exec_()

    def initUI(self):

        mainVBox = GuiBuilder.makeBoxLayoutIn(self, True)
        self.__initSettingVBox(mainVBox)
        self.__initCloseHBox(mainVBox)

    def __initSettingVBox(self, mainVBox):
        settingVBox = GuiBuilder.makeBoxLayoutIn(mainVBox, True)
        
        self.__initFacilityInputHBox(settingVBox)
        self.__initFacilityResultHBox(settingVBox)
        self.__initStateHBox(settingVBox)

    #TODO: Stretch 바꿔야 함
    def __initFacilityInputHBox(self, settingVBox):
        fInputHBox = GuiBuilder.makeBoxLayoutIn(settingVBox, False)

        GuiBuilder.makeLabelIn(fInputHBox,"건물 번호", 
            QtCore.Qt.AlignCenter).setStyleSheet("border: 1px solid black;")

        inputBox = QtWidgets.QLineEdit(str(self.__config.getFacilityNum()))
        fInputHBox.addWidget(inputBox)

    #TODO: 위에 값 받아서 리퀘스트보내야함
    def __initFacilityResultHBox(self, settingVBox):
        fResultHBox = GuiBuilder.makeBoxLayoutIn(settingVBox, False)
        GuiBuilder.makeLabelIn(fResultHBox, "대기중",
            QtCore.Qt.AlignCenter).setStyleSheet("border: 1px solid black;")

    #TODO: state값 따라 입장,퇴장 바꾸고 클릭할 때 마다 변경되게 
    def __initStateHBox(self, settingVBox):
        stateHBox = GuiBuilder.makeBoxLayoutIn(settingVBox, False)
        GuiBuilder.makePushButtonIn(stateHBox,1,None,
            str(self.__config.getState()))

    def __initCloseHBox(self, mainVBox):
        saveHBox = GuiBuilder.makeBoxLayoutIn(mainVBox, False)
        BTN_exit = GuiBuilder.makePushButtonIn(saveHBox,1,None,"닫기")
        BTN_exit.clicked.connect(lambda: self.event_BTN_exit())

    def event_BTN_exit(self):
        self.close()

