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
- 7교시: 카메라 세팅(usbipd)
- 8교시: gstream 예제 설명, gstreamer 설치 방법 설명
- 과제 : 없음
- 성과 기준 : OpenCV의 기본 클래스와 함수 사용법을 설명할 수 있어야 한다. OpenCV를 이용해 카메라에서 영상을 받아올 수 있어야 한다.

---

## 2026-6-09

---

- 1교시: 복습
- 2교시: 비디오 저장 코드
- 3교시: 도형 그리기 (line, rectangle, circle, ellipse) 설명 및 AI 실습
- 4교시: putText, freetype2 설명 및 실습
- 5교시:
- 6교시:
- 7교시:
- 8교시:
- 과제 : 없음
- 성과 기준 :

---

## 2026-6-10

---

- 1교시:
- 2교시:
- 3교시:
- 4교시:
- 5교시:
- 6교시:
- 7교시:
- 8교시:
- 과제 : 없음
- 성과 기준 :

---

## 2026-6-11

---

- 1교시:
- 2교시:
- 3교시:
- 4교시:
- 5교시:
- 6교시:
- 7교시:
- 8교시:
- 과제 : 없음
- 성과 기준 :

---

## 2026-6-12

---

- 1교시:
- 2교시:
- 3교시:
- 4교시:
- 5교시:
- 6교시:
- 7교시:
- 8교시: 시험
- 과제 : 없음
- 성과 기준 :
