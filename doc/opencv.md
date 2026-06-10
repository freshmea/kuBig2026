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
- 5교시: keyboard event, TickMeter, getTickCount 설명 및 실습
- 6교시: mouse event 설명 및 실습, example 실습
- 7교시: trackbar 설명 및 실습, file storage 설명 및 실습
- 8교시: 마스크 활용 설명 및 실습, example 실습
- 과제 : 없음
- 성과 기준 : OpenCV의 도형 그리기 함수와 텍스트 출력 함수를 사용할 수 있어야 한다. OpenCV의 이벤트 처리 함수를 사용할 수 있어야 한다. OpenCV의 트랙바와 파일 저장 기능을 사용할 수 있어야 한다.

---

## 2026-6-10

---

- 1교시: 복습, 밝기 조절, saturate_cast 설명 및 실습
- 2교시: constrast 조절, 곱하기, stretch, equalizeHist 설명 및 실습
- 3교시: 연산 함수(add, subtract, addWeighted, absdiff), bitwise 연산 설명 및 실습
- 4교시: 회선(convolution) 설명, filter2d, emboss 필터 실습
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
