from PyQt5 import QtCore, QtWidgets

class GuiBuilder:

    def __init__(self, crtWindow):
        self.__crtWindow = crtWindow
        self.__callNum = 0
        self.__translate = QtCore.QCoreApplication.translate

    def makeHBoxLayoutIn(self, location : QtWidgets.QBoxLayout):
        
        hBox = QtWidgets.QHBoxLayout()
        location.addLayout(hBox)

        return hBox

    def makeVBoxLayoutIn(self, location : QtWidgets.QBoxLayout):
        
        vBox = QtWidgets.QVBoxLayout()
        location.addLayout(vBox)

        return vBox

    def makeLabelIn(self, location : QtWidgets.QLayout , text , alignFlag : QtCore.Qt.AlignmentFlag):
        label = QtWidgets.QLabel('')
        label.setObjectName(self.__makeObjectName("label"))
        label.setText(self.__translate(self.__crtWindow, text))
        label.setAlignment(alignFlag)
        location.addWidget(label)

        return label


    def __callNameNum(self):
        self.__callNum += 1
        return (self.__callNum - 1)

    def __makeObjectName(self, name):
        return self.__crtWindow + name + str(self.__callNameNum)

    # def makeFrame(self, location):
    #     frame = QtWidgets.QFrame(location)
    #     frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
    #     frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    #     frame.setFrameShadow(QtWidgets.QFrame.Raised)
    #     frame.setObjectName(self.__makeObjectName("frame"))
    
    #     return frame

    # def makeMainWindow(self, W, H):
    #     mainWindow = QtWidgets.QMainWindow()
    #     mainWindow.setObjectName(self.__crtWindow)
    #     mainWindow.resize(W, H)
    #     #mainWindow.setWindowTitle(self.__translate(self.__crtWindow, self.__crtWindow))

    #     return mainWindow

    # def makeCentralWidget(self, location):
    #     centralwidget = QtWidgets.QWidget(location)
    #     centralwidget.setObjectName(self.__makeObjectName("centralwidget"))
    #     location.setCentralWidget(centralwidget)

    #     return centralwidget

    # def makeStatusBar(self, location):
    #     statusbar = QtWidgets.QStatusBar(location)
    #     statusbar.setObjectName(self.__makeObjectName("statusbar"))
    #     location.setStatusBar(statusbar)

    #     return statusbar