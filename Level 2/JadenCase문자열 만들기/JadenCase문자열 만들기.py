def Jaden_Case(s):
    # 함수를 완성하세요
    rst = ""
    for i in range(len(s.split(' '))):
        if s.split(' ')[i]:
            rst += s.split(' ')[i][0].upper()
            if len(s.split(' ')[i]) > 1:
                rst += str(s.split(' ')[i][1:].lower())
            if i != len(s.split(' ')) - 1:
                rst += " "
    return rst


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
