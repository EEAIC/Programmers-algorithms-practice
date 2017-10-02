def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    sum = 0
    num_list = list(str(number))
    for i in range(len(num_list)):
        sum += int(num_list[i])
    return sum
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));
