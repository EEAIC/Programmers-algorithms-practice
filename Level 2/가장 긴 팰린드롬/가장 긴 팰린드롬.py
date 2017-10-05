def longest_palindrom(s):
    # 함수를 완성하세요
    main_list = list(s)
    tmp_list = list(s)
    tmp_list.reverse()
    longest_num = 0
    Sum = 0
    for i in range(len(s)):
        for j in range(len(s), 0, -1):
            if main_list[i:j] == tmp_list[len(s) - j:len(s) - i]:
                if j - i >= longest_num:
                    longest_num = j - i
    return longest_num


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))
