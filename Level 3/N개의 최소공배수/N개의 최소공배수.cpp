#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

long long gcd(long long a, long long b)
{
	return b ? gcd(b, a % b) : a;
}

long long lcm(long long a, long long b) {
	return (a * b) / gcd(max(a, b), min(a, b));
}

long long nlcm(vector<int> num)
{
	long long answer = num[0];
	for (int i = 1; i < num.size(); i++) {
		answer = lcm(answer, num[i]);
	}
	return answer;
}

int main()
{
	vector<int> test{ 2,6,8,14 };

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	cout << nlcm(test);
}

