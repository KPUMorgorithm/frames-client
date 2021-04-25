#from .face.camera import Camera
import argparse
from .gui.gui_main import Ui_Main
ap = argparse.ArgumentParser()

ap.add_argument("-t", "--tick", default=50, help="밀리초 단위로 서버에 보내는 주기")
ap.add_argument("--ip", default="http://192.168.0.30:5000/match")
ap.add_argument("--timeout", default=3, help="초 단위로 requests 타임아웃 주기")
args = vars(ap.parse_args())

def main():
    mainUi = Ui_Main(480,800)
    mainUi.startUi()

if __name__ == "__main__":
    main()
