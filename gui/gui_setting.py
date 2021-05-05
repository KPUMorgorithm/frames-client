from PyQt5 import QtCore, QtGui, QtWidgets
from client.src.gui.gui_builder import GuiBuilder
from client.setting import Config

class SettingWindow(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.__config = Config()
        self.initUI()
        
        self.exec_()

    #/device/facility?deviceId=~~&~~~
    def initUI(self):

        mainVBox = GuiBuilder.makeBoxLayoutIn(self, True)

        facilityGroupBox = GuiBuilder.makeGroupBoxIn(mainVBox)
        facilityVBox = GuiBuilder.makeBoxLayoutIn(facilityGroupBox, True)
        facilitySelectHBox = GuiBuilder.makeBoxLayoutIn(facilityVBox, False)
        self.Btn_fNum = GuiBuilder.makeRadioButton(facilitySelectHBox,"건물 번호")
        self.Btn_fName = GuiBuilder.makeRadioButton(facilitySelectHBox,"건물 이름")
        self.LE_facilityEdit = GuiBuilder.makeLineEditIn(facilityVBox,1,str(self.__config.getFacilityNum()))

        stateGroupBox = GuiBuilder.makeGroupBoxIn(mainVBox)
        stateSelectHBox = GuiBuilder.makeBoxLayoutIn(stateGroupBox, False)
        self.Btn_stateIn = GuiBuilder.makeRadioButton(stateSelectHBox,"입구")
        self.Btn_stateOut = GuiBuilder.makeRadioButton(stateSelectHBox,"출구")

        closeHBox = GuiBuilder.makeBoxLayoutIn(mainVBox, False)
        
        self.__setSaveBtn(closeHBox)
        self.__setCloseBtn(closeHBox)

    def __setSaveBtn(self, parent):
        btn = GuiBuilder.makePushButtonIn(parent,1,None,"저장")
        btn.clicked.connect(lambda: self.__eventSaveBtn())
        
    def __eventSaveBtn(self):
        #TODO   정보를 받은 채로 request를 보내야함
        #       성공할 시 config 저장 후 self.타이틀바 새로고침, self.close()
        #       실패할 시 메세지 출력
        print(self.Btn_fNum.isChecked())
        print(self.Btn_fName.isChecked())
        print(self.Btn_stateIn.isChecked())
        print(self.Btn_stateOut.isChecked())
        print(self.LE_facilityEdit.text())

    def __setCloseBtn(self, parent):
        btn = GuiBuilder.makePushButtonIn(parent,1,None,"닫기")
        btn.clicked.connect(lambda: self.close())
        return btn
