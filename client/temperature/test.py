import wiringpi
import sys
import numpy as np
import time

SCE = 22
spi_chn0 = 0
SPEED_1MHz = 1000000
SPI_MODE3 = 3
OBJECT = 0xA0
SENSOR = 0xA1

def SPI_COMMAND(ADR):

    wiringpi.digitalWrite(SCE, 0)
    wiringpi.delayMicroseconds(10)

    sendData = bytes(ADR)
    (retlen,recvData) = wiringpi.wiringPiSPIDataRW(spi_chn0, sendData)
    wiringpi.delayMicroseconds(10)

    sendData = bytes(np.uint8(0x22))
    sendData = b'"'
    (retlen1,recvData1) = wiringpi.wiringPiSPIDataRW(spi_chn0, sendData)
    wiringpi.delayMicroseconds(10)
    
    sendData = bytes(0x22)
    (retlen2,recvData2) = wiringpi.wiringPiSPIDataRW(spi_chn0, sendData)
    wiringpi.delayMicroseconds(10)
    
    wiringpi.digitalWrite(SCE, 1)

    #recvData1 = int.from_bytes(recvData1, byteorder='big')
    #recvData2 = int.from_bytes(recvData2, byteorder='big')
    print ('recvData0: ',recvData)
    print ('retlen 0: ',retlen)
    print ('recvData1: ',recvData1)
    print ('retlen 1: ',retlen1)
    print ('recvData2: ',recvData2)
    print ('retlen 2: ',retlen2)
    #return (recvData2*256+recvData1)
    return 0


iSensor = 0 
iObject = 0

wiringpi.wiringPiSetup()

if wiringpi.wiringPiSetupGpio() == -1:
    print("SetupGpio == -1")
    sys.exit()

wiringpi.pinMode(SCE, 1)
wiringpi.digitalWrite(SCE, 1)

wiringpi.wiringPiSPISetupMode(spi_chn0, SPEED_1MHz, SPI_MODE3)
#wiringpi.wiringPiSPISetup(spi_chn0, SPEED_1MHz)
time.sleep(0.5)

while(True):
    #iSensor = SPI_COMMAND(SENSOR)
    wiringpi.delayMicroseconds(10)
    iObject = SPI_COMMAND(OBJECT)
    time.sleep(2)

    #print("Sensor : %5.2f , Object : %5.2f") % (iSensor/100, iObject/100)

    



