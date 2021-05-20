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

from client.src.main_threadpool import MainThreadPool
from client.src.singleton_instance import SingletonInstane

LIBTEMPATH = "client/lib/temperature/temperature.dll"
class LayoutFactory(metaclass = SingletonInstane):
    
    def __init__(self):
        self.vd = Video()
        # self.tp = Temperature(LIBTEMPATH)
        self.tp = None
        self.config = Config("config")
        self.thPool = MainThreadPool(10)

        self.thPool.addThreadPool(self.vd.run)
        # self.thPool.addThreadPool(self.tp.checkHighestTemp)

        self.thPool.addKillThreadFunc(self.__killSelf)

        print("LayoutFactory 생성됨(싱글톤 확인용)")

    def makeRequestModule(self, parent, stretch):
        view = RequestLayout(parent,stretch)
        vm = RequestViewModel(view,self.vd,self.tp,self.config)
        self.thPool.addThreadPool(vm.checkQueue)
        self.thPool.addKillThreadFunc(vm.stopRequest)
    
    def makeVideoModule(self, parent, stretch):
        view = VideoLabel(parent, stretch)
        vm = VideoViewModel(view, self.vd, self.tp)
        self.thPool.addThreadPool(vm.updateView)
        self.thPool.addKillThreadFunc(vm.stopVideo)

    def makeTitleBarModule(self, parent, stretch):
        view = TitleBarLayout(parent, stretch)
        TitleBarViewModel(view, self.makeSettingWindow, self.thPool.killAllThread)
    
    @classmethod
    def makeQRWindow(cls, url):
        #TODO 위치 조정(클라이언트 가운데로)
        view = QRWindow()
        QRViewModel(view, url)

    def makeSettingWindow(self):
        #TODO 위치 조정(클라이언트 가운데로)
        view = SettingWindow()
        SettingViewModel(view)

    def __killSelf(self):
        del self