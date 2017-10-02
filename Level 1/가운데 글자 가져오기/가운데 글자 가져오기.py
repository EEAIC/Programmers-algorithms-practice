def string_middle(str):
    # 함수를 완성하세요
    wordlist = list(str)
    if len(wordlist) % 2 == 0:
        return wordlist[len(wordlist) // 2 - 1] + wordlist[len(wordlist) // 2]
    else:
        return wordlist[len(wordlist) // 2]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
