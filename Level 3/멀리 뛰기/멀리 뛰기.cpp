#include<iostream>
#include<vector>
using namespace std;

int jumpCase(int n)
{
	int answer = 0;
	if (n > 0) {
		answer += jumpCase(n - 1);
		answer += jumpCase(n - 2);
	}
	else if (n == 0) {
		return 1;
	}
	else {
		return 0;
	}
	return answer;
}

int main()
{
	int test = 4;

	//�Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	cout << jumpCase(test);
}
