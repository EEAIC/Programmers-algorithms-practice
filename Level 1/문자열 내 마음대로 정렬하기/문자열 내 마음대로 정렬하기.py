def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    list_rst = []
    #list_str[0][0], list_str[0][n] = list_str[0][n], list_str[0][0]
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    for i in range(len(strings)):
        tmp = ""
        tmp += strings[i][1:]
        list_rst.append(tmp)
    return list_rst

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strange_sort(["sun", "bed", "car"], 1))

