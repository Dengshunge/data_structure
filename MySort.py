class Sort:
    def __init__(self,lis=None):
        self.lis = lis
        self.size = len(lis)

    def swap(self,x=0,y=0):
        assert x<self.size and y<self.size
        self.lis[x],self.lis[y] = self.lis[y],self.lis[x]

    def print(self):
        print(' '.join(map(str,self.lis)))

class Bubble_Sort(Sort):
    # 冒泡排序
    def BubbleSort0(self):
        #用lis[i]和lis[j]逐个比较，当lis[j]<lis[i]，发生交换，使得lis[i]保存的是每次比较的最小值
        for i in range(self.size):
            for j in range(i+1,self.size):
                if self.lis[j] < self.lis[i]:
                    self.swap(i,j)

    # 正宗的冒泡排序
    def BubbleSort(self):
        #相邻两个元素比较，将小的元素不断上移
        for i in range(self.size):
            for j in range(self.size-1,i,-1):
                if self.lis[j]<self.lis[j-1]:
                    self.swap(j,j-1)
            # 用于观察每次变化的结果
            # print('i:%d' % i)
            # self.print()

    # 改进版冒泡排序
    def BubbleSort2(self):
        flag = True
        for i in range(self.size):
            if flag == False:
                break
            flag = False
            for j in range(self.size-1,i,-1):
                if self.lis[j]<self.lis[j-1]:
                    self.swap(j,j-1)
                    flag = True
            # 用于观察每次变化的结果
            # 可以观察到最后两个i输出的结果是一样，这是因为最后一个检查完毕后，才发现没有变化，所以两个相同
            # print('i:%d' % i)
            # self.print()

# 简单选择排序
class Selection_Sort(Sort):
    def SelectSort(self):
        for i in range(self.size):
            min = i
            for j in range(i + 1, self.size):
                if self.lis[j] < self.lis[min]:
                    min = j
            if i != min:
                self.swap(i,min)
            # print('i:%d' % i)
            # self.print()

# 直接插入排序
class Insertion_Sort(Sort):
    def InsertSort(self):
        for i in range(1,self.size):
            if self.lis[i]<self.lis[i-1]:
                temp = self.lis[i]
                j = i-1
                while temp<self.lis[j] and j>=0:
                    self.lis[j+1]=self.lis[j]
                    j -= 1
                self.lis[j+1] = temp
            # print('i:%d' % i)
            # self.print()

# 希尔排序
class Shell_Sort(Sort):
    def ShellSort(self):
        increment = self.size
        while increment>1:
            increment = int(increment/3)
            for i in range(increment,self.size):
                if self.lis[i]<self.lis[i-increment]:
                    temp = self.lis[i]
                    j = i - increment
                    while j>=0 and self.lis[j]>temp:
                        self.lis[j+increment] = self.lis[j]
                        j -= increment
                    self.lis[j+increment] = temp

# 堆排序
class Heap_Sort(Sort):
    # 构建最大堆
    def HeapSort(self):
        # 构建最大堆
        i = int(self.size / 2) - 1  # 第一个非叶子节点
        while i >= 0:
            self.HeapAdjust(i, self.size - 1)  # 将从i到最后一个元素调整成最大堆
            i -= 1
        # 移除堆顶元素，构成新的序列
        j = self.size - 1
        while j>0:
            self.swap(0,j)#交换堆顶和最后的元素
            self.HeapAdjust(0, j - 1)#因为除了根节点外都是最大堆了，只需调整根节点来变成最大堆即可
            j -= 1

    # 堆调整，将从节点s到节点m调成最大堆
    def HeapAdjust(self,s=0,m=0):
        temp = self.lis[s]
        j = 2 * s + 1  # 左子树下标
        while j <= m:
            if j < m and self.lis[j] < self.lis[j + 1]:#如果j==m，说明只有左子树，所以不需要调整j
                j += 1
            if temp >= self.lis[j]:
                break
            else:
                self.lis[s] = self.lis[j]
                s = j
                j = j*2 + 1
        self.lis[s] = temp

# 归并排序
class Merging_Sort(Sort):
    def MergingSort(self):
        self.MSort(self.lis, self.lis, 0, self.size - 1)

    def MSort(self,SR,TR1,s,t):
        TR2 = [None] * self.size
        if s == t:
            TR1[s] = SR[s]
        else:
            m = int((s+t)/2)
            self.MSort(SR, TR2, s, m)
            self.MSort(SR, TR2, m + 1, t)
            self.Merge(TR2, TR1, s, m, t)

    def Merge(self,SR,TR,i,m,n):
        j = m+1
        k = i
        while i <= m and j <= n:
            if SR[i] < SR[j]:
                TR[k] = SR[i]
                i += 1
            else:
                TR[k] = SR[j]
                j += 1
            k += 1
        if i <= m:
            l = 0
            while l <= m-i:
                TR[k + l] = SR[i + l]
                l += 1
        if j <= n:
            l = 0
            while l <= n - j:
                TR[k + l] = SR[j + l]
                l += 1

# 在迭代的算法上，缓存空间上做了改进
# 在非迭代的算法上，没有书上的这么复杂，但思想上一致的，主要是在如何处理剩余元素上做了改动
# 若剩下的元素不能构成一个序列，则保留在原位置，不处理
# 若剩下的元素可以构成两个不完整的序列，则继续归并这两个序列。
class Merging_Sort_improve(Sort):# 在缓存空间上做了改进
    def MergingSort(self):
        temp = [None] * self.size#申请一个缓存空间，避免每次递归都产生新的空间
        self.MSort(temp, 0, self.size - 1)

    def MSort(self,temp,left,right):
        if left == right:
            temp[left] = self.lis[left]
        else:
            mid = int((left+right)/2)
            self.MSort(temp,left,mid)
            self.MSort(temp,mid+1,right)
            self.Merge(temp,left,mid,right)

    def Merge(self,temp,left,mid,right):
        # print(left,mid,right)
        # print('begin lis',self.lis)
        # print('begin temp',temp)
        i = left  # 左序列指针
        j = mid + 1  # 右序列指针
        k = 0  # 临时数组指针
        while i <= mid and j <= right:
            if self.lis[i] < self.lis[j]:
                temp[k] = self.lis[i]
                i += 1
            else:
                temp[k] = self.lis[j]
                j += 1
            k += 1
        while i <= mid:#说明右序列到头了，而左序列还有剩余，所以应该讲左序列的补充到tmep的后面
            temp[k] = self.lis[i]
            k += 1
            i += 1
        while j <= right:
            temp[k] = self.lis[j]
            k += 1
            j += 1
        # 将temp中的元素复制到原来的数组中
        k = 0
        while left <= right:
            self.lis[left] = temp[k]
            left += 1
            k += 1
        # print('end temp', temp)
        # print('end lis',self.lis)

    # 非递归版本
    def MergingSort2(self):
        TR = [None] * self.size
        k = 1 # 表示相邻长度
        while k < self.size:
            self.MergePass(TR, k, self.size - 1)
            k = 2*k

    def MergePass(self,TR,k,n):
        i = 0
        while i <= self.size - 2 * k: # 因为i+2k<self.size，不能越界
            self.Merge(TR,i,i+k-1,i+2*k-1)
            i += 2 * k
        # 若剩下两个不完整的序列，将其归并
        # 若剩下一个序列，则不处理。
        if i + k - 1 < n:  # 说明剩下2个序列，将其归并
            self.Merge(TR,i,i+k-1,n)


# 快速排序
class Quick_Sort(Sort):
    def QuickSort(self):
        self.QSort(0, self.size - 1)

    def QSort(self, low, high):
        if low < high:
            pivot = self.Partition(low, high)
            self.QSort(low, pivot - 1)
            self.QSort(pivot + 1, high)

    def Partition(self, low, high):
        pivotkey = self.lis[low]
        while low < high:
            # self.lis[high]是一个比pivotkey大的值，所以应该放在pivotkey的右边
            while low < high and pivotkey <= self.lis[high]:
                high -= 1
            self.swap(low, high)
            while low < high and pivotkey >= self.lis[low]:
                low += 1
            self.swap(low, high)
        return low

    # 对快排进行改进
    def QuickSort_improve(self):
        self.QSort_improve(0, self.size - 1)

    def QSort_improve(self, low, high):
        # 优化小数组排序方案和采用尾递归
        # 若数组非常小，快排的效果不如直接插入排序
        # 有资料认为，这个划分为7或50比较合适
        MAX_LENGTH_INSERT_SORT = 7
        if (high - low) > MAX_LENGTH_INSERT_SORT:
            # 当大于MAX_LENGTH_INSERT_SORT时，用快排
            # 采用尾递归，减少堆栈的深度
            while low < high:
                pivot = self.Partition_improve(low, high)
                self.QSort_improve(low, pivot - 1)
                low = pivot + 1  # 把之前的if换为while，利用了low
        else:
            self.InsertionSort(low, high)

    def QSort_improve_2(self,low,high):
        if low < high:
            pivot = self.Partition_improve_2(low,high)
            if low < pivot[0]:
                self.Partition_improve_2(low,pivot[0])
            if high > pivot[1]:
                self.Partition_improve_2(pivot[1],high)

    def Partition_improve(self, low, high):
        # 对pivotkey进行三数取中，将中间值放在self.lis[low]
        mid = int((low + high) / 2)
        if self.lis[low] > self.lis[high]:
            self.swap(low, high)
        if self.lis[mid] > self.lis[high]:
            self.swap(mid, high)
        if self.lis[mid] > self.lis[low]:
            self.swap(low, mid)  # 此时self.lis[low]是三数中的中间值
        pivotkey = self.lis[low]  # 此时self.lis[low]是三数中的中间值

        # 优化不必要的交换
        temp = pivotkey  # 保存为临时标量，是否需要使用呢？直接用pivotkey是否可以？
        while low < high:
            while low < high and pivotkey <= self.lis[high]:
                high -= 1
            self.lis[low] = self.lis[high]  # 采用替换而不是交换
            while low < high and pivotkey >= self.lis[low]:
                low += 1
            self.lis[high] = self.lis[low]  # 采用替换而不是交换
        self.lis[low] = temp
        return low

    # 这里是优化当list里面有重复数字的情况，当list里面有重复数字，且是pivotkey的时候，
    # 首先将于pivotkey相等的值移动到两边，然后再将两边与pivotkey相等的值移动在pivotkey附近
    # 最后返回两个变量，分别用于接下来的递归
    # https://blog.csdn.net/hacker00011000/article/details/52176100
    def Partition_improve_2(self, low, high):
        temp = self.lis[low]
        left, right = low, high
        first, last = low, high
        while low < high:
            while low < high and self.lis[high] >= temp:
                if self.lis[high] == temp:
                    self.lis[high], self.lis[right] = self.lis[right], self.lis[high]
                    right -= 1
                high -= 1
            self.lis[low] = self.lis[high]
            while low < high and self.lis[low] <= temp:
                if self.lis[low] == temp:
                    self.lis[low], self.lis[left] = self.lis[left], self.lis[low]
                    left += 1
                low += 1
            lis[high] = lis[low]
        lis[low] = temp
        # 上面添加的部分，使与中心轴相等的值位于两边
        # 接下来会让两边的值移动到中心轴两边
        # 交换左边
        i = low - 1
        while first < left and self.lis[i] != temp:
            self.lis[i], self.lis[first] = self.lis[first], self.lis[i]
            first += 1
            i -= 1
        # 交换右边
        j = low + 1
        while last > right and self.lis[j] != temp:
            self.lis[j], self.lis[last] = self.lis[last], self.lis[j]
            last -= 1
            j += 1
        return [i, j]

    def InsertionSort(self, left, right):
        for i in range(left + 1, right + 1):
            if self.lis[i] < self.lis[i - 1]:
                temp = self.lis[i]
                j = i - 1
                while j >= left and temp < self.lis[j]:
                    self.lis[j + 1] = self.lis[j]
                    j -= 1
                self.lis[j + 1] = temp

if __name__ == '__main__':
    # 冒泡排序
    # sqList = Bubble_Sort([4,1,7,3,8,5,9,2,6])
    # # sqList.BubbleSort0()
    # # sqList.BubbleSort()
    # sqList.BubbleSort2()
    # sqList.print()

    # 简单排序
    # sqList = Selection_Sort([4, 1, 7, 3, 8, 5, 9, 2, 6])
    # sqList.SelectSort()
    # sqList.print()

    # 插入排序
    # sqList = Insertion_Sort([4, 1, 7, 3, 8, 5, 9, 2, 6])
    # sqList.InsertSort()
    # sqList.print()

    # 希尔排序
    # sqList = Shell_Sort([9,1,5,8,3,7,4,6,2])
    # sqList.ShellSort()
    # sqList.print()

    # 堆排序
    # sqList = Heap_Sort([50,10,90,30,70,40,80,60,20])
    # sqList.HeapSort()
    # sqList.print()

    # 归并排序
    # sqList = Merging_Sort_improve([50,10,90,30,70,40,80,60,20])
    # # sqList.MergingSort()#递归版本
    # sqList.MergingSort2()#非递归
    # sqList.print()

    # 快速排序
    import random
    a = random.sample(range(1000000),50000)
    sqList = Quick_Sort(a)
    # sqList.QuickSort()#普通版
    sqList.QuickSort_improve()#优化版快排
    sqList.print()

