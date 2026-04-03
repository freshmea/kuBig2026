# MQTT 예제 안내

이 문서는 `network/mqttPub.c` 예제를 수업에서 어떻게 사용할지 설명한다.

## 학습 목표

- MQTT broker 주소와 topic 개념을 이해한다.
- C 프로그램에서 외부 라이브러리를 링크하는 흐름을 본다.
- 임베디드 프로젝트 이전에 네트워크 메시지 송신 개념을 익힌다.

## 실행 인자

기본 형식:

```bash
./mqttPub [broker] [client_id] [topic] [message]
```

예시:

```bash
./mqttPub tcp://127.0.0.1:1883 student01 school/test "hello mqtt"
```

## 수업 포인트

- broker 주소를 왜 문자열 상수로 두는지 설명한다.
- client id와 topic이 각각 무엇을 의미하는지 구분한다.
- 메시지 전송 실패 시 네트워크 문제인지 라이브러리 문제인지 먼저 나눈다.

## 확장 과제

- 센서 값 형식의 문자열을 만들어 publish 하기
- 명령행 인자가 없을 때 사용자 입력을 받도록 수정하기
- subscribe 예제를 추가해 송수신을 둘 다 확인하기
