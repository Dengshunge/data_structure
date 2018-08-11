# 引入numpy只是为了方便显示数据而已
import numpy as np
'''
背包问题一共包含三个：0-1背包，完全背包，多重背包
是个很经典的题目，利用动态规划，值得研究一下
这只是最基本的题目。
参考了https://blog.csdn.net/na_beginning/article/details/62884939
'''

class Solution:
    # 0-1背包
    def Bag0_1(self,weigth,value,bagWeigth):
        dp = [[0 for i in range(bagWeigth+1)] for i in range(len(value))] # 列为重量，行为物品
        # 处理第一行
        for i in range(bagWeigth + 1):
            if i >= weigth[0]:
                dp[0][i] = value[0]
        # 处理剩余的物品
        for item in range(1, len(value)):
            for j in range(1, bagWeigth + 1):
                if j < weigth[item]:
                    dp[item][j] = dp[item - 1][j]
                else:
                    dp[item][j] = max(dp[item - 1][j], dp[item - 1][j - weigth[item]] + value[item])
        print(np.array(dp))

        # 下面是寻找当取得最大价值时，是由哪些构成的
        x = [False for i in range(len(value))]
        j = bagWeigth
        for i in range(len(value) - 1, -1, -1):
            # 由于第一行比较特殊，所以要分开处理
            if (i != 0 and dp[i][j] > dp[i - 1][j]) or (i == 0 and dp[i][j] > 0):
                x[i] = True
                j -= weigth[i]
        print(x)

    # 完全背包问题
    def AllBag(self,weigth,value,bagWeigth):
        dp = [[0 for i in range(bagWeigth+1)] for i in range(len(value))] # 列为重量，行为物品
        # 处理第一个物品
        for i in range(1, bagWeigth + 1):
            dp[0][i] = int(i / weigth[0]) * value[0]
        # 处理剩下的物品
        for item in range(1, len(value)):
            for j in range(1, bagWeigth + 1):
                if j < weigth[item]:
                    dp[item][j] = dp[item - 1][j]
                else:
                    # 主要是这一行与0-1背包不同
                    dp[item][j] = max(dp[item - 1][j], dp[item][j - weigth[item]] + value[item])
        print(np.array(dp))
        # print(dp[-1][-1])

        # 寻找取了哪几个物品及数量
        num = {i:0 for i in range(len(value))}
        j = bagWeigth
        for i in range(len(value) - 1, -1, -1):  # 逆序
            if i >0:
                while j > 0 and dp[i][j] > dp[i-1][j]:
                    num[i] += 1
                    j -= weigth[i]
            else:
                while j>0 and dp[i][j] > 0:
                    num[i] += 1
                    j -= weigth[i]
        print(num)

    # 多重背包
    def MultiBag(self,weigth,value,numbers,bagWeigth):
        dp = [[0 for i in range(bagWeigth + 1)] for i in range(len(value))]  # 列为重量，行为物品
        # 处理第一个物品
        for i in range(bagWeigth+1):
            # 当数量i/weigth[0]没有超过numbers[0]时，可以得到该重量可以放的数量i/weigth[0]
            # 当数量i/weigth[0]超过numbers[0]时，总价值只能是numbers[0] * value[0]
            dp[0][i] = int(i / weigth[0]) * value[0] \
                if i <= weigth[0] * numbers[0] else numbers[0] * value[0]
        # 处理剩下物品
        for item in range(1, len(value)):
            for j in range(1, bagWeigth + 1):
                dp[item][j] = dp[item-1][j]
                # 下面处理最多放入k个商品item
                k = int(j / weigth[item]) if j <= weigth[item] * numbers[item] else numbers[item]
                for m in range(1, k + 1):
                    temp = dp[item - 1][j - m * weigth[item]] + m * value[item]
                    if temp > dp[item][j]:
                        dp[item][j] = temp
        print(np.array(dp))
        # print(dp[-1][-1])

        # 下面是寻找去了哪些物品机器数量
        item_map = {i: 0 for i in range(len(value))}
        j = bagWeigth
        for item in range(len(value) - 1, -1, -1):
            while (item > 0 and dp[item][j] > dp[item - 1][j]) or (item == 0 and dp[item][j] > 0):
                item_map[item] += 1
                j -= weigth[item]
                if item_map[item] >= numbers[item]:
                    break
        print(item_map)


weigth = [2,2,6,5,4]
value = [6,3,5,4,6]
bagWeigth = 10
a = Solution()
# a.Bag0_1(weigth,value,bagWeigth)
# a.AllBag([3,2,4,7],[3,1,5,9],bagWeigth)
a.MultiBag([1,2,2],[6,10,20],[10,5,2],8)
