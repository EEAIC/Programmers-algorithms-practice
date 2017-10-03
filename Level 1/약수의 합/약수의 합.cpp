#include<iostream>
using namespace std;

int sumDivisor(int n)
{
	int Divider = 1;
	int Sum = 0;
	while (Divider <= n) {
		if (n % Divider == 0) {
			Sum += Divider;
		}
		Divider++;
	}
	return Sum;
}

int main()
{
	int testCase = 10;
	int testAnswer = sumDivisor(testCase);

	cout << testAnswer;
}