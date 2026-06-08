# Atmega128A

---

## 2026-6-08

---

```bash
gst-launch-1.0 v4l2src device=/dev/video0 ! \
  image/jpeg,width=640,height=480,framerate=30/1 ! \
  jpegdec ! videoconvert ! autovideosink sync=false

gst-launch-1.0 v4l2src device=/dev/video0 ! \
  video/x-h264,width=1280,height=720,framerate=30/1 ! \
  h264parse ! avdec_h264 ! videoconvert ! autovideosink sync=false

```

- 1교시: openCV 소개, 설치 방법 설명
- 2교시: 라이브러리 설명
- 3교시: 기본 클래스 (Point_, Size_, Rect_ ) 설명
- 4교시: 모던 cpp 기법 소개(범위 기반 for문, auto 키워드) 및 예제 설명
- 5교시: inputarray, outputarray 설명
- 6교시: assign 얕은 복사, clone, copyTo 깊은 복사 설명
- 7교시:
- 8교시:
- 과제 :
- 성과 기준 :

---

## 2026-3-24

---

```text
SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2104", MODE="0666"

```

- 1교시: 입력 예제 PINE - switch1
- 2교시: 입력 예제 PINE - switch2, chattering, debouncing 설명, pull-up, pull-down 저항
- 3교시: 예제 설명, udev 설정
- 4교시: fnd 예제 설명, fnd1.c 작성, switch_fnd 과제 실습
- 5교시: fnd2 타이머 인터럽트 fnd2.c
- 6교시: switch_fnd 과제 풀이
- 7교시: 외부 인터럽트
- 8교시: 타이머 인터럽트
- 과제 : 없음
- 성과 기준 : 스위치 입력, 디바운싱, 인터럽트의 관계를 설명하고 FND 예제를 수정할 수 있어야 한다.

---

## 2026-3-25

---

```text
// 윈도우 설정
usbipd list
usbipd bind --busid 7-1
usbipd attach --wsl --busid 7-1

// udev 설정 파일 내용 99_avrisp.rules
SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2104", MODE="0666"
SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", MODE="0666"

// udev 설정 적용
sudo udevadm control --reload-rules
sudo udevadm trigger
```

- 1교시: 8 bit 타이머 카운트/ 16 비트 타이머 카운트
- 2교시: 타이머 인터럽트 예제 설명, timer1com.c 작성
- 3교시: output compare 인터럽트 예제 설명, timer2ledleftright.c 작성
- 4교시: USART 개념 설명, 레지스트리 설명
- 5교시: uart1  uart1.c 작성
- 6교시: uart2 예제 설명, stdio.h 사용하기, 외부 라이브러리 사용하기
- 7교시: lcd 사용방법 - lcd.c, uart3 예제 설명,
- 8교시: uart3 예제 실습 - 컴퓨터에서  atmega로 보낼때 3개 이상 character 보내면 깨지는 문제가 있음
- 과제 : 없음
- 성과 기준 : UART 송수신 경로를 설명하고 버퍼 길이 또는 타이밍 문제를 재현해 볼 수 있어야 한다.

---

## 2026-3-26

---

- 1교시: ADC 개념 설명, 레지스트리 설명, adc.c 작성
- 2교시: 가변 저항 읽기
- 3교시: dc 모터 제어 예제 설명, dc_motor.c 작성
- 4교시: pwm 개념 설명, 레지스트리 설명, dc_pwm.c 작성
- 5교시: dc_pwm_vr 예제 설명, dc_pwm_vr.c 작성, 버저 예제 설명, buzzer.c 작성
- 6교시: i2c 개념 설명, 레지스트리 설명, i2c_tempHumi 작성
- 7교시: SPI 개념 설명, 레지스트리 설명, eeprom 개념 설명
- 8교시: eeprom 쓰기 예제, eeprom.c 작성 eeprom 읽기 예제
- 과제 : 없음
- 성과 기준 : ADC, PWM, I2C, SPI 예제 중 하나를 선택해 센서 입력과 출력 제어 흐름을 설명할 수 있어야 한다.

---

## 2026-3-27

---

- 1교시: 복습, servo 모터 제어 예제 설명, servo.c 작성
- 2교시: servo 모터 제어 예제 switch_servo.c 작성1
- 3교시: servo 모터 제어 예제 switch_servo.c 작성2
- 4교시: pir 센서 예제 설명, pir.c 작성
- 5교시: 교재 리뷰
- 6교시: 교재 리뷰
- 7교시: Pico2W 보드 설명, Pico2W 보드 실습
- 8교시: 시험
- 과제 : 없음
- 성과 기준 : 서보, PIR, Pico2W 확장 실습을 프로젝트 아이디어와 연결해 응용 과제를 제안할 수 있어야 한다.
