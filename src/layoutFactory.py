from client.config.config import Config

from client.viewmodel.settingViewModel import SettingViewModel
from client.view.settingView import SettingWindow

from client.viewmodel.qrViewModel import QRViewModel
from client.view.qrView import QRWindow

from client.viewmodel.titlebarViewModel import TitleBarViewModel
from client.view.titlebarView import TitleBarLayout

from client.viewmodel.videoViewModel import VideoViewModel
from client.view.videoView import VideoLabel

from client.model.videoModel import Video
from client.model.temperatureModel import Temperature

from client.viewmodel.requestViewModel import RequestViewModel
from client.view.requestView import RequestLayout

class SingletonInstane(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonInstane, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class LayoutFactory(metaclass = SingletonInstane):
    
    def __init__(self):
        self.tp = Temperature("client/lib/temperature/temperature.dll")
        self.vd = Video()
        self.config = Config("config")
        
        print("LayoutFactory 생성됨(싱글톤 확인용)")

    def makeRequestModule(self, parent, stretch):
        view = RequestLayout(parent,stretch)
        RequestViewModel(view,self.vd,self.tp,self.config)
    
    def makeVideoModule(self, parent, stretch):
        view = VideoLabel(parent, stretch)
        VideoViewModel(view, self.vd, self.tp)

    def makeTitleBarModule(self, parent, stretch):
        view = TitleBarLayout(parent, stretch)
        TitleBarViewModel(view, self.makeSettingWindow)
    
    @classmethod
    def makeQRWindow(cls, url):
        view = QRWindow()
        QRViewModel(view, url)

    def makeSettingWindow(self):
        view = SettingWindow()
        SettingViewModel(view)