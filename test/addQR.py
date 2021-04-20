# 실행 타이밍: 검증서버로 Unknown을 받으면
# 1. WAS의 '등록 URL'에 특징점과 이름, 기기번호 등 상세 로그를 보냄 
# 2. WAS에서는 그 정보를 가지고 이름과 전화번호를 입력할 수 있는 고유의 폼을 보냄
# 3. WAS에서 회원 등록과 로그 등록을 수행함


# pip install qrcode

import pyqrcode

def testReceiveQR():
    testInput = "https://www.naver.com/"

    QRHandler.conversionURLtoImg(testInput)
    #img.save('test.jpg')
#https://pythonhosted.org/PyQRCode/rendering.html
class QRHandler:

    @staticmethod
    def conversionURLtoImg(url):
        img = pyqrcode.create(url)
        img.svg('uca-url.svg', scale=8)
        img.eps('uca-url.eps', scale=2)
        print(img.terminal(quiet_zone=1))

testReceiveQR()