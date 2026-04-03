# Tools Guide

이 디렉터리는 `kuBig2026` 저장소에서 반복적으로 쓰는 운영 스크립트와 자동화 도구를 모아둔 곳이다.

현재 포함된 주요 스크립트는 다음과 같다.

- `paperclip.sh`: Linux Node.js 환경에서 `paperclipai`를 실행하는 래퍼 스크립트
- `review_course_assets.sh`: 교육자료와 예제 소스를 자동 검토하는 스크립트

이 문서는 특히 `paperclip.sh`를 `systemd` 서비스로 등록해서 데몬처럼 운영하는 방법을 교육용으로 정리한 문서다.

## 1. 왜 `paperclip.sh`를 바로 실행하지 않고 `systemd`로 관리하는가

터미널에서 직접 실행하면 현재 셸이 닫히거나 WSL 세션이 내려갈 때 함께 종료된다. 반면 `systemd`로 등록하면 다음 장점이 있다.

- 시작, 중지, 재시작 명령이 표준화된다.
- 실패 시 자동 재시작 정책을 줄 수 있다.
- `journalctl`로 로그를 일관되게 확인할 수 있다.
- WSL 배포판이 다시 시작될 때 자동으로 재기동되게 설정할 수 있다.

단, WSL 자체가 종료되면 Paperclip도 같이 종료된다. 이 문서의 목적은 WSL이 살아 있는 동안 Paperclip를 안정적으로 서비스처럼 다루는 것이다.

## 2. 전제 조건

다음 조건이 먼저 갖춰져 있어야 한다.

1. WSL에서 `systemd`가 활성화되어 있어야 한다.
2. `nvm`이 설치되어 있어야 한다.
3. `paperclip.sh`가 현재 저장소에서 정상 실행되어야 한다.
4. Paperclip 초기화가 완료되어 `.paperclip/config.json`과 `.paperclip-data`가 생성되어 있어야 한다.

현재 저장소 기준 기본 경로는 다음과 같다.

- 작업 루트: `/home/aa/kuBig2026`
- 실행 스크립트: `/home/aa/kuBig2026/tools/paperclip.sh`
- 설정 파일: `/home/aa/kuBig2026/.paperclip/config.json`
- 데이터 디렉터리: `/home/aa/kuBig2026/.paperclip-data`
- `nvm` 경로: `/home/aa/.nvm`

## 3. `systemd`가 활성화되어 있는지 확인

아래 명령을 실행한다.

```bash
ps -p 1 -o comm=
```

출력이 `systemd`이면 준비된 상태다.

만약 `systemd`가 아니면 `/etc/wsl.conf`에 아래 내용을 넣고, Windows에서 `wsl --shutdown`을 실행한 뒤 WSL을 다시 시작해야 한다.

```ini
[boot]
systemd=true
```

## 4. 서비스 파일 만들기

서비스 파일은 아래 경로에 둔다.

```bash
sudo nano /etc/systemd/system/paperclip.service
```

내용은 다음 예시를 사용한다.

```ini
[Unit]
Description=Paperclip local server for kuBig2026
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=aa
Group=aa
WorkingDirectory=/home/aa/kuBig2026
Environment=HOME=/home/aa
Environment=NVM_DIR=/home/aa/.nvm
ExecStart=/home/aa/kuBig2026/tools/paperclip.sh run --config /home/aa/kuBig2026/.paperclip/config.json --data-dir /home/aa/kuBig2026/.paperclip-data
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 항목 설명

- `User`, `Group`: Paperclip를 실행할 리눅스 사용자
- `WorkingDirectory`: 저장소 루트
- `Environment`: `paperclip.sh`가 `nvm`을 찾을 수 있도록 필요한 환경 변수
- `ExecStart`: 실제 실행 명령
- `Restart=on-failure`: 비정상 종료 시 재시작

## 5. 서비스 등록 및 즉시 실행

서비스 파일을 저장한 뒤 아래 순서로 실행한다.

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now paperclip
sudo systemctl status paperclip
```

정상이라면 `active (running)` 상태가 보인다.

## 6. 자주 쓰는 운영 명령

### 시작

```bash
sudo systemctl start paperclip
```

### 중지

```bash
sudo systemctl stop paperclip
```

### 재시작

```bash
sudo systemctl restart paperclip
```

### 상태 확인

```bash
sudo systemctl status paperclip
```

### 부팅 자동 시작 해제

```bash
sudo systemctl disable paperclip
```

## 7. 로그 확인 방법

실행 로그는 아래 명령으로 확인한다.

```bash
journalctl -u paperclip -f
```

최근 로그만 짧게 보려면 다음을 사용한다.

```bash
journalctl -u paperclip -n 50 --no-pager
```

## 8. 실제로 서버가 살아 있는지 확인하는 방법

서비스 상태만 보는 것보다 health endpoint까지 확인하는 편이 정확하다.

```bash
curl -fsS http://127.0.0.1:3100/api/health
```

정상이라면 JSON 응답이 나온다.

프로세스와 응답을 같이 확인하려면 아래처럼 쓸 수 있다.

```bash
if systemctl is-active --quiet paperclip && curl -fsS http://127.0.0.1:3100/api/health >/dev/null 2>&1; then
    echo "Paperclip is running"
else
    echo "Paperclip is not healthy"
fi
```

## 9. WSL 환경에서 꼭 알아야 할 점

### WSL이 종료되면 Paperclip도 종료된다

`systemd` 서비스로 등록해도 WSL 배포판 자체가 내려가면 리눅스 프로세스도 모두 종료된다. 이것은 정상 동작이다.

### 다음에 WSL을 다시 켜면 어떻게 되는가

`enable` 상태라면 WSL이 다시 올라오면서 `paperclip` 서비스도 자동 시작된다.

즉, 아래처럼 이해하면 된다.

- WSL 실행 중: `systemd`가 Paperclip를 관리
- WSL 종료: Paperclip 종료
- WSL 재시작: `systemd`가 Paperclip 자동 재시작

### 상태 데이터는 유지된다

프로세스는 종료되지만 아래 데이터는 남는다.

- `.paperclip/config.json`
- `.paperclip-data/instances/default/db`
- `.paperclip-data/instances/default/logs`

따라서 다음 실행 때 이전 상태를 그대로 이어서 쓸 수 있다.

## 10. 장애가 날 때 점검 순서

### 1단계: 서비스 상태 확인

```bash
sudo systemctl status paperclip
```

### 2단계: 상세 로그 확인

```bash
journalctl -u paperclip -n 100 --no-pager
```

### 3단계: 포트 점유 확인

```bash
ss -lntp | grep 3100
```

### 4단계: 설정 파일 존재 여부 확인

```bash
ls -la /home/aa/kuBig2026/.paperclip
ls -la /home/aa/kuBig2026/.paperclip-data
```

### 5단계: `nvm` 경로 확인

```bash
ls -la /home/aa/.nvm/nvm.sh
```

## 11. 교육용 정리

이 구성을 통해 학습자가 익힐 수 있는 것은 단순히 Paperclip 사용법만이 아니다. 다음 운영 개념까지 함께 익히게 된다.

- 사용자 셸 실행과 서비스 실행의 차이
- `systemd` 서비스 파일 구조
- 환경 변수와 실행 경로 관리
- 로그 기반 점검 방법
- WSL의 수명 주기와 리눅스 데몬의 관계

즉, 이 문서는 Paperclip 운영 문서이면서 동시에 리눅스 서비스 운영의 입문 예제로도 사용할 수 있다.
