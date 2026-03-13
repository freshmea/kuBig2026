carSerial : main.o serial.o
	cc -o carSerial main.o serial.o

main.o : main.c serial.h
	cc -c main.c

serial.o : serial.c serial.h
	cc -c serial.c

clean :
	rm main.o serial.o carSerial
