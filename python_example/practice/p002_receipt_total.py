"""
Practice 002. 영수증 합계 계산

난이도: beginner
수업 순서: 002
학습 주제: 변수/산술연산
관련 기본 예제: basic/a03-a10

문제:
    상품 가격과 수량을 받아 공급가액, 부가세, 총액을 딕셔너리로 반환하세요.

예시:
    - (10000, 3) -> {"subtotal": 30000, "vat": 3000, "total": 33000}

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 2
TOPIC = "변수/산술연산"
TITLE = "영수증 합계 계산"


def calculate_receipt(*args, **kwargs):
    """문제 요구사항에 맞게 구현하세요."""
    # TODO: 학생 실습 코드 작성
    raise NotImplementedError("영수증 합계 계산 문제를 구현하세요.")


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    print("이 파일은 학생 실습용 골격입니다. TODO를 구현한 뒤 직접 테스트하세요.")


if __name__ == "__main__":
    main()
