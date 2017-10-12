public class WaterMelon {
    public String watermelon(int n){
        if (n % 2 == 0){
            String s = "수박";
            for (int i = 1; i < n/2; i++){
                s = s.concat("수박");
            }
            return  s;
        }
        else {
            String s = "수";
            for (int i = 1; i <= n/2; i++){
                s = s.concat("박수");
            }
            return s;
        }
    }

    // 실행을 위한 테스트코드입니다.
    public static void  main(String[] args){
        WaterMelon wm = new WaterMelon();
        System.out.println("n이 3인 경우: " + wm.watermelon(3));
        System.out.println("n이 4인 경우: " + wm.watermelon(4));
    }
}
