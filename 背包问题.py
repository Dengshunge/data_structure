# 引入numpy只是为了方便显示数据而已
import numpy as np

# 0-1背包
def max_Value(weigth,value,bagWeigth):
    dp = [[0 for i in range(bagWeigth+1)] for i in range(len(value))] # 列为重量，行为物品
    # 处理第一行
    for i in range(bagWeigth + 1):
        if i >= weigth[0]:
            dp[0][i] = value[0]
    # 处理剩余的物品
    for item in range(1,len(value)):
        for j in range(1,bagWeigth+1):
            if j < weigth[item]:
                dp[item][j] = dp[item - 1][j]
            else:
                dp[item][j] = max(dp[item - 1][j], dp[item - 1][j - weigth[item]] + value[item])
    print(np.array(dp))

    # 下面是寻找当取得最大价值时，是由哪些构成的
    x = [False for i in range(len(value))]
    j = bagWeigth
    for i in range(len(value)-1,-1,-1):
        # 由于第一行比较特殊，所以要分开处理
        if (i != 0 and dp[i][j] > dp[i - 1][j]) or (i == 0 and dp[i][j] > 0):
            x[i] = True
            j -= weigth[i]
    print(x)

weigth = [2,2,6,5,4]
value = [6,3,5,4,6]
bagWeigth = 10
max_Value(weigth,value,bagWeigth)
