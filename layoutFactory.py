from client.video.controller import VideoController
from client.video.view import VideoLabel
from client.video.video import Video

from client.src.temperature.temperature import Temperature

from client.request.controller import RequestController
from client.request.view import RequestLayout

class LayoutFactory:
    
    def __init__(self):
        self.tp = Temperature("client/src/temperature/temperature.dll")
        self.vd = Video()

    def makeRequestModule(self, parent, stretch):
        view = RequestLayout(parent,stretch)
        RequestController(self.vd,self.tp,view)
    
    def makeVideoModule(self, parent, stretch):
        view = VideoLabel(parent, stretch)
        VideoController(view, self.vd, self.tp)
