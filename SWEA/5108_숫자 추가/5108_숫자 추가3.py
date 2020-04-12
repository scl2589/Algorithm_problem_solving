class Node:
    def __init__(self, data=0, n = None):
        self.data = data
        self.next = n


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insertLast(self,node):
        if self.head is None: #빈 리스트
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def insertFirst(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insertAt(self, idx, node):
        if self.head is None or idx==0: #빈리스트일 경우, idx==0
            self.insertFirst(node)
        elif idx >= self.size:
            self.insertLast(node)
        else:
            pre, cur = None, self.head
            for _ in range(idx-1):
                pre = cur
                cur = cur.next
                self.size += 1

    def printidx(self, idx):
        cur = self.head
        for _ in range(idx):
            cur = cur.next
        return cur.data


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    mylist = LinkedList()
    for i in range(N):
        mylist.insertLast(Node(lst[i]))
    for _ in range(M):
        a, b = map(int,input().split())
        mylist.insertAt(a, b)
    print('#{} {}'.format(tc, mylist.printidx(L)))