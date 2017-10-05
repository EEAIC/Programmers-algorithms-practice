#include<iostream>
using namespace std;

int collatz(int num)
{
	int answer = 0;
	while (num != 1) {
		if (answer == 500) {
			return -1;
		}
		else if (num % 2 == 0) {
			num /= 2;
			answer++;
		}
		else {
			num = num * 3 + 1;
			answer++;
		}
	}
	return answer;
}

int main()
{
	int testCase = 6;
	int testAnswer = collatz(testCase);

	cout << testAnswer;
}