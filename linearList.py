#顺序表
class myList:
    def __init__(self,max=10):
        self.max = max
        self.num = 0
        self.__List = []

    def prepend(self,elem):
        if self.num > self.max:
            print('The list is full')
            return
        self.__List.append(elem)
        self.num += 1

    def insert(self,elem,i):
        if self.num > self.max:
            print('The list is full')
            return
        if i > self.num:
            print('insert index error')
            return
        self.__List.insert(i,elem)
        self.num += 1

    def __getitem__(self, i):
        if i >= self.num:
            print('index error')
            return
        return self.__List[i]

    def __setitem__(self, i, elem):
        if i >= self.num or i < 0:
            print('index error')
            return
        self.__List[i] = elem

    def pop(self,i):
        if i >= self.num or i <0:
            print('pop error')
            return
        self.__List.pop(i)
        self.num -=1

    def show(self):
        print(self.__List)

#单链表
class Node:
    #单链表节点
    def __init__(self,data,p=None):
        self.data = data
        self.next = p                                                                                                                                              = p

class LinkList:
    def __init__(self):
        self.head = None

    def create(self,data):
        if len(data) == 0:
            print('list is null')
            return
        self.head = Node(data[0])
        p = self.head#将p指向头节点,p的类型为Node
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    def print(self):
        p = self.head
        while p != None:
            print(p.data)
            p = p.next

    def len(self):
        p = self.head
        length = 0
        while p !=None:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        return self.len() == 0

    def append(self,item):
        p = self.head
        while p.next != None:
            p = p.next
        p.next = Node(item)

    def insert(self,index,item):
        #在index之前插入
        if index > self.len() or index<0:
            print('insert index error')
            return
        if index == 0:
            self.head = Node(item,self.head)
            return
        p = self.head
        n = 0
        while n < (index-1):
            p = p.next
            n += 1
        if index == self.len():
            p.next = Node(item)#插入最后
        else:
            p.next = Node(item,p.next)#插入中间

    def delete(self,index):
        if index >= self.len() or index < 0:
            print('delete index error')
            return
        if index == 0:
            self.head = self.head.next
        else:
            p = self.head
            n = 0
            while n < index-1:
                p = p.next
                n += 1
            p.next = p.next.next

if __name__ == '__main__':
    a = LinkList()
    a.create([10,15,20])
    a.append(25)
    a.insert(4,30)
    a.delete(0)
    a.print()
    print(a.head.data)