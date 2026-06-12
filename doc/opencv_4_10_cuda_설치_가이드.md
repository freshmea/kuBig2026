# OpenCV 4.10 CUDA 설치 가이드 (Ubuntu 22.04)

이 문서는 Ubuntu 22.04 환경에서 OpenCV 4.10을 CUDA, GStreamer, aruco 사용 가능 상태로 소스 빌드하는 절차를 정리합니다.

## 1. 개요

- Ubuntu 22.04 기본 apt 저장소의 OpenCV는 4.5.4입니다.
- OpenCV 4.10 + CUDA를 사용하려면 소스 빌드가 필요합니다.
- aruco는 opencv_contrib 모듈이 필요합니다.
- QR은 objdetect 모듈에서 사용합니다.

## 2. 사전 확인

```bash
lsb_release -ds
nvcc --version
nvidia-smi
cmake --version
gcc --version
```

권장 확인 포인트:

- `nvcc`가 정상 출력되는지
- `nvidia-smi`에서 GPU가 인식되는지
- CMake 3.20 이상

## 3. 의존성 패키지 설치

```bash
sudo apt update
sudo apt install -y \
  build-essential git pkg-config cmake \
  libgtk-3-dev \
  libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
  libxvidcore-dev libx264-dev \
  libjpeg-dev libpng-dev libtiff-dev libopenexr-dev \
  libtbb2 libtbb-dev libdc1394-dev libeigen3-dev \
  gstreamer1.0-tools libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
  python3-dev python3-numpy
```

## 4. 소스 다운로드 (OpenCV 4.10.0)

```bash
cd ~
git clone --branch 4.10.0 https://github.com/opencv/opencv.git
git clone --branch 4.10.0 https://github.com/opencv/opencv_contrib.git
mkdir -p ~/opencv/build
cd ~/opencv/build
```

## 5. CMake 설정 (최소 옵션 세트)

RTX 3060 Laptop GPU 기준 아키텍처는 `8.6`입니다.

```bash
cmake \
  -D CMAKE_BUILD_TYPE=Release \
  -D CMAKE_INSTALL_PREFIX=/usr/local/opencv-4.10 \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
  -D WITH_CUDA=ON \
  -D OPENCV_DNN_CUDA=ON \
  -D CUDA_ARCH_BIN=8.6 \
  -D WITH_GSTREAMER=ON \
  -D BUILD_opencv_aruco=ON \
  -D BUILD_opencv_objdetect=ON \
  -D BUILD_TESTS=OFF \
  -D BUILD_PERF_TESTS=OFF \
  -D BUILD_EXAMPLES=OFF \
  ..
```

참고:

- 다른 GPU라면 `CUDA_ARCH_BIN`을 장치에 맞게 변경합니다.
- DNN CUDA 성능/호환성 확보를 위해 cuDNN 설치를 권장합니다.

## 6. 빌드 및 설치

```bash
cd ~/opencv/build
make -j"$(nproc)"
sudo make install
sudo ldconfig
```

## 7. 설치 검증

### 7.1 pkg-config 버전 확인

```bash
pkg-config --modversion opencv4
```

### 7.2 Python에서 빌드 정보 확인

```bash
python3 - <<'PY'
import cv2
print('OpenCV version:', cv2.__version__)
info = cv2.getBuildInformation()
print('CUDA enabled:', 'NVIDIA CUDA:                   YES' in info)
print('GStreamer enabled:', 'GStreamer:                    YES' in info)
print('cuDNN enabled:', 'cuDNN:                         YES' in info)
PY
```

## 8. CMake 프로젝트 연동 방법

시스템 기본 OpenCV(4.5.4) 대신 설치한 OpenCV(4.10)를 강제로 사용하려면:

```bash
cmake -D OpenCV_DIR=/usr/local/opencv-4.10/lib/cmake/opencv4 ..
```

또는 환경 변수 사용:

```bash
export CMAKE_PREFIX_PATH=/usr/local/opencv-4.10:$CMAKE_PREFIX_PATH
```

## 9. 문제 해결

### 9.1 CUDA가 NO로 뜨는 경우

- `nvcc --version` 확인
- CMake 캐시 삭제 후 재설정

```bash
cd ~/opencv/build
rm -rf CMakeCache.txt CMakeFiles
```

### 9.2 GStreamer가 NO로 뜨는 경우

- `libgstreamer1.0-dev`, `libgstreamer-plugins-base1.0-dev` 설치 확인
- CMake 재설정

### 9.3 opencv_contrib 관련 에러

- `OPENCV_EXTRA_MODULES_PATH` 경로 확인
- `opencv`와 `opencv_contrib` 버전(태그) 일치 확인

## 10. 선택 사항: 제거/재설치

설치 경로를 분리했으므로 필요 시 디렉토리 삭제로 정리할 수 있습니다.

```bash
sudo rm -rf /usr/local/opencv-4.10
sudo ldconfig
```

재설치 시 5단계부터 다시 진행하면 됩니다.
