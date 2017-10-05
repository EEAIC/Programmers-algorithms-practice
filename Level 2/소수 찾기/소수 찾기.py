def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?

    num = 0
    for i in range(1,n+1):
        multiple = 0
        for j in range(1, i+1):
            if i % j == 0:
                multiple += 1
        if multiple == 2:
            num += 1
    return num


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))
