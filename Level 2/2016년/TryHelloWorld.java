class TryHelloWorld
{
    public String getDayName(int a, int b)
    {
        String[] day = {"FRI", "SAT", "SUN","MON", "TUE", "WED", "THU"};
        int i = 0;
        int total_days = - 1;
        int date = 0;
        for (i = 1; i < a; i++){
            if (i != a){
                if ((1 <= i && i <= 7 && i % 2 == 1) || (8 <= i && i <= 11 && i % 2 == 0)) {
                    total_days += 31;
                }
                else if ((3 <= i && i <= 7 && i % 2 == 0) || (8 <= i && i <= 11 && i % 2 == 1)){
                    total_days += 30;
                }
                else if (i == 2){
                    total_days += 29;
                }
            }
        }
        total_days += b;
        date = total_days % 7;
        return day[date];
    }
    public static void main(String[] args)
    {
        TryHelloWorld test = new TryHelloWorld();
        int a=5, b=24;
        System.out.println(test.getDayName(a,b));
    }
}

