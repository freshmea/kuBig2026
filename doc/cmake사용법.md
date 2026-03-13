# CMake 사용법

---

- CMakeLists.txt 로 빌드 하는 방법

```shell
mkdir build
cd build
cmake ..
make
```

- makefile 사용법
  - 우선 소스를 오브젝트로 만든다.

```shell
cc -c main.c
cc -c serial.c
cc -o carSerial main.o serial.o
```

```text
carSerial : main.o serial.o
	cc -o carSerial main.o serial.o

main.o : main.c serial.h
	cc -c main.c

serial.o : serial.c serial.h
	cc -c serial.c

clean :
	rm main.o serial.o carSerial
```
