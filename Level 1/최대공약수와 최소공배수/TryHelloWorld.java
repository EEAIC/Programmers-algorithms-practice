import java.util.Arrays;

class TryHelloWorld {
    public int[] gcdlcm(int a, int b) {
        int[] answer = new int[2];
        int gcd = 1;
        int divider = 2;
        while (a >= divider && b >= divider) {
            if ( a % divider == 0 && b % divider == 0){
                a /= divider;
                b /= divider;
                gcd *= divider;
            }
            else{
                divider++;
            }
        }
        answer[0] = gcd;
        answer[1] = gcd * a * b;
        return answer;
    }
    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        TryHelloWorld c = new TryHelloWorld();
        System.out.println(Arrays.toString(c.gcdlcm(3, 12)));
    }
}

