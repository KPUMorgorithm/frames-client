from client.src.config.config import Config

from client.settings.controller import SettingController
from client.settings.view import SettingWindow

from client.QR.controller import QRController
from client.QR.view import QRWindow

from client.titlebar.controller import TitleBarController
from client.titlebar.view import TitleBarLayout

from client.video.controller import VideoController
from client.video.view import VideoLabel
from client.video.video import Video

from client.src.temperature.temperature import Temperature

from client.request.controller import RequestController
from client.request.view import RequestLayout

class SingletonInstane(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonInstane, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class LayoutFactory(metaclass = SingletonInstane):
    
    def __init__(self):
        self.tp = Temperature("client/src/temperature/temperature.dll")
        self.vd = Video()
        self.config = Config("config")
        
        print("LayoutFactory 생성됨(싱글톤 확인용)")

    def makeRequestModule(self, parent, stretch):
        view = RequestLayout(parent,stretch)
        RequestController(view,self.vd,self.tp,self.config)
    
    def makeVideoModule(self, parent, stretch):
        view = VideoLabel(parent, stretch)
        VideoController(view, self.vd, self.tp)

    def makeTitleBarModule(self, parent, stretch):
        view = TitleBarLayout(parent, stretch)
        TitleBarController(view, self.makeSettingWindow)
    
    @classmethod
    def makeQRWindow(cls, url):
        view = QRWindow()
        QRController(view, url)

    def makeSettingWindow(self):
        view = SettingWindow()
        SettingController(view)