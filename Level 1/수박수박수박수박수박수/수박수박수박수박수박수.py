def water_melon(n):
    if n % 2 == 0:
        return "수박" * (n // 2)
    else:
        return "수박" * (n // 2) + "수"


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
