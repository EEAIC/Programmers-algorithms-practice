def is_pair(s):
    # 함수를 완성하세요
    list_pair = list(s)
    num = 0
    for i in range(len(list_pair)):
        if list_pair[0] == "(":
            num += 1
        elif list_pair[0] == ")":
            num -= 1
        del list_pair[0]
        if num < 0:
            return False
    if num == 0:
        return True
    else:
        return False
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))
