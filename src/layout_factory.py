from client.config.config import Config

from client.viewmodel.setting_viewmodel import SettingViewModel
from client.view.setting_view import SettingWindow

from client.viewmodel.qr_viewmodel import QRViewModel
from client.view.qr_view import QRWindow

from client.viewmodel.titlebar_viewmodel import TitleBarViewModel
from client.view.titlebar_view import TitleBarLayout

from client.viewmodel.video_viewmodel import VideoViewModel
from client.view.video_view import VideoLabel

from client.model.video.video_model import Video
from client.model.temperature.thermal_adapter import TemperatureAdapter

from client.viewmodel.request_viewmodel import RequestViewModel
from client.view.request_view import RequestLayout

from client.src.singleton_instance import SingletonInstane

QSSPATH = "client/resource/qss/main_stylesheet.qss"

class LayoutFactory(metaclass = SingletonInstane):
    
    def __init__(self):
        self.vd = Video()
        self.vd.start()
        self.tp = TemperatureAdapter()
        # self.tp=None
        self.config = Config("config")

        print("LayoutFactory 생성됨(싱글톤 확인용)")

    def makeRequestModule(self, parent, stretch):
        view = RequestLayout(parent,stretch)
        vm = RequestViewModel(view,self.vd,self.tp,self.config, self.makeQRWindow)
        self.reqStart, self.reqStop = vm.startReq, vm.stopReq

    def makeVideoModule(self, parent, stretch):
        view = VideoLabel(parent, stretch)
        VideoViewModel(view, self.vd, self.tp)
        
    def makeTitleBarModule(self, parent, stretch):
        view = TitleBarLayout(parent, stretch)
        vm = TitleBarViewModel(view, self.makeSettingWindow, self.killFunc, self.config)
        self.changeFunc = vm.changeLabel

    @classmethod
    def makeQRWindow(cls, url):
        #TODO 위치 조정(클라이언트 가운데로)
        view = QRWindow(QSSPATH)
        QRViewModel(view, url)
        return True

    def makeSettingWindow(self):
        #TODO 위치 조정(클라이언트 가운데로)
        self.reqStop()
        print(self.run)
        view = SettingWindow(QSSPATH)
        SettingViewModel(view, self.config, self.changeFunc)
        self.reqStart()

    def killFunc(self):
        self.vd.running=False
        self.vd.stop()
        del self.tp