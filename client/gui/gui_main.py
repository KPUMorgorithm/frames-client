from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from .gui_objectmaker import ObjectMaker

MAINWINDOW = "MainWindow"
TRANSLATE = QtCore.QCoreApplication.translate

OM = ObjectMaker(MAINWINDOW, TRANSLATE)

class Ui_Main(object):

    def __init__(self,W,H):
        
        super().__init__()
        self.__app = QtWidgets.QApplication(sys.argv)

        # Make MainWindow
        self.__MainWindow = OM.makeMainWindow(W,H)
 
        #Central Widget
        self.__centralwidget = OM.makeCentralWidget(self.__MainWindow)

        #StatusBar (하단)
        self.statusbar = OM.makeStatusBar(self.__MainWindow)

        # SetUp Ui
        self.setupUi()

        QtCore.QMetaObject.connectSlotsByName(self.__MainWindow)


    def setupUi(self):
        
        #TODO: CameraImage input
        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setGeometry(QtCore.QRect(10, 10, 512, 512))
        #self.graphicsView.setObjectName("graphicsView")

        # Temperature Frame
        self.FR_TEMP = OM.makeFrame(self.__centralwidget, 530, 10, 261, 181)
        
        self.LB_TEMP_Main = OM.makeLabel(self.FR_TEMP,110,10,56,12,"체온측정")
        self.LB_TEMP_Value = OM.makeLabel(self.FR_TEMP,30, 40, 56 ,12, "Value")
        self.LB_TEMP_Status = OM.makeLabel(self.FR_TEMP, 170, 40, 56, 12, "Status")

        

    def startUi(self):
        
        self.__MainWindow.show()
        sys.exit(self.__app.exec_())

