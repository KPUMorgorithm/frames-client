from abc import *

class AbstractData(metaclass=ABCMeta):

    @abstractclassmethod
    def __init__(self):
        self.qss = ""
        self.data = ""

class UncheckedLandmarkStateData(AbstractData):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
 
        self.data = "얼굴을 화면 중앙에 위치해주세요"
        self.qss = """
                width: 100%;
                color: #FFFFFF;
                background-color: #ded119;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """

class CheckedStateData(AbstractData):

    def __init__(self, temp, name, *args, **kwargs):
        super().__init__(*args,**kwargs)
 
        self.data = str(temp) + "\n" + name
        self.qss = """
                width: 100%;
                color: #FFFFFF;
                background-color: #719C70;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """
    
class UnknownStateData(AbstractData):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.data = "인식에 실패했습니다."
        self.qss = """
                width: 100%;
                color: #FFFFFF;
                background-color: #392f31;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """

class MaskedStateData(AbstractData):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.data = "마스크를 탈의해주세요."
        self.qss = """
                width: 100%;
                color: #FFFFFF;
                background-color: #F24A33;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """

class LowTemperatureStateData(AbstractData):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.data = "체온이 측정되지 않았습니다"
        self.qss = """
                width: 100%;
                color: #FFFFFF;
                background-color: #333333;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """

class TimeoutStateData(AbstractData):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.data = "서버와의 연결에 실패했습니다.\n관리자에게 문의해주세요."
        self.qss = """
                width: 100%;
                color: #FFFFFF;
                background-color: #F24A33;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """
    

