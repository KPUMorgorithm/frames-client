from PyQt5 import QtWidgets

class VideoLabel(QtWidgets.QLabel):

    def __init__(self, parent : QtWidgets.QBoxLayout, stretch,*args, **kwargs):
        super(VideoLabel, self).__init__(*args, **kwargs)
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        self.setScaledContents(True)
        
        parent.addWidget(self, stretch=stretch)

