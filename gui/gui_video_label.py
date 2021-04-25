from ..src.temperature.temperature import Temperature
from PyQt5 import QtGui, QtWidgets, QtCore

class VideoLabel(QtWidgets.QLabel):

    def __init__(self, *args, **kwargs):
        super(VideoLabel, self).__init__(*args, **kwargs)
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        self.setScaledContents(True)
        
        self.tp = Temperature("client/src/temperature/temperature.dll")

    def pixmapEvent(self, pixmap):
        qp = QtGui.QPainter(pixmap)

        tem = self.tp.checkTemperature()
        qp.setPen(self._selectPenByTem(tem))
        qp.setFont(QtGui.QFont("Arial", 30))
        try:
            qp.drawText(
                pixmap.rect(), QtCore.Qt.AlignTop | QtCore.Qt.AlignRight, 
                str(tem))
        except:
            pass
        finally:
            self.setPixmap(pixmap)
            qp.end()
    
    def getTemperautre(self):
        return self.tp

    def _selectPenByTem(self, tem):
        if tem < 35:
            color = QtCore.Qt.gray
        elif tem < 37:
            color = QtCore.Qt.green
        elif tem < 37.5:
            color = QtCore.Qt.yellow
        else:
            color = QtCore.Qt.red
        
        pen = QtGui.QPen(color, 5)

        return pen