#include <iostream>
#include <wiringPi.h>
#include <wiringPiSPI.h>

class Temperature
{
private:
    // int16_t iSensor; 
    int16_t iObject;
    double temperature;

    const int SCE = 22;
    const int spi_chn0 = 0;
    const int SPEED_1MHz = 1000000;
    const int SPI_MODE3 = 3;
    const int OBJECT = 0xA0;
    // const int SENSOR = 0xA1;
    
    int16_t SPI_COMMAND(uint8_t ADR){
	    uint8_t Data_Buf[3];

	    Data_Buf[0] = ADR;
	    Data_Buf[1] = 0x22;
	    Data_Buf[2] = 0x22;
	
	    digitalWrite(SCE, 0);  				// SCE LOW
	    delayMicroseconds(10);				// delay 10us

	    wiringPiSPIDataRW (spi_chn0, Data_Buf, 1);		// transfer 1st byte.
	    delayMicroseconds(10);				// delay 10us
	    wiringPiSPIDataRW (spi_chn0, Data_Buf+1, 1);	            // transfer 2nd byte
	    delayMicroseconds(10);				// delay 10us
	    wiringPiSPIDataRW (spi_chn0, Data_Buf+2, 1);		// transfer 3rd byte
	    delayMicroseconds(10);				// delay 10us

	    digitalWrite(SCE, 1);  				// SCE HIGH
	    return (Data_Buf[2]*256+Data_Buf[1]);			// High + Lo byte
    }

public: // Constructor
    Temperature(){
        temperature = 0;
        wiringPiSetup();					// Wiring Pi setup
 	    if(wiringPiSetupGpio() == -1) { return; }
	    pinMode(SCE, OUTPUT);				// SCE Port Output
	    digitalWrite(SCE,1);					// SCE high

	    wiringPiSPISetupMode(spi_chn0, SPEED_1MHz, SPI_MODE3); //SPI0, 1Mhz, SPI Mode3 Setting
	    delay(500);					// wait 500ms
    }

public: // public func
    
    // void check(){
    //     iSensor = SPI_COMMAND(SENSOR);
    //     delayMicroseconds(10);
    //     iObject = SPI_COMMAND(OBJECT);
    //     delay(500);				// Wait 500ms
    //     printf("Sensor : %5.2f  , Object : %5.2f \n", (double)iSensor/100, (double)iObject/100);    
    // }

    int16_t check(){
        iObject = SPI_COMMAND(OBJECT);
        delayMicroseconds(10);
        return iObject;
    }

};

extern "C" {
    Temperature* Temperature_new(){
        return new Temperature();
    }

    // void Temperature_check(Temperature* f){
    //     f->check();
    // }

    int16_t Temperature_check(Temperature* f){
        return f->check();
    }
}