from PyQt5 import QtCore, QtWidgets


class GuiBuilder:

    def __init__(self, crtWindow, translate):
        self.__crtWindow = crtWindow
        self.__callNum = 0
        self.__translate = translate

    def makeMainWindow(self, W, H):
        mainWindow = QtWidgets.QMainWindow()
        mainWindow.setObjectName(self.__crtWindow)
        mainWindow.resize(W, H)
        #mainWindow.setWindowTitle(self.__translate(self.__crtWindow, self.__crtWindow))

        return mainWindow

    def makeCentralWidget(self, location):
        centralwidget = QtWidgets.QWidget(location)
        centralwidget.setObjectName(self.__makeObjectName("centralwidget"))
        location.setCentralWidget(centralwidget)

        return centralwidget

    def makeStatusBar(self, location):
        statusbar = QtWidgets.QStatusBar(location)
        statusbar.setObjectName(self.__makeObjectName("statusbar"))
        location.setStatusBar(statusbar)

        return statusbar


    def makeLabel(self,location,startX,startY,W,H,text=""):
        label = QtWidgets.QLabel(location)
        label.setGeometry(startX,startY,W,H)
        label.setObjectName(self.__makeObjectName("label"))
        label.setText(self.__translate(self.__crtWindow, text))

        return label

    # def makeLabel(self,location,text=""):
    #     label = QtWidgets.QLabel(location)
    #     label.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
    #     label.setScaledContents(True)
    #     label.setObjectName(self.__makeObjectName("label"))
    #     label.setText(self.__translate(self.__crtWindow, text))

    #     return label

    # def makeFrame(self, location, startX, startY, W, H):
    #     frame = QtWidgets.QFrame(location)
    #     frame.setGeometry(QtCore.QRect(startX,startY,W,H))
    #     frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    #     frame.setFrameShadow(QtWidgets.QFrame.Raised)
    #     frame.setObjectName(self.__makeObjectName("frame"))
    
    #     return frame

    def makeFrame(self, location):
        frame = QtWidgets.QFrame(location)
        frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName(self.__makeObjectName("frame"))
    
        return frame

    def __callNameNum(self):
        self.__callNum += 1
        return (self.__callNum - 1)

    def __makeObjectName(self, name):
        return self.__crtWindow + name + str(self.__callNameNum)