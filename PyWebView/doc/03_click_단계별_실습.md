# Click Counter 단계별 수업 자료

## 1. 수업 목표

- 버튼 클릭으로 값이 증가/감소하는 작은 데스크톱 앱을 만든다.
- JavaScript가 직접 상태를 계산하는 방식과 Python 서버가 상태를 관리하는 방식의 차이를 이해한다.
- 같은 앱을 여러 개 실행했을 때 상태가 분리되는 문제를 발견하고 해결한다.
- 폴링과 서버 이벤트(SSE)의 차이를 비교하고, 변경이 있을 때만 화면을 즉시 동기화하는 구조를 구현한다.

## 2. 대상 및 사전 준비

- 대상: Python 기초 문법, HTML/CSS/JavaScript 기초, fetch API를 간단히 배운 학습자
- 준비:
  - Python 3.9+
  - uv
  - 프로젝트 폴더: PyWebView
  - 이전 실습: `timer` 예제의 로컬 서버 + 프론트엔드 분리 구조

## 3. 최종 결과물(현재 코드 기준)

- 백엔드: `click/backend/server.py`
  - 정적 파일 제공
  - 카운터 값을 Python 변수로 관리
  - `GET /api/counter`로 현재 값 반환
  - `POST /api/counter/increase`로 값 증가
  - `POST /api/counter/decrease`로 값 감소
  - `GET /api/counter/events`로 변경 이벤트 전송
  - 고정 포트 `49321`을 사용해 서버 중복 실행 방지
- 프론트엔드:
  - `click/frontend/index.html`
  - `click/frontend/style.css`
  - `click/frontend/app.js`
  - 버튼 클릭 시 서버 API 호출
  - `EventSource`로 서버 이벤트를 받아 화면 즉시 갱신
- 앱 부팅: `click/main.py`
  - 서버 시작
  - PyWebView 창 생성
  - 이미 서버가 실행 중이면 기존 서버 사용

---

## 4. 수업 진행 시나리오

이번 수업은 같은 기능을 여러 번 고치며 진행한다.

1. JavaScript만으로 클릭 카운터 만들기
2. 상태 계산을 Python 서버로 이동하기
3. 앱을 두 개 실행했을 때 값이 분리되는 문제 확인
4. 서버를 하나만 실행하도록 수정하기
5. 한 창의 변경이 다른 창 화면에 바로 반영되지 않는 문제 확인
6. 폴링으로 해결해 보기
7. SSE로 변경 시점에만 즉시 동기화하기

핵심은 처음부터 정답 구조를 외우는 것이 아니라, 문제가 생기는 이유를 보고 구조를 개선하는 것이다.

---

## 5. 단계별 실습

### 단계 A. JavaScript만으로 클릭 카운터 만들기

#### A-1. 구현

HTML에 숫자를 보여줄 영역과 버튼 두 개를 만든다.

```html
<div id="count">0</div>
<button id="decrease" type="button">-</button>
<button id="increase" type="button">+</button>
```

JavaScript에서 변수를 만들고 버튼 클릭 때 값을 바꾼다.

```js
let count = 0;

increaseButton.addEventListener('click', () => {
    count += 1;
    countEl.textContent = count;
});
```

#### A-2. 문제점 지적

- 값이 브라우저 창 내부 JavaScript 변수에만 존재한다.
- 같은 앱을 두 개 실행하면 각 창이 서로 다른 `count`를 가진다.
- Python 백엔드가 상태를 알 수 없으므로 저장, 공유, 검증 같은 기능을 붙이기 어렵다.

#### A-3. 해결 방향

- 카운터 값을 Python 서버가 관리하게 한다.
- 프론트엔드는 "버튼이 눌렸다"는 요청만 보내고, 계산 결과는 서버에서 받는다.

강의 포인트:
- UI가 상태를 직접 소유하면 간단하지만, 여러 창/여러 사용자/저장 기능으로 확장하기 어렵다.

---

### 단계 B. Python 서버에서 카운터 계산하기

#### B-1. 구현

서버에 카운터 변수와 API를 만든다.

```text
GET  /api/counter
POST /api/counter/increase
POST /api/counter/decrease
```

응답 예시:

```json
{
  "count": 1
}
```

프론트엔드는 클릭 때 `fetch()`로 서버에 요청한다.

```js
increaseButton.addEventListener('click', () => {
    requestCounter('/api/counter/increase', { method: 'POST' });
});
```

#### B-2. 문제점 지적

- 이제 계산은 서버가 하지만, 서버가 앱 실행마다 새로 뜨면 여전히 값이 분리된다.
- `timer` 예제처럼 빈 포트를 자동 할당하면 창마다 다른 서버가 만들어질 수 있다.

#### B-3. 해결 방향

- 클릭 카운터처럼 창 사이에 상태를 공유해야 하는 앱은 하나의 서버를 기준으로 삼아야 한다.

강의 포인트:
- 자동 포트 할당은 충돌을 피하는 데 좋지만, 여러 창이 같은 상태를 공유해야 할 때는 적합하지 않을 수 있다.

---

### 단계 C. 서버 중복 실행 막기

#### C-1. 구현

고정 포트를 정한다.

```python
COUNTER_PORT = 49321
```

서버 시작 전에 기존 서버가 있는지 확인한다.

```python
def _existing_server_is_ready(self) -> bool:
    try:
        with request.urlopen(f"{self.base_url}/api/counter", timeout=1) as response:
            return response.status == HTTPStatus.OK
    except (OSError, error.URLError):
        return False
```

이미 서버가 있으면 새 서버를 띄우지 않고 같은 URL을 사용한다.

#### C-2. 문제점 지적

- 두 창이 같은 서버를 쓰게 되어 값은 공유된다.
- 하지만 한쪽 창에서 버튼을 눌러도 다른 창의 화면은 자동으로 바뀌지 않는다.
- 서버 값과 화면 값이 잠시 다를 수 있다.

#### C-3. 해결 방향

- 다른 창도 서버의 변경을 알 수 있어야 한다.

강의 포인트:
- "데이터가 공유된다"와 "화면이 동기화된다"는 다른 문제다.

---

### 단계 D. 폴링으로 화면 동기화하기

#### D-1. 구현

각 창이 일정 시간마다 서버 값을 다시 읽는다.

```js
setInterval(() => {
    requestCounter('/api/counter');
}, 500);
```

#### D-2. 장점

- 구현이 쉽다.
- 서버가 단순하다.
- 많은 입문 수업에서 설명하기 좋다.

#### D-3. 문제점

- 값이 바뀌지 않아도 계속 요청한다.
- 0.5초마다 확인하면 최대 0.5초 늦게 반영된다.
- 간격을 줄이면 서버 요청이 많아진다.

#### D-4. 해결 방향

- 서버가 값이 바뀌는 순간 클라이언트에 신호를 보내게 한다.

강의 포인트:
- 폴링은 "클라이언트가 계속 물어보는 방식"이다.
- 실시간성은 간격에 의존한다.

---

### 단계 E. SSE로 변경 시점에 즉시 동기화하기

#### E-1. 구현

서버에 이벤트 스트림 API를 만든다.

```text
GET /api/counter/events
```

응답 형식은 `text/event-stream`이다.

```text
data: {"count": 1}

```

프론트엔드는 `EventSource`를 사용한다.

```js
const counterEvents = new EventSource('/api/counter/events');

counterEvents.addEventListener('message', (event) => {
    const payload = JSON.parse(event.data);
    renderCount(payload.count);
});
```

서버는 값이 바뀔 때 연결된 모든 창에 새 값을 보낸다.

```python
def _broadcast_counter(self, payload: dict[str, int]) -> None:
    for client_queue in list(self._event_clients):
        client_queue.put(payload)
```

#### E-2. 장점

- 값이 바뀔 때만 이벤트를 보낸다.
- 다른 창이 거의 즉시 갱신된다.
- WebSocket보다 단순하다.
- 서버에서 클라이언트로 보내는 단방향 알림에 적합하다.

#### E-3. 한계

- 클라이언트에서 서버로 보내는 요청은 여전히 `fetch()`를 사용한다.
- 양방향 실시간 채팅처럼 양쪽이 계속 메시지를 주고받는 구조라면 WebSocket이 더 적합하다.

강의 포인트:
- 클릭 카운터는 "클라이언트 요청은 fetch, 서버 알림은 SSE" 조합으로 충분하다.

---

## 6. 최종 구조

```text
PyWebView/
  click/
    backend/
      __init__.py
      server.py
    frontend/
      index.html
      style.css
      app.js
    __init__.py
    main.py
```

## 7. 각 파일 역할

- `click/main.py`
  - `CounterApiServer` 생성
  - 서버 시작
  - PyWebView 창 생성
  - 종료 시 자신이 띄운 서버만 정리
- `click/backend/server.py`
  - 정적 파일 제공
  - 카운터 값 관리
  - JSON API 제공
  - SSE 이벤트 스트림 제공
  - 서버 중복 실행 방지
- `click/frontend/index.html`
  - 숫자 표시 영역
  - 증가/감소 버튼
- `click/frontend/style.css`
  - 데모 화면 스타일
- `click/frontend/app.js`
  - 버튼 클릭 시 POST 요청
  - `EventSource`로 서버 변경 이벤트 수신
  - 받은 `count` 값을 DOM에 반영

---

## 8. 실습 순서(권장 100분)

1. 0~15분: JavaScript 로컬 상태 카운터 구현
2. 15~30분: Python 서버 API로 상태 이동
3. 30~45분: 앱 두 개 실행 후 값 분리 문제 확인
4. 45~60분: 고정 포트와 기존 서버 감지로 단일 서버 구조 만들기
5. 60~70분: 화면 동기화 문제 확인
6. 70~80분: 폴링 방식으로 임시 해결
7. 80~95분: SSE 방식으로 변경 시점 동기화 구현
8. 95~100분: 구조 정리 및 질문

---

## 9. 체크리스트

- [ ] `uv run click/main.py`로 앱이 실행된다.
- [ ] `+` 버튼을 누르면 값이 증가한다.
- [ ] `-` 버튼을 누르면 값이 감소한다.
- [ ] JavaScript가 직접 `count += 1`을 하지 않는다.
- [ ] Python 서버가 카운터 값을 관리한다.
- [ ] 앱을 두 개 실행해도 같은 서버를 사용한다.
- [ ] 한쪽 창에서 값을 바꾸면 다른 창도 자동으로 갱신된다.
- [ ] 폴링 없이 SSE 이벤트로 동기화된다.

---

## 10. 실습 중 자주 나오는 질문 정리

### Q1. 왜 JavaScript에서 바로 계산하면 안 되나?

안 되는 것은 아니다. 가장 단순한 데모에는 좋은 방식이다.
하지만 여러 창이 같은 값을 공유하거나, 서버에서 검증/저장/로그를 남겨야 한다면 상태를 서버가 관리하는 편이 낫다.

### Q2. 왜 POST를 쓰나?

`increase`와 `decrease`는 서버의 상태를 변경한다.
HTTP 관점에서 상태 변경 요청은 `GET`보다 `POST`가 더 적합하다.

### Q3. 고정 포트는 항상 좋은가?

아니다.
`timer`처럼 창마다 독립적으로 동작해도 되는 앱은 빈 포트 자동 할당이 편하다.
하지만 `click`처럼 여러 창이 같은 상태를 공유해야 하는 앱은 같은 서버를 찾을 기준이 필요하므로 고정 포트가 단순한 선택이다.

### Q4. 폴링과 SSE 중 무엇을 써야 하나?

- 폴링: 쉽고 단순하지만 계속 물어본다.
- SSE: 서버가 변경 시점에 알려준다. 단방향 실시간 알림에 적합하다.
- WebSocket: 양방향 실시간 통신이 필요할 때 적합하다.

### Q5. 창을 닫으면 서버는 어떻게 되나?

현재 구조에서는 처음 서버를 띄운 앱이 종료될 때 서버도 종료된다.
모든 창과 독립적으로 서버를 계속 유지하려면 서버를 별도 백그라운드 프로세스로 분리하는 추가 설계가 필요하다.

---

## 11. 실행 방법

```powershell
uv venv
uv sync
uv run click/main.py
```

두 창 동기화를 확인하려면 같은 명령을 터미널 두 개에서 실행한다.

문법 점검:

```powershell
uv run python -m compileall click
```

---

## 12. 확장 과제

### 과제 1. 초기화 버튼 추가

- `POST /api/counter/reset` 추가
- 프론트에 reset 버튼 추가
- 모든 창에 reset 결과가 즉시 반영되는지 확인

### 과제 2. 최소값 제한

- 카운터가 0보다 작아지지 않게 서버에서 막기
- 프론트가 아니라 서버에서 막아야 하는 이유 설명

### 과제 3. 이벤트 로그 표시

- 서버가 증가/감소 시각을 함께 전송
- 프론트에서 최근 변경 로그 5개 표시

### 과제 4. 서버 독립 실행

- PyWebView 창과 서버 프로세스를 분리
- 첫 번째 창이 닫혀도 다른 창의 동기화가 유지되도록 설계

---

## 13. 강사용 운영 메모

- 먼저 JavaScript 로컬 상태 버전을 일부러 만들게 한다.
- 두 창을 띄워 값이 따로 움직이는 장면을 보여준다.
- "서버 값 공유"를 해결한 뒤에도 "화면 동기화" 문제가 남는다는 점을 강조한다.
- 폴링을 먼저 보여주면 SSE가 왜 필요한지 학생이 더 쉽게 이해한다.
- SSE는 WebSocket보다 단순하므로, 입문 수업에서는 실시간 알림의 첫 예제로 적합하다.

이 수업의 핵심은 클릭 카운터 자체가 아니라,
"상태는 어디에 있어야 하는가"와 "변경 사실을 화면에 어떻게 전달할 것인가"를 구분해서 이해하는 것이다.
