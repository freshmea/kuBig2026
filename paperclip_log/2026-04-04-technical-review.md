# 기술 검토 보고서

작성일: 2026-04-04

## 목적

기술 검토자로서 `kuBig2026` 저장소를 최신 상태로 유지하고, 빌드/스크립트/문서 관련 결함을 발견 및 수정하여 다음 운영 담당자가 즉시 사용할 수 있도록 준비한다.

## 주요 발견 및 조치

1. Paperclip UI 패치 스크립트가 해시 네임이 붙은 번들을 하드코딩한 경로로 수정하기 때문에 Paperclip 패키지를 재설치할 때마다 경로를 다시 찾아야 했고, 유지보수가 어렵다. `tools/patch_paperclip_dropdown.js`를 고쳐서 `@paperclipai/server/ui-dist/assets` 디렉터리에서 `index-*.js` 파일을 자동 선택하도록 했고, 패치 결과도 로그에 남기도록 했다.
2. `network/mqttPub` CMake 타깃은 `paho-mqtt3c` 라이브러리가 없으면 링커가 `NOTFOUND`를 집어넣어 엉뚱한 에러를 낸다. CMake 구성단에서 라이브러리 누락을 감지하여 명시적으로 중단하고, 네트워크 README에 `libpaho-mqtt3c-dev` 설치 안내를 넣어 의존성을 문서화해서 다음 운영자가 빌드 실패 상황에서 빠르게 복구할 수 있게 했다.

## 다음 행동 항목

- 환경에 `cmake`, `gcc`, `libpaho-mqtt3c-dev`가 갖춰졌을 때 `tools/review_course_assets.sh`를 다시 실행하여 빌드/문서 검증이 통과하는지 확인하고, 문제가 있으면 추가로 보고한다.
- 개선 사항이 현장 운영자에게 전달되었는지 Paperclip 이슈에 요약 코멘트를 남기되, 요청이 있을 경우 `paperclipai` CLI를 통해 동일 내용을 업데이트한다.
