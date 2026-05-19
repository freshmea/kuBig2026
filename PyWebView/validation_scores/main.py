from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


class ScoreApi:
    def validate_score(self, name: str, score: str) -> dict[str, object]:
        errors: list[str] = []
        clean_name = name.strip()
        if len(clean_name) < 2:
            errors.append("이름은 두 글자 이상이어야 합니다.")

        try:
            numeric_score = int(score)
        except ValueError:
            errors.append("점수는 정수여야 합니다.")
            numeric_score = 0

        if not 0 <= numeric_score <= 100:
            errors.append("점수는 0부터 100 사이여야 합니다.")

        if errors:
            return {"ok": False, "errors": errors}

        grade = "A" if numeric_score >= 90 else "B" if numeric_score >= 80 else "C"
        return {"ok": True, "student": {"name": clean_name, "score": numeric_score, "grade": grade}}


def main() -> None:
    webview.create_window(
        "06 Validation Scores",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=ScoreApi(),
        width=520,
        height=460,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
