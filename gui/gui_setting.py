from PyQt5 import QtCore, QtGui, QtWidgets
from client.gui.gui_builder import GuiBuilder
from client.setting import Config

class SettingWindow(QtWidgets.QDialog):

    isfNum : bool

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
        #TODO: Stretch 바꿔야 함
        #TODO: 토글 이벤트 달기
        facilitySelectHBox = GuiBuilder.makeBoxLayoutIn(mainVBox, False)
        BTN_fnum = self.__setFnumBtn(facilitySelectHBox)
        BTN_fName = self.__setFnameBtn(facilitySelectHBox)
        LE_facilityEdit = GuiBuilder.makeLineEditIn(mainVBox,1,str(self.__config.getFacilityNum()))
        
        stateSelectHBox = GuiBuilder.makeBoxLayoutIn(mainVBox, False)
        BTN_stateIn = GuiBuilder.makePushButtonIn(stateSelectHBox,1,None,"입구")
        BTN_stateOut = GuiBuilder.makePushButtonIn(stateSelectHBox,1,None,"출구")
        
        closeHBox = GuiBuilder.makeBoxLayoutIn(mainVBox, False)
        BTN_save = self.__setSaveBtn(closeHBox)
        BTN_close = self.__setCloseBtn(closeHBox)

    def __setSaveBtn(self, parent):
        btn = GuiBuilder.makePushButtonIn(parent,1,None,"저장")
        #TODO   정보를 받은 채로 request를 보내야함
        #       성공할 시 config 저장 후 self.타이틀바 새로고침, self.close()
        #       실패할 시 메세지 출력

    def __setCloseBtn(self, parent):
        btn = GuiBuilder.makePushButtonIn(parent,1,None,"닫기")
        btn.clicked.connect(lambda: self.close())
        return btn

    def __setFnumBtn(self, parent):
        btn = GuiBuilder.makePushButtonIn(parent,1,None,"건물 번호")
        btn.setCheckable(True)
        btn.toggle()
        return btn

    def __setFnameBtn(self, parent):
        btn = GuiBuilder.makePushButtonIn(parent,1,None,"건물 이름")
        btn.setCheckable(True)
        return btn