def sumDivisor(num):
    answer = 1
    divider = 2
    while divider <= num:
        if num % divider == 0:
            answer += divider
            divider += 1
        else:
            divider += 1
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))