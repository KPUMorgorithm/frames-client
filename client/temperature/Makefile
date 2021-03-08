CC = g++
TARGET = temperature.dll
LIB = -lwiringPi -lwiringPiDev

$(TARGET) : temperature.o
	$(CC) --shared $(LIB) -o $@ $?
	rm *.o

temperature.o : temperature.cpp
	$(CC) -fPIC -c $?

clean :
	rm $(TARGET)