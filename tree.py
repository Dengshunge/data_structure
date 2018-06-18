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
        print(BinaryTreeNode.data)
        self.preOrder(BinaryTreeNode.left)
        self.preOrder(BinaryTreeNode.right)

    def inOrder(self,BinaryTreeNode):#中序
        if BinaryTreeNode == None:
            return
        self.inOrder(BinaryTreeNode.left)
        print(BinaryTreeNode.data)
        self.inOrder(BinaryTreeNode.right)

    def postOrder(self,BinaryTreeNode):#后序
        if BinaryTreeNode == None:
            return
        self.postOrder(BinaryTreeNode.left)
        self.postOrder(BinaryTreeNode.right)
        print(BinaryTreeNode.data)

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
    print('中序')
    bt.inOrder(bt.root)
    print('后序')
    bt.postOrder(bt.root)

