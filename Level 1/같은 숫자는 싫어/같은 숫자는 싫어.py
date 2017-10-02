def no_continuous(s):
    # 함수를 완성하세요
    set_no_continuous = []
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            set_no_continuous += s[i]
            if i + 1 == len(s) - 1:
                set_no_continuous += s[i + 1]
        elif i + 1 == len(s) - 1:
            set_no_continuous += s[i]
    return set_no_continuous

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(no_continuous("1333033"))