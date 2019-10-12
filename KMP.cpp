#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

class Solution {
public:
	int KMP(string S, string P)
	{
		vector<int> next = GetNext(P);
		int i = 0;//S的下标
		int j = -1;//P的下标
		int s_len = S.size(), p_len = P.size();
		while (i<s_len&&j<p_len)
		{
			if (j == -1 || S[i] == P[j])// P 的第一个字符不匹配或 S[i] == P[j]
			{
				i++;
				j++;
			}
			else
				j = next[j];// 当前字符匹配失败，进行跳转
		}
		if (j == p_len)// 匹配成功
			return i - j;
		return -1;
	}
private:
	vector<int> GetNext(string P)
	{
		int len = P.size();
		vector<int> next(len, -1);
		int i = 0, j = -1;
		while (i<len-1)
		{
			if (j == -1 || P[i] == P[j])
			{
				i++;
				j++;
				if (P[i] != P[j])
					next[i] = j;
				else
					next[i] = next[j];
			}
			else
				j = next[j];
		}
	}
};


int main()
{
	Solution a;
	
	string S = "aaaaa";
	string P = "bba";
	cout << a.KMP(S, P) << endl;


	system("pause");
}

