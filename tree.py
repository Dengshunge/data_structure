class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self,root = None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def preOrder(self,BinaryTreeNode):#前序
        if BinaryTreeNode == None:
            return
        print(BinaryTreeNode.data,end=' ')
        self.preOrder(BinaryTreeNode.left)
        self.preOrder(BinaryTreeNode.right)

    def inOrder(self,BinaryTreeNode):#中序
        if BinaryTreeNode == None:
            return
        self.inOrder(BinaryTreeNode.left)
        print(BinaryTreeNode.data,end=' ')
        self.inOrder(BinaryTreeNode.right)

    def postOrder(self,BinaryTreeNode):#后序
        if BinaryTreeNode == None:
            return
        self.postOrder(BinaryTreeNode.left)
        self.postOrder(BinaryTreeNode.right)
        print(BinaryTreeNode.data,end=' ')

    # 非递归前序遍历
    # 当p非空或stack非空时，输出p.data并将p压入stack，遍历左子树
    # 当无左子树时，弹出stack，遍历该节点的右子树
    def preOrder1(self):
        if self.root == None:
            return
        stack = []
        p = self.root
        while p != None or stack:
            while p != None:
                print(p.data,end=' ')
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop().right

    # 非递归中序遍历
    # 先将p和左子树压入stack，当p为空时，弹出stack并输出数据，转而将p变为右子树
    def inOrder1(self):
        if self.root == None:
            return
        stack = []
        p = self.root
        while p != None or stack:
            while p != None:
                stack.append(p)
                p = p.left
            if stack:
                s = stack.pop()
                print(s.data,end=' ')
                p = s.right

    # 非递归后序遍历
    # 只有当左子树和右子树都被访问了，才能访问根节点
    # 当当前根节点右子树和per相等时，说明已经可以访问该根节点了
    # https://blog.csdn.net/qq_33951180/article/details/52687692
    def postOrder1(self):
        if self.root == None:
            return
        stack = []
        p,per = self.root,None
        while p != None or stack:
            while p != None:
                stack.append(p)
                p = p.left
            top = stack[-1]
            if top.right == None or top.right == per:
                # 只有当右子树被访问或者当前结点的右子树为空时，才能访问根节点
                print(top.data,end=' ')
                per = top
                stack.pop()
            else:
                p = top.right

if __name__ == '__main__':
    #先创建叶节点
    n17 = BinaryTreeNode('k')
    n15 = BinaryTreeNode('j')
    n12 = BinaryTreeNode('i')
    n8 = BinaryTreeNode('h',right=n17)
    n7 = BinaryTreeNode('g',right=n15)
    n6 = BinaryTreeNode('f',left=n12)
    n5 = BinaryTreeNode('e')
    n4 = BinaryTreeNode('d',left=n8)
    n3 = BinaryTreeNode('c',left=n6,right=n7)
    n2 = BinaryTreeNode('b',left=n4,right=n5)
    root = BinaryTreeNode('a',left=n2,right=n3)

    bt = BinaryTree(root)
    print('前序')
    bt.preOrder(bt.root)
    print()
    bt.preOrder1()
    print('中序')
    bt.inOrder(bt.root)
    print()
    bt.inOrder1()
    print('后序')
    bt.postOrder(bt.root)
    print()
    bt.postOrder1()

