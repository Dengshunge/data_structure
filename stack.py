class Stack:
    def __init__(self,item=[]):
        self.item = []
        if len(item):
            for i in item:
                self.item.append(i)

    def push(self,item):
        self.item.append(item)

    def pop(self):
        data = self.item[-1]
        self.item.pop()
        return data

    def print(self):
        print(' '.join(map(str,self.item)))

#链栈节点
class Node:
    def __init__(self,data,p=None):
        self.data = data
        self.next = p

class Stack_Link:
    def __init__(self):
        self.head = None

    def create(self,data):
        self.head = Node(None)
        p = self.head
        for i in data:
            self.insert(i)

    def insert(self,item):#头插法
        p = self.head
        p.next = Node(item,p.next)

    def push(self,item):
        self.insert(item)

    def pop(self):
        p = self.head
        data = p.next.data
        p.next = p.next.next
        return data


    def print(self):
        p = self.head.next
        a = []
        while p != None:
            a.append(p.data)
            p = p.next
        print(' '.join(map(str,a)))

#顺序队列
class Queue:
    def __init__(self,data=[]):
        self.data = []
        if len(data):
            for i in data:
                self.data.append(i)

    def enqueue(self,item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def print(self):
        print(' '.join(map(str,self.data)))

    def size(self):
        return len(self.data)

#链式队列
class Queue_Link:
    def __init__(self,item=[]):
        self.head = Node(None)
        if len(item):
            for i in item:
                self.enqueue(i)

    def enqueue(self,item):#插入链尾
        p = self.head
        while p.next != None:
            p = p.next
        p.next = Node(item)

    def dequeue(self):
        res = self.head.next.data
        self.head.next = self.head.next.next
        return res

    def print(self):
        res = []
        p = self.head.next
        while p != None:
            res.append(p.data)
            p = p.next
        print(' '.join(map(str,res)))

if __name__ == '__main__':
    a = Queue_Link([1,2,3])
    a.enqueue(4)
    a.dequeue()
    a.print()
