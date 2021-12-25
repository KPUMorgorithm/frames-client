## Overview

- 한국산업기술대학교 컴퓨터공학과 2021 캡스톤디자인 프로젝트입니다.  
- 소개 영상 
  [![](http://img.youtube.com/vi/X_F54xwaDtw/0.jpg)](https://youtu.be/X_F54xwaDtw?t=0s)   

- Jetson Nano 보드에 카메라와 체온인식 센서, 터치스크린을 장착한 단말기 입니다.  
    

#### Award

- 한국산업기술대학교 2021 캡스톤디자인 장려상
- KICS 2021 추계학술대회 14E-9, 14E-13 (웹 기반 실시간 코로나19 확진자 감시에 대한 연구, 안면인식 특징점의 가중치 합산 저장 알고리즘 연구)  
- IIBC 논문 심사중 


## Environment
#### Hardware
- Jetson Nano B01 (Jetpack 4.5.1)
- Lepton 2.5 + PureThermal 2 : 체온측정모듈
- IMX 219-AF : AF 카메라
- SunFounder 10.1 inch Touch Screen

#### Dependency

- OpenCV 4.5.2 compliled CUDA 10.2.89
- PyQT5
- face_recognition 1.3.0
- tensorflow 2.4
