# 折半查找
def Binart_Search(a=[], n=0):
    if len(a) == 0:
        return False
    low = 0
    high = len(a) - 1
    time = 0
    while low <= high:
        time += 1
        mid = int((low + high) / 2)
        if n == a[mid]:
            print('time: ', time)
            return mid
        elif n < a[mid]:
            high = mid - 1
        elif n > a[mid]:
            low = mid + 1
    return False


# 插值查找
def Binart_Search_chazhi(a=[], n=0):
    if len(a) == 0:
        return False
    low = 0
    high = len(a) - 1
    time = 0
    while low <= high:
        time += 1
        # 下面一行是重点，更换了系数
        mid = low + int(((n - a[low]) / (a[high] - a[low])) * (high - low))
        if mid > high or mid < low:
            return False
        if n == a[mid]:
            print('time: ', time)
            return mid
        elif n < a[mid]:
            high = mid - 1
        elif n > a[mid]:
            low = mid + 1
    return False


# 斐波那契查找
def Fibonacci_Search(a=[], n=0):
    # 首先生成菲波那切数列
    F = [1, 1]
    # 其最大元素的值必须超过查找表中元素个数的数值
    while F[-1] < len(a):
        F.append(F[-1] + F[-2])
    # 下面是查找过程
    b = a[:]
    low = 0
    high = len(b) - 1
    k = 0
    while high > (F[k] - 1):
        k += 1
    i = high
    while i < (F[k] - 1):  # 将不满的数值补全
        b.append(b[-1])
        i += 1
    while low <= high:
        mid = low + F[k - 1] - 1
        if n < b[mid]:
            high = mid - 1
            k -= 1
        elif n > b[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                return mid
            else:
                return high
    return False


# 二叉树查找
import tree
class BinarySortTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        # 二叉树查找
        # 返回查找到最后的节点和值
        p = self.root
        q = p
        while p:
            val = p.data
            q = p
            if key < val:
                p = p.left
            elif key > val:
                p = p.right
            else:  # key==val
                return p, val
        return q, None

    def insert(self, key):
        # 插入操作
        bt = self.root
        if not bt:
            self.root = tree.BinaryTreeNode(data=key)
            return True
        per, p = self.search(key=key)
        if p:
            # 当p非空，说明存在该元素，所以不需要插入
            print('该元素%d存在，不需要插入' % key)
            return False
        else:
            # 当p为空时，说明不存在该元素，而per指向当前节点
            if key < per.data:
                per.left = tree.BinaryTreeNode(data=key)
            else:
                per.right = tree.BinaryTreeNode(data=key)
            return True

    def delete(self, key):
        p, q = None, self.root  # p为q的父节点
        if q == None:
            print('空树')
            return
        # 如果存在该结点，则q指向该结点，p指向该结点的父节点
        while q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if not q:  # 说明未找到key
                print('没有此元素')
                return
        if q.right == None:#当前结点的右子树为空
            if q is p.left:#q为p的左子树
                p.left = q.left
            else:#q为p的右子树
                p.right = q.left
        elif q.left == None:#当前结点的左子树为空
            if q is p.left:
                p.left = q.right
            else:
                p.right = q.right
        else:#左右子树都不为空
            r1, r2 = q, q.left  # r1为r2的父结点
            while r2.right:  # 最大值
                r1, r2 = r2, r2.right
            q.data = r2.data
            if r2 is r1.right:
                r1.right = r2.left
            else:
                r1.left = r2.left

    def inOrder(self, BinaryTreeNode):  # 中序
        # 中序遍历数组
        if BinaryTreeNode == None:
            return
        self.inOrder(BinaryTreeNode.left)
        print(BinaryTreeNode.data)
        self.inOrder(BinaryTreeNode.right)

    def __iter__(self):
        # 另一种方法进行中序遍历，利用了迭代器和生成器，值得学习一下
        # 实现二叉树的中序遍历算法,展示我们创建的二叉排序树.直接使用python内置的列表作为一个栈。
        stack = []
        node = self.root
        while node or stack:  # 当node或者栈非空的情况下，说明还有元素
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()  # 左子树的最下面一个元素出队
            yield node.data  # 利用生成器
            node = node.right  # 遍历此节点的右子树,若有子树为空，但栈没空，还会继续循环

    def TreeDepth(self , pRoot):
        if pRoot == None:
            return 0;
        lDepth =  self.TreeDepth(pRoot.left);
        rDepth =  self.TreeDepth(pRoot.right);
        return max(lDepth , rDepth) + 1

# 平衡二叉树
class BiTNode:
    def __init__(self,data=None,bf=0,left=None,right=None):
        self.data = data
        self.bf = bf
        self.left = left
        self.right = right

class AVL_Tree:
    def __init__(self):
        self.root = None

    def search(self, key):
        # 二叉树查找
        # 返回查找到最后的节点和值
        p = self.root
        q = p
        while p:
            val = p.data
            q = p
            if key < val:
                p = p.left
            elif key > val:
                p = p.right
            else:  # key==val
                return p, val
        return q, None

    def R_Rotate(self,P):#右旋
        L = P.left
        P.left = L.right
        L.right = P
        return L

    def L_Rotate(self,P):#左旋
        R = P.right
        P.right = R.left
        R.left = P
        return R

    def LeftBalance(self,BiTNode):#左平衡旋转
        L = BiTNode.left
        if L.bf == 1:#说明结点插入在L的左子树上
            L.bf = BiTNode.bf = 0
            self.R_Rotate(BiTNode)
        elif L.bf == -1:#说明结点插入在L的右子树上
            Lr = L.right
            if Lr.bf == 1:
                BiTNode.bf = -1
                L.bf = 0
            elif Lr.bf == 0:
                BiTNode.bf = L.bf = 0
            else:#Lr.bf == -1
                BiTNode.bf = 0
                L.bf = -1
            Lr.bf = 0
            self.L_Rotate(L)
            self.R_Rotate(BiTNode)
        else:
            print('LeftBalance error')
            print('L.bf==0')
            return

    def RightBalance(self,BiTNode):#右平衡旋转
        R = BiTNode.right
        if R.bf == -1:#说明结点插入在R的右子树上
            R.bf = BiTNode.bf = 0
            self.L_Rotate(BiTNode)
        elif R.bf == 1:#说明结点插入在L的左子树上
            Rl = R.left
            if Rl.bf == 1:
                BiTNode.bf = 0
                R.bf = -1
            elif Rl.bf == 0:
                BiTNode.bf = R.bf = 0
            else:#Rl.bf == -1
                BiTNode.bf = 1
                R.bf = 0
            Rl.bf = 0
            self.R_Rotate(R)
            self.L_Rotate(BiTNode)
        else:
            print('RightBalance error')
            print('R.bf==0')
            return

    def InsertAVL(self,p,key,taller):
        if not p:
            p = BiTNode(data=key)
            taller = True
        else:
            if p.data == key:
                taller = False
                return False
            if p.data>key:
                if not self.InsertAVL(p.left,key=key,taller=taller):
                    return False
                if taller:
                    if p.bf == 1:
                        self.LeftBalance(p)
                        taller = False
                    elif p.bf == 0:
                        p.bf = 1
                        taller = True
                    else:#p.bf == -1
                        p.bf = 0
                        taller = True
            else:#p.data<key
                if not self.InsertAVL(p.right,key=key,taller=taller):
                    return False
                if taller:
                    if p.bf == 1:
                        p.bf =0
                        taller = False
                    elif p.bf == 0:
                        p.bf = -1
                        taller = True
                    else:#p.bf == -1
                        self.RightBalance(p)
                        taller = False
        return True

    def InsertAVL1(self,key):
        bt = self.root
        if not bt:
            self.root = BiTNode(key)
            return True
        # while


        per,p = self.search(key)
        if p:#该元素已经存在
            print('该元素已经存在')
            return False
        else:
            pass

    def InsertAVL2(self,p,key,taller):
        if self.root == None:
            self.root = BiTNode(key)
            return True
        if not p:
            p = BiTNode(data=key)
            taller = True
        else:
            if p.data == key:
                taller = False
                return False
            if p.data>key:
                if not self.InsertAVL2(p.left,key=key,taller=taller):
                    return False
                if taller:
                    if p.bf == 1:
                        self.LeftBalance(p)
                        taller = False
                    elif p.bf == 0:
                        p.bf = 1
                        taller = True
                    else:#p.bf == -1
                        p.bf = 0
                        taller = True
            else:#p.data<key
                if not self.InsertAVL2(p.right,key=key,taller=taller):
                    return False
                if taller:
                    if p.bf == 1:
                        p.bf =0
                        taller = False
                    elif p.bf == 0:
                        p.bf = -1
                        taller = True
                    else:#p.bf == -1
                        self.RightBalance(p)
                        taller = False
        return True




    def TreeDepth(self , pRoot):
        if pRoot == None:
            return 0;
        lDepth =  self.TreeDepth(pRoot.left);
        rDepth =  self.TreeDepth(pRoot.right);
        return max(lDepth , rDepth) + 1

    def __iter__(self):
        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.data
            node = node.right



if __name__ == '__main__':
    # a = list(range(0,100,1))
    # n = 40

    # 折半查找
    # Binart_Search(a, n)

    # 插值查找
    # x = Binart_Search_chazhi(a,n)
    # print(x)

    # 斐波那契查找
    # xx = Fibonacci_Search(a,n)
    # print(xx)

    # # 二叉树查找
    # lis = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
    # bs_tree = BinarySortTree()
    # for i in lis:
    #     bs_tree.insert(i)
    # # bs_tree.inOrder(bs_tree.root)#利用迭代读取
    # for n in bs_tree:
    #     print(n, end=' ')  # 利用迭代器读取
    # print('\n')
    # print(bs_tree.TreeDepth(bs_tree.root))

    # # 二叉树删除
    # bs_tree.delete(62)
    # for n in bs_tree:
    #     print(n, end=' ')  # 利用迭代器读取

    # AVL树，未写完
    # lis = [3, 2, 1,4,5,6,7,10,9,8]
    # bs_tree = AVL_Tree()
    # taller = True
    # for i in lis:
    #     bs_tree.InsertAVL2(bs_tree.root,i,taller)
    # for n in bs_tree:
    #     print(n, end=' ')  # 利用迭代器读取
    pass