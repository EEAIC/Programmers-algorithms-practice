#include<iostream>
using namespace std;
long long fibonacci(int n)
{
	int level = 1;
	long long previous_val = 0;
	long long current_val = 0;
	long long Tmp = 0;
	while (level <= n) {
		if (level == 1) {
			previous_val = 0;
			current_val = 1;
			level++;
		}
		else {
			Tmp = current_val;
			current_val = previous_val + current_val;
			previous_val = Tmp;
			level++;
		}
	}
	return current_val;
}

int main()
{
	int testCase = 10;
	long long testAnswer = fibonacci(testCase);

	cout << testAnswer;
}