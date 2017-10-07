class SumDivisor {
    public int sumDivisor(int num) {
        int Divider = 1;
        int Sum = 0;
        while (Divider <= num){
            if (num % Divider == 0){
                Sum += Divider;
            }
            Divider++;
        }
        return Sum;
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        SumDivisor c = new SumDivisor();
        System.out.println(c.sumDivisor(12));
    }
}

