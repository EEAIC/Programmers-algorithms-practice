#include<iostream>
using namespace std;

int numOfPrime(int n)
{
	int answer = 0;
  int i,j;
  int multiple;
  for (i = 1; i < n + 1; i++) {
      multiple = 0;
      for (j = 1; j < i + 1; j++) {
          if (i % j == 0) {
              multiple += 1;
          }
      }
      if (multiple == 2) {
          answer += 1;
      }
  }
	return answer;
}

int main()
{
	int testCase = 10;
	int testAnswer = numOfPrime(testCase);

	cout<<testAnswer;
}
