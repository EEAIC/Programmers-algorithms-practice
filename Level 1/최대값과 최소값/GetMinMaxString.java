public class GetMinMaxString {
    public String getMinMaxString(String str) {
        String rst = "";
        String[] str_digit;
        int min = 0;
        int max = 0;
        str_digit = str.split(" ");
        max = min = Integer.parseInt(str_digit[0]);
        for (int i = 0; i < str_digit.length;i++){
            if (max < Integer.parseInt(str_digit[i])) {
                max = Integer.parseInt(str_digit[i]);
            }
            if (min > Integer.parseInt(str_digit[i])){
                min = Integer.parseInt(str_digit[i]);
            }
        }
        return min + " " + max;
    }

    public static void main(String[] args) {
        String str = "1 2 3 4";
        GetMinMaxString minMax = new GetMinMaxString();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString(str));
    }
}
