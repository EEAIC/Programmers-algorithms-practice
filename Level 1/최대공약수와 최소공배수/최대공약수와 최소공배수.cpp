#include<vector>
#include<iostream>
using namespace std;
vector<int> gcdlcm(int a, int b)
{
	vector<int> answer;
	int gcd = 1;
	int divider = 2;
	while (a >= divider && b >= divider) {
		if (a % divider == 0 && b % divider == 0) {
			a /= divider;
			b /= divider;
			gcd *= divider;
		}
		else {
			divider++;
		}
	}
	answer.push_back(gcd);
	answer.push_back(gcd * a * b);
	return answer;
}

int main()
{
	int a = 3, b = 12;
	vector<int> testAnswer = gcdlcm(a, b);

	cout << testAnswer[0] << " " << testAnswer[1];
}