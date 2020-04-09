class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
class LinkedList:
    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node
        
        self.before = None
        self.current = None
        
    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node
        
    def move_to(self,D):
        self.current = self.head.link
        self.before = self.head
        for _ in range(D):
            if self.current == None:
                return False  # 실패
            self.before = self.current
            self.current = self.current.link
        return True  # 성공
        
    def insert(self, idx, data):
        new_node = Node(data)
        self.move_to(idx)
        self.before.link = new_node
        new_node.link = self.current
    
    def delete(self, idx):
        self.move_to(idx)
        self.before.link = self.current.link

    def change(self, idx, data):
        self.move_to(idx)
        self.current.data = data

    def my_result(self, idx):
        if self.move_to(idx):
            return self.current.data
        else:
            return -1

T = int(input())
for test_case in range(1, 1 + T):
    N, M, L = map(int, input().split())
    Seq = LinkedList()
    for i in map(int, input().split()):
        Seq.append(i)
    for _ in range(M):
        data = list(input().split())
        if data[0] == 'I':
            Seq.insert(int(data[1]), int(data[2]))
        elif data[0] == 'D':
            Seq.delete(int(data[1]))
        elif data[0] == 'C':
            Seq.change(int(data[1]), int(data[2]))
    print('#{} {}'.format(test_case, Seq.my_result(L)))