# 05 사용자 설정 JSON 저장 단계별 실습

## 1. 수업 목표

- 앱 설정을 JSON 파일로 저장하고 다시 불러온다.
- 기본값, 저장값, 손상된 설정 파일 처리 방식을 이해한다.
- `localStorage`와 Python 파일 저장의 차이를 비교한다.

## 2. 최종 결과물

- 데모 폴더: `settings_store`
- 실행: `uv run settings_store/main.py`
- 저장 파일: `settings_store/data/settings.json`

최종 동작:

1. 앱 시작 시 Python이 설정 파일을 읽는다.
2. 파일이 없으면 기본 설정을 반환한다.
3. 사용자가 테마, 글자 크기, 마지막 카운터 값을 바꾼다.
4. 저장 버튼을 누르면 Python이 JSON 파일로 저장한다.
5. 앱을 다시 열면 이전 설정이 복원된다.

---

## 3. 단계별 실습

### 단계 A. 설정을 화면 상태로만 관리하기

#### A-1. 구현 아이디어

처음에는 select, range, number input의 값을 JS 변수로만 관리할 수 있다.

#### A-2. 문제점

- 앱을 닫으면 값이 사라진다.
- 여러 설정 항목을 한곳에서 관리하기 어렵다.
- Python 앱에서 설정값을 활용할 수 없다.

#### A-3. 해결

설정은 Python이 JSON 파일로 관리한다.

강의 포인트:
- 사용자 설정은 UI 상태가 아니라 앱 상태다.

---

### 단계 B. 기본 설정 정의하기

#### B-1. 구현

```python
DEFAULT_SETTINGS = {"theme": "light", "fontSize": 18, "lastCount": 0}
```

#### B-2. 설명

- 설정 항목의 기준값을 한곳에 모은다.
- 새 설정이 추가되어도 기본값을 알 수 있다.
- 수업에서는 단순 dict가 가장 이해하기 쉽다.

#### B-3. 트릭

기본 설정을 함수 내부에 흩뿌리지 않는다.
상수 하나로 모아야 나중에 항목을 추가할 때 안전하다.

---

### 단계 C. 설정 파일 읽기

#### C-1. 구현

```python
def load_settings(self) -> dict[str, str | int]:
    if not SETTINGS_PATH.exists():
        return DEFAULT_SETTINGS.copy()
    try:
        saved = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return DEFAULT_SETTINGS.copy()
    return DEFAULT_SETTINGS | saved
```

#### C-2. 문제점과 해결

- 파일 없음: 기본값 반환
- JSON 깨짐: 기본값 반환
- 예전 설정 파일에 새 항목 없음: `DEFAULT_SETTINGS | saved`로 병합

#### C-3. Python 3.13 포인트

`dict | dict` 병합 문법을 사용한다.
왼쪽 기본값 위에 오른쪽 저장값을 덮어쓴다.

강의 포인트:
- 설정 파일은 사용자가 지우거나 망가뜨릴 수 있으므로 방어적으로 읽는다.

---

### 단계 D. 설정 파일 저장

#### D-1. 구현

```python
def save_settings(self, settings: dict[str, str | int]) -> dict[str, str]:
    next_settings = DEFAULT_SETTINGS | settings
    SETTINGS_PATH.write_text(
        json.dumps(next_settings, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return {"status": "saved", "path": str(SETTINGS_PATH)}
```

#### D-2. 설명

- `ensure_ascii=False`는 한글을 그대로 저장한다.
- `indent=2`는 사람이 읽기 좋게 저장한다.
- 저장 전에 기본값과 병합해 누락 항목을 보완한다.

---

### 단계 E. localStorage와 비교

#### E-1. localStorage 장점

- JS만으로 간단히 저장 가능
- 브라우저 UI 상태 저장에 편리

#### E-2. Python 파일 저장 장점

- Python 코드가 설정을 직접 사용할 수 있다.
- 파일 위치와 내용을 수업자가 확인하기 쉽다.
- 패키징/백업/마이그레이션 설명으로 이어가기 좋다.

강의 포인트:
- Python 심화 수업에서는 설정 저장도 Python 책임으로 두는 편이 학습 목표에 맞다.

---

## 4. 체크리스트

- [ ] 설정 파일이 없을 때 기본값으로 실행된다.
- [ ] 저장 후 `settings.json`이 생긴다.
- [ ] 앱 재실행 후 설정이 복원된다.
- [ ] JSON이 한글을 깨뜨리지 않는다.

## 5. 확장 과제

- 마지막 창 크기 저장
- 최근 파일 경로 저장
- 설정 초기화 버튼 추가
