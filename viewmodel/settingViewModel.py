from client.view.settingView import SettingWindow
from PyQt5 import QtWidgets

class SettingViewModel:

    Btn_fNum : QtWidgets.QRadioButton
    Btn_fName : QtWidgets.QRadioButton
    LE_fEdit : QtWidgets.QLineEdit
    Btn_sIn : QtWidgets.QRadioButton
    Btn_sOut : QtWidgets.QRadioButton

    view: SettingWindow

    def __init__(self, view : SettingWindow):
        self.view = view
        self.Btn_fNum = view.getBtnfNum()
        self.Btn_fName = view.getBtnfName()
        self.Btn_sIn = view.getBtnsIn()
        self.Btn_sOut = view.getBtnsOut()
        self.LE_fEdit = view.getLEfEdit()

        view.getBtnClose().clicked.connect(lambda: self.view.close())
        view.getBtnSave().clicked.connect(lambda: self.__eventSaveBtn)
        # str(self.__config.getFacilityNum()
        self.view.exec_()

    def __eventSaveBtn(self):
        #TODO   정보를 받은 채로 request를 보내야함
        #       성공할 시 config 저장 후 self.타이틀바 새로고침, self.close()
        #       실패할 시 메세지 출력
        print(self.Btn_fNum.isChecked())
        print(self.Btn_fName.isChecked())
        print(self.Btn_sIn.isChecked())
        print(self.Btn_sOut.isChecked())
        print(self.LE_fEdit.text())
