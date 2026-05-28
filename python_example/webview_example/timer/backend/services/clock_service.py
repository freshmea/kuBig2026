from datetime import datetime

WEEKDAYS = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]


def get_clock_payload():
    now = datetime.now()
    date_text = (
        f"{now.year}년 {now.month}월 {now.day}일 "
        f"{WEEKDAYS[now.weekday()]}"
    )
    return {
        "time": now.strftime("%H:%M:%S"),
        "date": date_text,
    }
