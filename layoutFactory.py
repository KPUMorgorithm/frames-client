from client.request.controller import RequestController
from client.request.view import RequestLayout
from client.request import *

class layoutFactory:
    
    @staticmethod
    def makeRequestModule(parent, stretch ,vd, tp):
        view = RequestLayout(parent,stretch)
        RequestController(vd,tp,view)
