def nextSqure(n):
    # 함수를 완성하세요
    i = 1
    while True:
        if i ** 2 == n:
            return (i + 1) ** 2
        elif i ** 2 > n:
            return 'no'
        i += 1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)))
