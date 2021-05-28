from client.main_widget import Ui_Main

def main():
    mainUi = Ui_Main(480,800)
    mainUi.startUi()

if __name__ == "__main__":
    main()

# 카메라 안꺼졌을때 sudo service nvargus-daemon restart