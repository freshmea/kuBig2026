# Atmega128 예제 인덱스

이 문서는 `atmega128/src` 아래 예제들을 주제별로 빠르게 찾기 위한 안내서다.

## 추천 학습 순서

1. GPIO: `led2.c`, `led3.c`, `led4.c`
2. 입력과 인터럽트: `switch1.c`, `switch2.c`, `interrupt1.c`, `interrupt_fnd.c`
3. 타이머: `timer0led.c`, `timer1com.c`, `timer2ledleftright.c`
4. UART/LCD: `uart1.c`, `uart2.c`, `uart3.c`, `lcd1.c`
5. ADC/PWM: `cds.c`, `dc_pwm.c`, `dc_pwm_vr.c`, `pwmbuzzer.c`
6. 센서/확장: `i2c_tempHumi.c`, `pir.c`, `external_eeprom.c`

## 수업 연결

- 1주차 임베디드 입문: GPIO와 스위치
- 2주차 임베디드 기초: 타이머와 UART
- 프로젝트 연결: PWM, 센서 입력, EEPROM, LCD 출력

## 학습 체크포인트

- 레지스터 설정값이 무엇을 의미하는지 말할 수 있는가
- 예제 하나를 복사하지 않고 수정해 새 동작을 만들 수 있는가
- 장치 연결 문제와 코드 문제를 구분할 수 있는가

## 빌드 참고

이 폴더는 각 `src/*.c` 파일마다 개별 `.elf` 타깃을 만든다. 예제 이름이 `uart1.c`라면 대응 타깃은 `uart1.elf`다.

## 연결 문서

- [Atmega128 진행사항](../doc/atmega128.md)
- [문제 해결 가이드](../doc/문제해결_가이드.md)
- [Atmega128 GPIO/UART 실습지](실습지.md)
