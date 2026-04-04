# Paperclip 모델 변경 회고

작성일: 2026-04-04

## 결론

이번 작업에서 재현 가능하게 확인된 사실은 다음 하나다.

- Paperclip의 실제 모델 소스 오브 트루스는 라이브 서버와 그 뒤의 내장 PostgreSQL 데이터다.
- 온보딩 드롭다운 UI를 직접 패치하는 방식은 이 환경에서 안정적으로 마무리되지 않았다.
- 실제 런타임 모델을 바꾸는 가장 확실한 방법은 라이브 데이터 소스에서 `adapterConfig.model` 값을 직접 변경하는 것이다.

즉, 이번 건은 프런트엔드 드롭다운 수정 작업으로 끝낼 문제가 아니었고, 운영 관점에서는 DB 또는 라이브 API 기준으로 처리하는 것이 맞다.

## 환경 요약

- Paperclip 서버 주소: `http://127.0.0.1:3100`
- 설정 파일: `/home/aa/kuBig2026/.paperclip/config.json`
- 실행 방식: `systemd` 서비스에서 `/home/aa/kuBig2026/tools/paperclip.sh run --config /home/aa/kuBig2026/.paperclip/config.json --data-dir /home/aa/kuBig2026/.paperclip-data`
- DB 모드: `embedded-postgres`
- 내장 PostgreSQL 데이터 디렉터리: `/home/aa/kuBig2026/.paperclip-data/instances/default/db`
- 내장 PostgreSQL 포트: `54329`

## 이번에 실패한 시도

### 1. 저장소 안의 정적 파일만 고치면 반영될 것이라는 가정

초기에는 저장소 안의 문서나 설정 파일이 실제 서비스 동작을 좌우한다고 볼 수 있었지만, 이번 건의 실제 소스 오브 트루스는 실행 중인 Paperclip 서버와 그 데이터였다. 저장소 안의 과거 파일, 백업, 참고 문서는 현재 서빙 중인 온보딩 UI와 직접 연결되지 않았다.

정리:

- 저장소 파일 수정만으로는 라이브 모델 목록이 바뀌지 않았다.
- 라이브 서버 기준 검증이 필요했다.

### 2. 온보딩 기본값만 바꾸는 방식

Codex 기본 상수를 `gpt-5.1-codex-mini`로 바꾸는 작업은 일부 화면 표시에는 영향을 줄 수 있었지만, 드롭다운 항목 자체를 추가하지는 못했다.

원인:

- 드롭다운 항목은 프런트엔드 하드코딩 기본값이 아니라 라이브로 받아오는 `adapterModels` 데이터에 의해 만들어졌다.
- 따라서 기본 문자열만 바꾸면 선택된 값처럼 보일 수는 있어도 실제 메뉴 항목에는 나타나지 않는다.

### 3. 설치된 UI 번들 직접 패치

실제 서빙되는 설치 경로의 `ui-dist` 번들을 찾아서 minified JS를 직접 수정하는 작업도 시도했다.

문제점:

- 파일이 사실상 한 줄짜리 minified 번들이어서 구조적 패치가 매우 취약했다.
- 일부 문자열 치환은 성공한 것처럼 보여도, 서버가 다른 hashed asset을 서빙하거나 브라우저 캐시와 어긋날 수 있었다.
- 화면에 `gpt-5.1-codex-mini`가 표시되는 것과 드롭다운 옵션으로 존재하는 것은 다른 문제였다.
- 최종적으로 사용자 눈으로 확인했을 때 드롭다운에는 여전히 원하는 항목이 나타나지 않았다.

정리:

- 설치된 번들 패치는 유지보수성과 재현성이 낮다.
- Paperclip 프런트엔드 소스 트리와 빌드 파이프라인을 통제하지 않는 이상 운영 방법으로 채택하면 안 된다.

### 4. 페이지 텍스트 확인만으로 성공 판정

한 시점에서는 라이브 페이지에 `Command Model`과 `gpt-5.1-codex-mini`가 보였기 때문에 성공처럼 보였다. 하지만 이것은 실제 드롭다운 옵션 존재를 증명하지 못했다.

정리:

- 필드 값 표시 확인과 드롭다운 옵션 존재 확인은 분리해서 검증해야 한다.
- 이번 건에서 최종 실패 판정은 사용자가 실제 드롭다운에서 항목이 없다고 확인한 것으로 확정됐다.

## 최종 운영 판단

이 환경에서는 다음 원칙으로 처리하는 것이 맞다.

1. 모델 변경은 UI 패치가 아니라 라이브 데이터 변경으로 처리한다.
2. 온보딩 드롭다운이 라이브 모델 목록을 그대로 쓰는 구조라면, UI만 손봐서는 문제를 끝내기 어렵다.
3. 운영자가 확실하게 제어할 수 있는 것은 실행 중인 Paperclip 서버의 데이터와 런타임 설정이다.

## 권장 모델 변경 방법

### 원칙

목표는 특정 Codex 에이전트의 `adapterConfig.model` 값을 원하는 모델로 바꾸는 것이다. 이번 작업 기준으로 대상 모델은 아래 값이다.

- `gpt-5.1-codex-mini`

### 변경 순서

#### 1. 현재 서비스와 데이터 위치 확인

- Paperclip 서버는 `http://127.0.0.1:3100`에서 동작한다.
- 내장 PostgreSQL 데이터는 `/home/aa/kuBig2026/.paperclip-data/instances/default/db`에 있다.
- 서비스 재시작 명령은 `sudo systemctl restart paperclip`이다.

#### 2. 대상 에이전트 식별

라이브 기준에서 어떤 에이전트의 모델을 바꿀지 먼저 확인한다.

확인 포인트:

- `adapterType`이 `codex_local`인지
- 현재 `adapterConfig.model`이 무엇인지
- 변경 대상 에이전트 ID가 무엇인지

운영상 가장 안전한 확인 기준은 라이브 API 응답이다. 예를 들어 Paperclip가 이미 부여한 인증 컨텍스트가 있다면 `/api/agents/me` 같은 엔드포인트에서 현재 에이전트의 `adapterConfig.model`을 확인할 수 있다.

#### 3. DB 백업 또는 유지보수 창 확보

직접 DB 값을 수정할 때는 최소한 다음 중 하나는 먼저 수행한다.

- Paperclip가 만든 백업 디렉터리 상태 확인
- 수동 백업 수행
- 짧은 유지보수 시간 확보 후 작업

이번 환경에서 설정상 백업 디렉터리는 다음 경로다.

- `/home/aa/kuBig2026/.paperclip-data/instances/default/data/backups`

#### 4. 내장 PostgreSQL에 접속

현재 설정은 `embedded-postgres`이며 데이터 디렉터리와 포트는 확인되었다. 다만 DB 인증 정보와 실제 테이블 스키마는 Paperclip 버전에 따라 달라질 수 있으므로, 접속 후 먼저 스키마를 확인해야 한다.

확인해야 할 것:

- 에이전트 레코드가 저장된 테이블 이름
- `adapter_config` 또는 그에 준하는 JSON/JSONB 컬럼 이름
- `adapter_type` 또는 그에 준하는 구분 컬럼 이름

#### 5. `adapterConfig.model` 값을 직접 변경

실제 테이블과 컬럼 이름이 확인되면, Codex 에이전트 레코드에서 모델 값만 바꾼다.

아래는 개념 예시다.

```sql
update agents
set adapter_config = jsonb_set(adapter_config::jsonb, '{model}', '"gpt-5.1-codex-mini"', true)
where id = '<target-agent-id>'
  and adapter_type = 'codex_local';
```

주의:

- 위 SQL은 컬럼명이 `adapter_config`, `adapter_type`일 때의 예시다.
- 실제 Paperclip 버전의 스키마가 다르면 테이블명과 컬럼명부터 맞춰야 한다.
- 컬럼 타입이 이미 `jsonb`이면 캐스팅은 필요 없을 수 있다.

#### 6. 서비스 재시작

DB 수정 후에는 Paperclip 프로세스가 변경된 값을 다시 읽도록 서비스를 재시작한다.

```bash
sudo systemctl restart paperclip
```

#### 7. 라이브 검증

검증은 반드시 라이브 기준으로 한다.

검증 항목:

- 현재 에이전트 조회에서 `adapterConfig.model`이 바뀌었는지
- 실제 작업 실행 시 해당 모델이 쓰이는지
- 온보딩 화면이 여전히 다른 목록을 보여도, 런타임 에이전트 값 자체는 바뀌었는지

중요:

- 이번 작업의 핵심 목표는 드롭다운 미관이 아니라 실제 모델 변경이다.
- UI 드롭다운이 값을 반영하지 못하더라도, 런타임 에이전트 데이터가 바뀌면 운영 목적은 달성된다.

## 이후 동일 이슈 대응 원칙

다음부터는 아래 순서로만 판단한다.

1. 먼저 라이브 API나 DB에서 현재 `adapterConfig.model`을 확인한다.
2. UI에 안 보인다는 이유만으로 프런트엔드 번들부터 패치하지 않는다.
3. 설치된 minified bundle 직접 수정은 최후의 실험용 수단으로만 취급한다.
4. 운영 변경은 라이브 데이터 변경과 재시작, 라이브 검증으로 끝낸다.

## 최종 메모

이번 작업에서 문서화 가능한 결론은 명확하다.

- 온보딩 드롭다운 커스텀 항목 추가 시도는 실패했다.
- 라이브 Paperclip 서버의 내장 PostgreSQL 데이터가 실제 모델 변경의 기준점이다.
- 다음 작업자는 프런트엔드 번들 수정부터 시작하지 말고, 에이전트 레코드의 `adapterConfig.model`부터 직접 확인하고 변경해야 한다.