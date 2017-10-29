#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>

using namespace std;

int noOvertime(int no, vector<int> works)
{
	int answer = 0;
	for (int i = 0; i < no; i++) {
		int max_indent = distance(works.begin(), max_element(works.begin(), works.end()));
		works[max_indent] = works[max_indent] - 1;
	}
	for (int i = 0; i < works.size(); i++) {
		answer += works[i] * works[i];
	}
	return answer;
}

int main()
{
	vector<int> works{ 4,3,3 };
	int testNo = 4;

	int testAnswer = noOvertime(testNo, works);

	cout << testAnswer;
}