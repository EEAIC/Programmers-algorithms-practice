def numPY(s):
    # 함수를 완성하세요
    num_p = 0
    num_y = 0
    for i in range(len(s)):
        if "p" == s[i] or "P" == s[i]:
            num_p += 1
    for i in range(len(s)):
        if "y" == s[i] or "Y" == s[i]:
            num_y += 1
    if num_p == num_y:
        return True
    else:
        return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )