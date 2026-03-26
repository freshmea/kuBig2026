# Atmega128A

---

## 2026-3-23

---

- 1교시: 마이크로 컨트롤러란
- 2교시: Atmega128A 설명, 아두이노 보드 설명
- 3교시: Atmega128A 내부 모듈 설명 - cpu, flash, sram, eeprom, gpio, uart, adc, timer
- 4교시: CMake 프로젝트 파일 작성, main.c 작성
- 5교시: 빌드 실행, isp mk2 usb 인식, windows usbipd 설치, wsl2 usbip 설치, usbipd wsl2 연결
- 6교시: led 깜빡이 예제 - main.c led1.c
- 7교시: led 비트연산 예제 - led2.c led3.c
- 8교시: 복합 비트 연산자로 특정 비트 제어 - led4.c
- 과제 : 책 1 chapter 2 chapter 읽기(기초 CS 개념)

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

---

## 2026-3-26

---

- 1교시: ADC 개념 설명, 레지스트리 설명, adc.c 작성
- 2교시: 가변 저항 읽기
- 3교시:
- 4교시:
- 5교시:
- 6교시:
- 7교시:
- 8교시:
- 과제 : 없음
