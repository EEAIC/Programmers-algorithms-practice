#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> >productMatrix(vector<vector<int> >A, vector<vector<int> >B)
{
	vector<vector<int> >answer;
  vector<int> tmp;
    int tmp_Sum = 0;
    int i, j, k;
 		tmp.clear();
    for (i = 0; i < A.size(); i++){
       tmp.clear();
        for (j = 0; j < B[0].size(); j++){
            tmp_Sum = 0;
            for (k = 0; k < A[0].size(); k++){
            	tmp_Sum += A[i][k] * B[k][j];
            }
            tmp.push_back(tmp_Sum);
        }
        answer.push_back(tmp);
    }
    return answer;
}

int main()
{
	vector<vector<int> >A{{1,2},{2,3}};
	vector<vector<int> >B{{2,3},{3,4}};
	vector<vector<int> > testAnswer = productMatrix(A,B);

	for(int i=0;i<testAnswer.size(); i++)
	{
		for(int j=0;j<testAnswer[i].size(); j++)
			cout<<testAnswer[i][j]<<" ";
		cout<<"\n";
	}
}
