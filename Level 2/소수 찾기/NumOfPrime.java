class NumOfPrime {
    int numberOfPrime(int n) {
        int answer = 0;
        int i,j;
        int multiple;
        for (i = 1; i < n + 1; i++) {
            multiple = 0;
            for (j = 1; j < i + 1; j++) {
                if (i % j == 0) {
                    multiple += 1;
                }
            }
            if (multiple == 2) {
                answer += 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        NumOfPrime prime = new NumOfPrime();
        System.out.println( prime.numberOfPrime(10) );
    }

}