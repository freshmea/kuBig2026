# GPT Image Slide Prompts

Source document: `doc/01_수업자료_웹뷰_단계별_실습.md`

Output target: `doc/ppt/gpt_image_slides/slide_01.png` ~ `slide_20.png`

Shared visual reference for all slides:

- 16:9 Korean lecture slide, modern educational infographic
- Consistent design system: dark navy header band, clean off-white background, Python blue/yellow accents, pywebview green accent
- Clear conceptual diagrams, simple metaphors, high polish
- No photo realism unless metaphor requires it
- Use large readable Korean headings and minimal body text
- Avoid clutter, watermarks, random logos, fake UI brand marks

## 01. Title

Create a polished Korean lecture slide, 16:9. Title text exactly: "PyWebView 탁상 시계". Subtitle: "Python 백엔드와 WebView 프론트엔드 분리". Visual: Python engine block connected to a small local server cube and a desktop webview window, all in one clean architecture scene. Add small labels: "Python", "localhost", "WebView". Modern educational style, navy header, light background, Python blue/yellow accents, no watermark.

## 02. Learning Goals

Create a 16:9 Korean lecture slide. Title exactly: "수업 목표". Four large goal cards with short Korean labels: "WebView 이해", "문제 발견", "역할 분리", "DOM 부분 갱신". Visual metaphor: a student climbing four steps toward a desktop app window. Clean infographic style, same navy/blue/yellow palette.

## 03. Big Metaphor

Create a 16:9 Korean lecture slide. Title: "비유: 쇼윈도와 작업실". Visual: left side a beautiful shop window labeled "WebView 화면", right side an organized workshop labeled "Python 백엔드", between them a small delivery box labeled "JSON". Include minimal Korean note: "보여주기" near window, "계산과 상태" near workshop. Consistent lecture style.

## 04. Teaching Loop

Create a 16:9 Korean lecture slide. Title: "반복형 수업 진행". Show a circular loop diagram with four stages: "단순 데모", "문제 발견", "구조 개선", "확장". Use arrows around the loop. Add small metaphor of a rough sketch becoming a clean blueprint. Consistent colors.

## 05. Step A Simple Demo

Create a 16:9 Korean lecture slide. Title: "단계 A: 가장 단순한 데모". Visual: one Python file opening a tiny desktop window that says "Hello". Include a small code-like card with short text: `create_window(html="<h1>Hello</h1>")`. Emphasize quick success, simple and friendly.

## 06. Problem: Mixed Code

Create a 16:9 Korean lecture slide. Title: "문제: 코드가 뒤섞인다". Visual metaphor: tangled colored strings labeled "Python", "HTML", "CSS", "JS" inside one messy box. On the right, a frustrated developer looking at a long string. Include short Korean phrase: "동작하지만 유지보수 어렵다". No watermark.

## 07. Solution: File Separation

Create a 16:9 Korean lecture slide. Title: "해결: 파일을 역할별로 분리". Visual: four clean folders/cards arranged horizontally: "index.html", "style.css", "app.js", "main.py". Each has one icon: structure, paint, lightning, window. Add phrase: "역할이 보이면 구조가 보인다". Same design system.

## 08. Base Path

Create a 16:9 Korean lecture slide. Title: "기준 경로: 어디서 찾을 것인가". Visual metaphor: a map with a clear starting pin labeled "__file__", paths leading to "frontend", "index.html", "style.css". Include phrase: "실행 위치가 달라도 길을 잃지 않는다". Clean technical infographic.

## 09. Full Reload Problem

Create a 16:9 Korean lecture slide. Title: "문제: 전체 페이지를 다시 만든다". Visual split screen: left, a whole house being rebuilt just to change a wall clock; right, only clock hands moving. Labels: "전체 리로드" and "부분 갱신". Strong visual metaphor, classroom-friendly.

## 10. DOM Partial Update

Create a 16:9 Korean lecture slide. Title: "DOM 부분 갱신". Visual: web page skeleton with only two highlighted nodes: "time" and "date". Python server sends small glowing JSON packet to those nodes. Include labels: "필요한 노드만 변경", "빠르고 안정적". Modern infographic.

## 11. Final Architecture

Create a 16:9 Korean lecture slide. Title: "최종 구조". Visual architecture diagram: "timer/main.py" starts "ClockApiServer", server serves "frontend files" and "/api/clock", WebView loads localhost URL, JS fetches JSON. Use arrows and clear Korean labels. Keep it polished and readable.

## 12. Localhost Loopback

Create a 16:9 Korean lecture slide. Title: "localhost: 같은 컴퓨터 안의 복도". Visual: one computer building with two rooms, "Frontend" and "Backend", connected by an internal hallway labeled "127.0.0.1". Add tiny courier carrying JSON through hallway. Friendly metaphor.

## 13. JSON Contract

Create a 16:9 Korean lecture slide. Title: "JSON API: 작은 계약서". Visual: a clean contract document between "Python" and "JavaScript" with fields "time" and "date". Include small JSON snippet: `{ "time": "...", "date": "..." }`. Emphasize agreement/contract metaphor.

## 14. ClockApiServer Role

Create a 16:9 Korean lecture slide. Title: "ClockApiServer의 역할". Visual: backend server as a control tower with three panels: "정적 파일 제공", "현재 시간 계산", "JSON 응답". Include small route label "/api/clock". Technical but friendly.

## 15. Frontend fetch Role

Create a 16:9 Korean lecture slide. Title: "프론트엔드의 역할". Visual: JavaScript as a small messenger, asking `/api/clock`, receiving JSON, updating two display panels "time" and "date". Include phrase: "계산하지 않고 반영한다". Clean infographic.

## 16. Port 0

Create a 16:9 Korean lecture slide. Title: "포트 0: 빈 자리 자동 배정". Visual metaphor: parking lot with many numbered spaces, some occupied, OS attendant gives an empty space to the server car. Labels: "포트 충돌", "자동 할당", "127.0.0.1". Use Python blue/yellow accents.

## 17. Failure as Lesson

Create a 16:9 Korean lecture slide. Title: "실패는 문제 정의다". Visual: three warning cards: "검은 화면", "API 실패", "포트 충돌". Below them a clean path arrow to "원인 분석" and "구조 개선". Classroom tone, not scary.

## 18. Final File Roles

Create a 16:9 Korean lecture slide. Title: "최종 파일 역할". Visual: vertical file tree for `timer/` with five nodes: "main.py", "backend/server.py", "frontend/index.html", "frontend/style.css", "frontend/app.js". Each node has a short Korean role label. Clean educational diagram.

## 19. 90 Minute Flow

Create a 16:9 Korean lecture slide. Title: "90분 수업 흐름". Visual timeline from left to right with five time blocks: "0~15 단순 데모", "15~30 문제 재현", "30~55 JSON API", "55~75 구조 정리", "75~90 확장 과제". Add small icons for each block.

## 20. Summary

Create a 16:9 Korean lecture slide. Title: "핵심 정리". Visual: five connected concept stones across a bridge: "단순 시작", "문제 관찰", "역할 분리", "부분 갱신", "다음 확장". At the far end, a sign says "click counter · 상태 공유 · SSE". Consistent polished lecture style.
