def adder(a, b):
    inputNum = [a,b]
    inputNum.sort()
    current = inputNum[0]
    sum = 0
    for i in range(inputNum[1] - inputNum[0] + 1):
        sum += current
        current += 1
    # 함수를 완성하세요
    return sum

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
