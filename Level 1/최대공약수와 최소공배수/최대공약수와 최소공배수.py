def gcdlcm(a, b):
    answer = []
    divider = 2
    gcd = 1
    while a >= divider and b >= divider:
        if a % divider == 0 and b % divider == 0:
            a //= divider
            b //= divider
            gcd *= divider
        else:
            divider += 1
    answer.append(gcd)
    answer.append(gcd * a * b)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))