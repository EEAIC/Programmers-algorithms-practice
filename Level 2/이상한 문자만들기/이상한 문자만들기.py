def toWeirdCase(s):
    # 함수를 완성하세요
    rst = ""
    for i in range(len(s.split(' '))):
        if s.split(' ')[i]:
            for j in range(len(s.split(' ')[i])):
                if j % 2 == 0:
                    rst += s.split(' ')[i][j].upper()
                else:
                    rst += str(s.split(' ')[i][j].lower())
            if i != len(s.split(' ')) - 1:
                rst += " "
    return rst

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")))
