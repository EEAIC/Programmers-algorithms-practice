#include<iostream>
#include<string>
using namespace std;

string caesar(string s, int n)
{
	string answer = "";
	if (n > 26) {
		n = n - n / 26 * 26;
	}
	for (int i = 0; i < s.length(); i++) {
		int Tmp = 0;
		Tmp = s[i];
		if (Tmp != 32) {
			if (97 <= Tmp && Tmp <= 122) {
				Tmp = Tmp + n;
				if (Tmp > 122) {
					Tmp = Tmp - 122 + 96;
				}
			}
			else if (65 <= Tmp && Tmp <= 90) {
				Tmp = Tmp + n;
				if (Tmp > 90) {
					Tmp = Tmp - 90 + 64;
				}
			}
		}
		answer.push_back(Tmp);
	}
	return answer;
}

int main()
{
	string text = "a B z";
	int testNo = 4;

	string testAnswer = caesar(text, testNo);

	cout << testAnswer;
}