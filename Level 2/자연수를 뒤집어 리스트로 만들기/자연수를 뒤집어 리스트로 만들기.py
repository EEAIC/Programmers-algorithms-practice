def digit_reverse(n):
    # 함수를 완성해 주세요
    rst_list = list(str(n))
    rst_list.reverse()
    for  i in range(len(rst_list)):
        rst_list[i] = int(rst_list[i])
    return rst_list

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)))
