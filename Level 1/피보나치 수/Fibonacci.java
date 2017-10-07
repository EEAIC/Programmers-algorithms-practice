class Fibonacci {
    public long fibonacci(int num) {
        int level = 1;
        long previous_val = 0;
        long current_val = 0;
        long Tmp = 0;
        while (level <= num){
            if (level == 1){
                previous_val = 0;
                current_val = 1;
                level++;
            }
            else {
                Tmp = current_val;
                current_val = previous_val + current_val;
                previous_val = Tmp;
                level++;
            }
        }
        return current_val;
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        Fibonacci c = new Fibonacci();
        int testCase = 3;
        System.out.println(c.fibonacci(testCase));
    }
}

