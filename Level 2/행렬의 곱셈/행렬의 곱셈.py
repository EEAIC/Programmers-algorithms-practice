def productMatrix(A, B):
    answer = []
    tmp_Sum = 0
    for i in range(len(A)):
        tmp = []
        for j in range(len(A[0])):
            tmp_Sum = 0
            for k in range(len(B)):
                tmp_Sum += A[i][k] * B[k][j]
            tmp.append(tmp_Sum)
        answer.append(tmp)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))
