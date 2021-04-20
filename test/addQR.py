# 실행 타이밍: 검증서버로 Unknown을 받으면
# 1. WAS의 '등록 URL'에 특징점과 이름, 기기번호 등 상세 로그를 보냄 
# 2. WAS에서는 그 정보를 가지고 이름과 전화번호를 입력할 수 있는 고유의 폼을 보냄
# 3. WAS에서 회원 등록과 로그 등록을 수행함


# pip install qpcode

import qrcode

def testReceiveQR():
    testInput = "https://www.naver.com/"

    img = QRHandler.conversionURLtoQR(testInput)
    img.save('test.jpg')

class QRHandler:

    @staticmethod
    def conversionURLtoImg(url):
        img = qrcode.make(url)
        return img