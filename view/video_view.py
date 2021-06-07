from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import numpy as np
class VideoLabel(QtWidgets.QLabel):

    def __init__(self, parent : QtWidgets.QBoxLayout, stretch,*args, **kwargs):
        super(VideoLabel, self).__init__(*args, **kwargs)
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        self.setScaledContents(True)
        
        parent.addWidget(self, stretch=stretch)

    @pyqtSlot(QPixmap)
    def updateView(self,pixmap):
        self.setPixmap(pixmap)