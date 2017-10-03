dp = {}
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num in dp:
        return dp[num]
    else:
        sum = fibonacci(num - 1) + fibonacci(num - 2)
        dp[num] = sum
        return sum
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))