from client.view.setting_view import SettingWindow
from PyQt5 import QtWidgets

from client.config.config import Config
from client.model.request.request_helper import RequestHelper
from client.model.request.request_config_state import State

class SettingViewModel:

    Btn_fNum : QtWidgets.QRadioButton
    Btn_fName : QtWidgets.QRadioButton
    LE_fEdit : QtWidgets.QLineEdit
    Btn_sIn : QtWidgets.QRadioButton
    Btn_sOut : QtWidgets.QRadioButton

    view: SettingWindow

    def __init__(self, view : SettingWindow, config : Config):
        self.view = view
        self.Btn_fNum = view.getBtnfNum()
        self.Btn_fName = view.getBtnfName()
        self.Btn_sIn = view.getBtnsIn()
        self.Btn_sOut = view.getBtnsOut()
        self.LE_fEdit = view.getLEfEdit()

        self.__config = config

        view.getBtnClose().clicked.connect(lambda: self.view.close())
        view.getBtnSave().clicked.connect(lambda: self.__eventSaveBtn())
        # str(self.__config.getFacilityNum()
        self.view.exec_()

    def __eventSaveBtn(self):
        #TODO   정보를 받은 채로 request를 보내야함
        #       성공할 시 config 저장 후 self.타이틀바 새로고침, self.close()
        #       실패할 시 메세지 출력

        text = self.LE_fEdit.text()
        # resultState : State = None

        resultState , isStateIn = RequestHelper.requestConfig(self.__config, 
            self.Btn_fNum.isChecked(),
            self.Btn_fName.isChecked(),
            self.Btn_sIn.isChecked(),
            self.Btn_sOut.isChecked(),
            text)

        print(resultState)
        if resultState == State.ACCEPT:
            self.__config.iniSave(text, int(isStateIn))
