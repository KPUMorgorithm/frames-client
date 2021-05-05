from client.QR.qrcode import QRBuilder
from client.QR.view import QRWindow
from PyQt5 import  QtWidgets

class QRController:
    view: QRWindow
    LB_img : QtWidgets.QLabel
    Btn_close : QtWidgets.QPushButton
    
    def __init__(self, view : QRWindow, url):
        self.view = view
        self.LB_img = view.getLbImg()
        self.view.getBtnClose().clicked.connect(lambda: self.event_exit())

        self.updateView(url)

        self.view.exec_()
    
    def updateView(self, url):
        self.LB_img.setPixmap(QRBuilder.makeQRPixmapBy(url))
    
    def event_exit(self):
        self.view.close()

        
    #TODO n초 뒤에 꺼지게 해야함
