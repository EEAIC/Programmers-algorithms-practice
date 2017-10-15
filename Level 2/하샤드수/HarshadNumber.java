public class HarshadNumber{
    public boolean isHarshad(int num){

        int Sum_n = 0;
        boolean rst = false;
        String Tmp_num = String.valueOf(num);
        for (int i = 0; i<Tmp_num.length();i++){
            Sum_n += Character.getNumericValue(Tmp_num.charAt(i));
        }
        if (num % Sum_n == 0){
            rst = true;
        }
        return rst;
    }
    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        HarshadNumber sn = new HarshadNumber();
        System.out.println(sn.isHarshad(18));
    }
}