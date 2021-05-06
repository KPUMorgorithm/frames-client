from PyQt5 import QtGui
import qrcode
from client.model.qr.Image import Image

class QRHelper:

    @staticmethod
    def makeQRPixmapBy(url) -> QtGui.QPixmap:
        
        return qrcode.make(url, image_factory = Image).pixmap()

 