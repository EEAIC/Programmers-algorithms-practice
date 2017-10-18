class Collatz {
    public int collatz(long num) {
        int answer = 0;
        while (num != 1){
            if (answer >= 500){
                answer = -1;
                break;
            }
            else if (num % 2 == 0){
                num = num / 2;
                answer++;
            }
            else {
                num = num * 3 + 1;
                answer++;
            }
        }

        return answer;
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        Collatz c = new Collatz();
        int ex = 6;
        System.out.println(c.collatz(ex));
    }
}