from .face.camera import Camera
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-t", "--tick", default=50, help="밀리초 단위로 서버에 보내는 주기")
ap.add_argument("--ip", default="http://192.168.0.30:5000/match")
args = vars(ap.parse_args())
def main():
    cam = Camera('cam', tick=int(args["tick"]), ip=args["ip"])
    cam.start()

if __name__ == "__main__":
    main()