#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>
#include <unordered_set>
#include <time.h>
#include "linearlist.cpp"

using namespace std;

class Solution {
public:
	int Bag0_1(vector<int> &weight, vector<int> &val, int max_weight)
	{
		int num_of_object = weight.size();
		vector<vector<int>> dp(num_of_object, vector<int>(max_weight + 1, 0));
		for (int i = 0; i <= max_weight; ++i)
			if (i >= weight[0])
				dp[0][i] = val[0];
		for (int i = 1; i < num_of_object; ++i)
		{
			for (int j = 0; j <= max_weight; ++j)
			{
				if (j < weight[i])
					dp[i][j] = dp[i - 1][j];
				else
					dp[i][j] = max(dp[i - 1][j - weight[i]] + val[i], dp[i - 1][j]);
			}
		}
		return dp.back().back();
	}
};



int main()
{
	Solution a;
	vector<int> weight = { 2,3,4,5 };
	vector<int> val = { 3,4,5,6 };
	cout << a.Bag0_1(weight, val, 8) << endl;

	system("pause");
}

