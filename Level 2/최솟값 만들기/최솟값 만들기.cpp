#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int getMinSum(vector<int> A, vector<int> B)
{
	int answer = 0;
  int i;
	sort(A.begin(),A.end());
  sort(B.begin(),B.end());
  reverse(B.begin(), B.end());
  for (i = 0; i < A.size(); i++){
  	answer += A[i] * B[i];
  }
	return answer;
}
int main()
{
	vector<int> tA{1,2}, tB{3,4};

	//아래는 테스트 출력을 위한 코드입니다.
	cout<<getMinSum(tA,tB);
}
