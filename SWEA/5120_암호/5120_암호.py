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
        
        self.num_of_data = 0
        
    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node
        self.tail.link = self.head.link # 첫 요소와 끝을 연결
        self.num_of_data += 1
        
    def first(self):
        self.current = self.head.link
        self.before = self.tail
        return self.current.data
        
    def next(self):
        self.before = self.current
        self.current = self.current.link
        return self.current.data
        
    def insert(self, data):
        new_node = Node(data)
        self.before.link = new_node
        new_node.link = self.current
        self.current = new_node # current 갱신
        self.num_of_data += 1
    
    def my_func(self, D):
        for _ in range(D):
            self.next()
        num = self.before.data + self.current.data
        self.insert(num)
        
    def my_result(self):
        lst = [self.first()]
        for _ in range(self.num_of_data - 1):
            lst.append(self.next())
        # 마지막 10자리까지 출력
        return ' '.join(map(str, lst[-1:-11:-1]))

T = int(input())
for test_case in range(1, 1 + T):
    N, M, K = map(int, input().split())
    Seq = LinkedList()
    for i in map(int, input().split()):
        Seq.append(i)
    Seq.first()
    for _ in range(K):
        Seq.my_func(M)
    print('#{} {}'.format(test_case, Seq.my_result()))