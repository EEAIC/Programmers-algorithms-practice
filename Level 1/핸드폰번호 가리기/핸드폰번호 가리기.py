def hide_numbers(s):
    #함수를 완성해 별이를 도와주세요
    list_s = list(s)
    for i in range(len(list_s) - 4):
        list_s[i] = "*"
    return ''.join(list_s)
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));