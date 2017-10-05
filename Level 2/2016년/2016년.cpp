#include<iostream>
#include<string>
#include<vector>

using namespace std;
string getDayName(int a,int b)
{
    vector <string> day = {"FRI", "SAT", "SUN","MON", "TUE", "WED", "THU"};
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
int main()
{
	int a=5,b=24;

	//아래는 테스트 출력을 위한 코드입니다.
	cout<<getDayName(a,b);
}
