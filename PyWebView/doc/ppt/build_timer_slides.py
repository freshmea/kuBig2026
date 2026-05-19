from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path(__file__).resolve().parent
ASSET_DIR = OUT_DIR / "assets"
SLIDE_DIR = OUT_DIR / "timer_webview_slides"
W, H = 1920, 1080

FONT = Path("C:/Windows/Fonts/malgun.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/malgunbd.ttf")

NAVY = "#162238"
BLUE = "#2f6fab"
YELLOW = "#ffd343"
GREEN = "#36b37e"
RED = "#e15241"
PURPLE = "#6d5bd0"
INK = "#1f2937"
MUTED = "#64748b"
PAPER = "#f8fafc"
LINE = "#d7dee9"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT), size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def rounded(draw: ImageDraw.ImageDraw, xy, fill, outline=None, radius=28, width=3):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, start, end, fill=BLUE, width=8):
    draw.line([start, end], fill=fill, width=width)
    x1, y1 = start
    x2, y2 = end
    if abs(x2 - x1) >= abs(y2 - y1):
        direction = 1 if x2 > x1 else -1
        pts = [(x2, y2), (x2 - direction * 28, y2 - 16), (x2 - direction * 28, y2 + 16)]
    else:
        direction = 1 if y2 > y1 else -1
        pts = [(x2, y2), (x2 - 16, y2 - direction * 28), (x2 + 16, y2 - direction * 28)]
    draw.polygon(pts, fill=fill)


def load_asset(name: str, max_size: tuple[int, int]) -> Image.Image | None:
    path = ASSET_DIR / name
    if not path.exists():
        return None
    img = Image.open(path).convert("RGBA")
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    return img


def paste_center(base: Image.Image, img: Image.Image, box: tuple[int, int, int, int], alpha=255):
    x1, y1, x2, y2 = box
    layer = img.copy()
    if alpha < 255:
        layer.putalpha(alpha)
    x = x1 + ((x2 - x1) - layer.width) // 2
    y = y1 + ((y2 - y1) - layer.height) // 2
    base.alpha_composite(layer, (x, y))


def draw_wrapped(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], fnt, fill=INK, width_chars=30, line_gap=12):
    x, y = xy
    for paragraph in text.split("\n"):
        lines = wrap(paragraph, width=width_chars) or [""]
        for line in lines:
            draw.text((x, y), line, font=fnt, fill=fill)
            y += fnt.size + line_gap
        y += line_gap
    return y


def make_base(num: int, title: str, subtitle: str = "") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGBA", (W, H), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, H), fill=PAPER)
    draw.rectangle((0, 0, W, 112), fill=NAVY)
    draw.text((78, 30), title, font=font(42, True), fill="#ffffff")
    if subtitle:
        draw.text((80, 122), subtitle, font=font(26), fill=MUTED)
    draw.text((1680, 38), f"{num:02d} / 20", font=font(24, True), fill=YELLOW)
    draw.rectangle((0, H - 58, W, H), fill="#eef2f7")
    draw.text((78, H - 42), "PyWebView 단계별 실습 · timer/clock", font=font(20), fill=MUTED)
    return img, draw


def badge(draw, xy, text, fill=BLUE):
    x, y = xy
    tw, th = text_size(draw, text, font(24, True))
    rounded(draw, (x, y, x + tw + 34, y + 48), fill=fill, radius=24)
    draw.text((x + 17, y + 10), text, font=font(24, True), fill="#ffffff")


def box(draw, xy, title, body="", color=BLUE):
    rounded(draw, xy, fill="#ffffff", outline=color, radius=24, width=4)
    x1, y1, x2, y2 = xy
    draw.text((x1 + 28, y1 + 24), title, font=font(30, True), fill=color)
    if body:
        draw_wrapped(draw, body, (x1 + 28, y1 + 76), font(24), fill=INK, width_chars=max(16, (x2 - x1) // 24))


def bullet_list(draw, items, xy, fnt=None, color=INK, gap=18):
    fnt = fnt or font(30)
    x, y = xy
    for item in items:
        draw.ellipse((x, y + 12, x + 14, y + 26), fill=BLUE)
        y = draw_wrapped(draw, item, (x + 30, y), fnt, fill=color, width_chars=43, line_gap=8) + gap
    return y


def code_block(draw, xy, lines, width=760, height=300):
    x, y = xy
    rounded(draw, (x, y, x + width, y + height), fill="#111827", radius=20)
    yy = y + 28
    for line in lines:
        draw.text((x + 28, yy), line, font=font(24), fill="#e5e7eb")
        yy += 36


def slide_1():
    img, draw = make_base(1, "PyWebView 탁상 시계", "Python 백엔드와 WebView 프론트엔드를 분리하는 첫 수업")
    art = load_asset("imagen-architecture-metaphor.png", (860, 560))
    if art:
        paste_center(img, art, (930, 190, 1780, 770))
    py = load_asset("python-logo.png", (300, 100))
    pv = load_asset("pywebview-logo.png", (280, 120))
    if py:
        img.alpha_composite(py, (94, 205))
    if pv:
        img.alpha_composite(pv, (96, 330))
    draw.text((94, 500), "핵심 질문", font=font(34, True), fill=BLUE)
    draw_wrapped(draw, "웹 기술로 데스크톱 창을 만들 때, 왜 Python과 화면 코드를 분리해야 할까?", (94, 555), font(34), width_chars=29)
    badge(draw, (94, 820), "20장 이미지 강의자료", GREEN)
    return img


def slide_2():
    img, draw = make_base(2, "오늘의 학습 목표")
    bullet_list(draw, [
        "WebView 기반 데스크톱 앱의 기본 동작 이해",
        "단순 데모에서 시작해 문제를 발견하고 구조 개선",
        "HTML/CSS/JS와 Python 백엔드를 역할별로 분리",
        "localhost JSON API로 필요한 DOM만 갱신",
    ], (120, 210), font(36))
    box(draw, (1120, 220, 1740, 680), "수업의 큰 그림", "작게 만들고 → 불편을 관찰하고 → 구조로 해결한다.", PURPLE)
    return img


def slide_3():
    img, draw = make_base(3, "비유: 쇼윈도와 작업실")
    box(draw, (130, 250, 760, 690), "WebView 화면", "학생이 보는 쇼윈도\nHTML/CSS/JS가 담당\n예쁘고 빠르게 보여준다", BLUE)
    box(draw, (1160, 250, 1790, 690), "Python 백엔드", "실제 작업실\n시간 계산, 파일, DB, 시스템 기능\n규칙과 상태를 관리한다", GREEN)
    arrow(draw, (780, 470), (1140, 470), fill=YELLOW, width=12)
    draw.text((815, 410), "작은 약속(JSON API)", font=font(30, True), fill=NAVY)
    return img


def slide_4():
    img, draw = make_base(4, "반복형 수업 진행 방식")
    steps = [
        ("1", "단순 데모", "가장 빨리 동작하게 만든다"),
        ("2", "문제 발견", "가독성, 깜빡임, 확장성 문제를 본다"),
        ("3", "구조 개선", "역할 분리와 API로 해결한다"),
        ("4", "다음 확장", "실습 과제로 연결한다"),
    ]
    x = 105
    for n, title, body in steps:
        box(draw, (x, 300, x + 380, 640), f"{n}. {title}", body, BLUE if n != "2" else RED)
        if n != "4":
            arrow(draw, (x + 390, 470), (x + 470, 470), fill=MUTED, width=7)
        x += 440
    return img


def slide_5():
    img, draw = make_base(5, "단계 A: 가장 단순한 데모")
    code_block(draw, (110, 260), [
        "import webview",
        "",
        "webview.create_window(",
        "    'Hello',",
        "    html='<h1>Hello</h1>'",
        ")",
        "webview.start()",
    ], width=780, height=380)
    box(draw, (1040, 265, 1740, 650), "장점", "파일 하나로 바로 실행된다.\n처음 WebView 개념을 보여주기 좋다.", GREEN)
    draw.text((1040, 735), "그러나 수업은 여기서 멈추지 않는다.", font=font(34, True), fill=RED)
    return img


def slide_6():
    img, draw = make_base(6, "문제 1: Python 문자열 안에 화면 코드가 섞인다")
    rounded(draw, (120, 220, 1780, 760), fill="#fff7ed", outline="#fed7aa", radius=30, width=4)
    code_block(draw, (180, 280), [
        "html = \"<style>...</style><script>...</script>\"",
        "webview.create_window('Clock', html=html)",
        "",
        "# 시간이 지나면 문자열이 점점 길어진다",
        "# 따옴표, 들여쓰기, CSS, JS가 뒤섞인다",
    ], width=920, height=340)
    draw.text((1180, 315), "비유", font=font(34, True), fill=RED)
    draw_wrapped(draw, "요리 레시피, 재료 목록, 계산서가 한 종이에 뒤엉킨 상태", (1180, 375), font(34), width_chars=18)
    return img


def slide_7():
    img, draw = make_base(7, "해결 1: 파일을 역할별로 분리")
    box(draw, (130, 250, 530, 650), "index.html", "구조\n시간과 날짜가 놓일 자리", BLUE)
    box(draw, (610, 250, 1010, 650), "style.css", "표현\n글꼴, 색상, 배치", PURPLE)
    box(draw, (1090, 250, 1490, 650), "app.js", "행동\nAPI 호출과 DOM 갱신", GREEN)
    box(draw, (1540, 250, 1810, 650), "main.py", "창 실행", NAVY)
    draw.text((160, 760), "강의 포인트: 동작하는 코드와 유지보수 가능한 코드는 다르다.", font=font(34, True), fill=INK)
    return img


def slide_8():
    img, draw = make_base(8, "base path: 파일을 어디서 찾을 것인가")
    code_block(draw, (110, 245), [
        "BASE_DIR = Path(__file__).resolve().parent",
        "FRONTEND_DIR = BASE_DIR / 'frontend'",
        "",
        "url = server.base_url",
    ], width=880, height=260)
    box(draw, (1120, 245, 1740, 640), "비유: 약속 장소", "상대 경로만 믿으면 실행 위치에 따라 길을 잃는다.\n현재 파일 기준으로 출발점을 정하면 안정적이다.", BLUE)
    badge(draw, (1120, 700), "Path(__file__) 기준", GREEN)
    return img


def slide_9():
    img, draw = make_base(9, "문제 2: 시간을 바꾸려고 페이지 전체를 다시 로드")
    box(draw, (130, 250, 760, 690), "전체 리로드", "집의 시계만 바꾸려고\n집 전체를 다시 짓는 방식", RED)
    box(draw, (1160, 250, 1790, 690), "부분 갱신", "시계 바늘만 움직이는 방식\n필요한 DOM만 바꾼다", GREEN)
    arrow(draw, (785, 470), (1135, 470), fill=YELLOW, width=12)
    draw.text((710, 760), "목표: 화면 전체가 아니라 데이터만 갱신", font=font(40, True), fill=NAVY)
    return img


def slide_10():
    img, draw = make_base(10, "DOM 부분 갱신: 최소 단위로 바꾸기")
    rounded(draw, (150, 230, 880, 720), fill="#ffffff", outline=LINE, radius=30, width=4)
    draw.text((210, 300), "HTML", font=font(34, True), fill=BLUE)
    code_block(draw, (210, 370), [
        "<div id='time'>--:--:--</div>",
        "<div id='date'>----</div>",
    ], width=600, height=170)
    rounded(draw, (1030, 230, 1760, 720), fill="#ffffff", outline=LINE, radius=30, width=4)
    draw.text((1090, 300), "JS", font=font(34, True), fill=GREEN)
    code_block(draw, (1090, 370), [
        "timeEl.textContent = payload.time",
        "dateEl.textContent = payload.date",
    ], width=600, height=170)
    arrow(draw, (890, 475), (1020, 475), fill=YELLOW, width=10)
    return img


def slide_11():
    img, draw = make_base(11, "최종 아키텍처: Python + localhost + WebView")
    art = load_asset("imagen-architecture-metaphor.png", (700, 430))
    if art:
        paste_center(img, art, (1060, 200, 1760, 650), alpha=230)
    box(draw, (130, 220, 560, 420), "PyWebView 창", "localhost URL을 화면에 로드", BLUE)
    box(draw, (130, 500, 560, 700), "Frontend", "HTML/CSS/JS\nDOM 텍스트 갱신", PURPLE)
    box(draw, (640, 360, 1030, 560), "Backend", "ClockApiServer\n/api/clock 제공", GREEN)
    arrow(draw, (560, 600), (640, 470), fill=YELLOW, width=10)
    arrow(draw, (640, 430), (560, 330), fill=YELLOW, width=10)
    return img


def slide_12():
    img, draw = make_base(12, "localhost/루프백: 같은 컴퓨터 안의 복도")
    box(draw, (160, 270, 700, 640), "127.0.0.1", "내 컴퓨터 자신을 가리키는 주소", BLUE)
    box(draw, (1220, 270, 1760, 640), "프론트 ↔ 백엔드", "네트워크처럼 보이지만 같은 머신 내부 통신", GREEN)
    arrow(draw, (720, 455), (1200, 455), fill=YELLOW, width=14)
    draw.text((790, 385), "loopback", font=font(40, True), fill=NAVY)
    bullet_list(draw, [
        "분산 시스템을 만들려는 것이 아니다.",
        "역할 분리를 쉽게 설명하기 위한 설계 도구다.",
    ], (220, 760), font(32))
    return img


def slide_13():
    img, draw = make_base(13, "JSON API: 화면과 Python 사이의 작은 계약")
    code_block(draw, (120, 260), [
        "GET /api/clock",
        "",
        "{",
        "  \"time\": \"14:23:51\",",
        "  \"date\": \"2026년 5월 19일 화요일\"",
        "}",
    ], width=820, height=370)
    box(draw, (1080, 285, 1740, 645), "계약의 장점", "화면은 Python 내부 구현을 몰라도 된다.\nPython은 화면 디자인을 몰라도 된다.\n둘은 JSON 모양만 약속하면 된다.", BLUE)
    return img


def slide_14():
    img, draw = make_base(14, "Backend: ClockApiServer의 역할")
    bullet_list(draw, [
        "사용 가능한 포트를 찾는다.",
        "정적 파일(index.html, CSS, JS)을 제공한다.",
        "`/api/clock` 요청에 현재 시간 JSON을 반환한다.",
        "앱 종료 시 서버를 정리한다.",
    ], (130, 220), font(34))
    code_block(draw, (1040, 240), [
        "now = datetime.now()",
        "return {",
        "  'time': now.strftime('%H:%M:%S'),",
        "  'date': date_text,",
        "}",
    ], width=720, height=300)
    return img


def slide_15():
    img, draw = make_base(15, "Frontend: fetch 루프의 역할")
    code_block(draw, (115, 245), [
        "async function refreshClock() {",
        "  const response = await fetch('/api/clock')",
        "  const payload = await response.json()",
        "  timeEl.textContent = payload.time",
        "}",
        "setInterval(refreshClock, 1000)",
    ], width=900, height=350)
    box(draw, (1120, 260, 1740, 640), "JS는 얇게", "시간 계산을 하지 않는다.\n서버에서 받은 값을 화면에 반영한다.\n실패해도 UI 전체가 죽지 않게 처리한다.", GREEN)
    return img


def slide_16():
    img, draw = make_base(16, "포트 0: 빈 주차칸 자동 배정")
    box(draw, (130, 260, 720, 650), "문제", "포트를 고정하면 이미 사용 중일 수 있다.\n예: 8000, 3000 충돌", RED)
    box(draw, (1190, 260, 1780, 650), "해결", "포트 0으로 bind하면 OS가 빈 포트를 골라준다.", GREEN)
    arrow(draw, (745, 455), (1165, 455), fill=YELLOW, width=14)
    code_block(draw, (745, 690), [
        "sock.bind(('127.0.0.1', 0))",
        "port = sock.getsockname()[1]",
    ], width=700, height=120)
    return img


def slide_17():
    img, draw = make_base(17, "실패를 수업 재료로 쓰기")
    box(draw, (130, 220, 560, 600), "검은 화면", "문서 전체 리로드\n렌더링 비용\n상태 초기화", RED)
    box(draw, (745, 220, 1175, 600), "API 실패", "fetch 예외\n서버 중지\n응답 형식 오류", PURPLE)
    box(draw, (1360, 220, 1790, 600), "포트 충돌", "이미 사용 중\n권한 문제\n실행 환경 차이", BLUE)
    draw.text((230, 760), "데모 실패는 중단이 아니라 문제 정의 단계다.", font=font(42, True), fill=NAVY)
    return img


def slide_18():
    img, draw = make_base(18, "최종 파일 역할")
    rows = [
        ("timer/main.py", "서버 시작 + WebView 창 생성"),
        ("timer/backend/server.py", "정적 파일 제공 + /api/clock JSON 응답"),
        ("timer/frontend/index.html", "시간/날짜가 표시될 자리"),
        ("timer/frontend/style.css", "시계 화면의 시각 디자인"),
        ("timer/frontend/app.js", "fetch 호출 + DOM 텍스트 갱신"),
    ]
    y = 210
    for path, role in rows:
        rounded(draw, (140, y, 1780, y + 110), fill="#ffffff", outline=LINE, radius=18, width=3)
        draw.text((180, y + 32), path, font=font(30, True), fill=BLUE)
        draw.text((720, y + 32), role, font=font(30), fill=INK)
        y += 125
    return img


def slide_19():
    img, draw = make_base(19, "90분 수업 운영 흐름")
    timeline = [
        ("0~15분", "단순 WebView 데모"),
        ("15~30분", "파일 분리와 리로드 문제"),
        ("30~55분", "JSON API + DOM 갱신"),
        ("55~75분", "파일 구조 정리"),
        ("75~90분", "확장 과제와 발표"),
    ]
    y = 230
    for time, label in timeline:
        badge(draw, (160, y), time, BLUE)
        draw.text((420, y + 8), label, font=font(34, True), fill=INK)
        if y < 730:
            draw.line((250, y + 60, 250, y + 130), fill=LINE, width=8)
        y += 140
    return img


def slide_20():
    img, draw = make_base(20, "핵심 정리")
    bullet_list(draw, [
        "처음에는 단순하게 만들고, 불편함을 관찰한다.",
        "HTML/CSS/JS와 Python을 파일과 역할로 분리한다.",
        "페이지 전체를 다시 만들지 말고 필요한 DOM만 갱신한다.",
        "localhost JSON API는 화면과 Python 사이의 명확한 계약이다.",
        "다음 수업은 상태 공유와 실시간 동기화로 확장한다.",
    ], (120, 200), font(34))
    py = load_asset("python-logo.png", (260, 90))
    pv = load_asset("pywebview-logo.png", (290, 120))
    if py:
        img.alpha_composite(py, (1260, 720))
    if pv:
        img.alpha_composite(pv, (1260, 830))
    draw.text((1180, 610), "다음 연결", font=font(36, True), fill=BLUE)
    draw.text((1180, 660), "click counter · 서버 상태 · SSE", font=font(30), fill=INK)
    return img


SLIDES = [
    slide_1, slide_2, slide_3, slide_4, slide_5,
    slide_6, slide_7, slide_8, slide_9, slide_10,
    slide_11, slide_12, slide_13, slide_14, slide_15,
    slide_16, slide_17, slide_18, slide_19, slide_20,
]


def main() -> None:
    SLIDE_DIR.mkdir(parents=True, exist_ok=True)
    for old in SLIDE_DIR.glob("slide_*.png"):
        old.unlink()
    for index, maker in enumerate(SLIDES, start=1):
        maker().convert("RGB").save(SLIDE_DIR / f"slide_{index:02d}.png", quality=95)

    sources = OUT_DIR / "SOURCES.md"
    sources.write_text(
        "\n".join([
            "# Slide Asset Sources",
            "",
            "- GPT Imagen generated architecture metaphor: `assets/imagen-architecture-metaphor.png`",
            "- Python logo: https://www.python.org/community/logos/",
            "- pywebview logo from official documentation site: https://pywebview.flowrl.com/logo.png",
            "- uv logo downloaded from official documentation assets: https://docs.astral.sh/uv/assets/logo-letter.svg",
            "",
            "Korean slide text and diagrams were rendered locally with Pillow for accuracy.",
        ]),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
