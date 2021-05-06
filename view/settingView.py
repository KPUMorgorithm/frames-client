from PyQt5 import QtCore, QtWidgets
from client.src.gui_builder import GuiBuilder

class SettingWindow(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.initUI()

    #/device/facility?deviceId=~~&~~~
    def initUI(self):

        mainVBox = GuiBuilder.makeBoxLayoutIn(self, True)

        facilityGroupBox = GuiBuilder.makeGroupBoxIn(mainVBox)
        facilityVBox = GuiBuilder.makeBoxLayoutIn(facilityGroupBox, True)
        facilitySelectHBox = GuiBuilder.makeBoxLayoutIn(facilityVBox, False)
        self.Btn_fNum = GuiBuilder.makeRadioButton(facilitySelectHBox,"건물 번호")
        self.Btn_fName = GuiBuilder.makeRadioButton(facilitySelectHBox,"건물 이름")
        self.LE_facilityEdit = GuiBuilder.makeLineEditIn(facilityVBox,1,"0")

        stateGroupBox = GuiBuilder.makeGroupBoxIn(mainVBox)
        stateSelectHBox = GuiBuilder.makeBoxLayoutIn(stateGroupBox, False)
        self.Btn_stateIn = GuiBuilder.makeRadioButton(stateSelectHBox,"입구")
        self.Btn_stateOut = GuiBuilder.makeRadioButton(stateSelectHBox,"출구")

        closeHBox = GuiBuilder.makeBoxLayoutIn(mainVBox, False)
        
        self.Btn_save = GuiBuilder.makePushButtonIn(closeHBox,1,None,"저장")
        self.Btn_close = GuiBuilder.makePushButtonIn(closeHBox,1,None,"닫기")


    def getBtnfNum(self):
        return self.Btn_fNum

    def getBtnfName(self):
        return self.Btn_fName
    
    def getBtnsIn(self):
        return self.Btn_stateIn
    
    def getBtnsOut(self):
        return self.Btn_stateOut
    
    def getLEfEdit(self):
        return self.LE_facilityEdit
    
    def getBtnSave(self):
        return self.Btn_save
    
    def getBtnClose(self):
        return self.Btn_close

