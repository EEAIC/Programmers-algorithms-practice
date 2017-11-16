#include<iostream>
#include<bitset>
#include<cmath>
using namespace std;

int nextBigNumber(int n)
{
	int answer = 0;
	int cnt = 0;
	int tmp_cnt = -1;
	bitset<20> tmp(n);
	for (int i = 0; i < tmp.size(); i++) {
		if (tmp[i] == 1) {
			cnt++;
		}
	}
	while (cnt != tmp_cnt) {
		++n;
		tmp = n;
		tmp_cnt = 0;
		for (int i = 0; i < tmp.size(); i++) {
			if (tmp[i] == 1) {
				tmp_cnt++;
			}
		}
	}
	for (int i = 0; i < tmp.size(); i++) {
		answer += tmp[i] * pow(2, i);
	}
	return answer;
}
int main()
{
	int n = 78;

	//아래는 테스트 출력을 위한 코드입니다.
	cout << nextBigNumber(n);
}
