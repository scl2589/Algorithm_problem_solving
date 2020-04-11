def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)
# 노드 삭제
def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link
# 가운데 노드로 삽입
def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
# 첫번째 노드 삽입
def addtoFirst(data):
    global Head
    Head = Node(data, Head)
class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n

T = int(input())
for tc in range(T):
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))  

    Head = None
    addtoFirst(numbers[0])

    for node in numbers[1:]:
        addtoLast(node)

    for _ in range(M - 1):
        temp_numbers = list(map(int, input().split()))
        pre = Head  
        while pre.link != None:
            if pre.link.item > temp_numbers[0]: 
                break
            pre = pre.link

        if pre == Head:  
            addtoFirst(temp_numbers[0])
            pre = Head  
            for item in temp_numbers[1:]:
                add(pre, item)
                pre = pre.link
        else:
            for item in temp_numbers:
                add(pre, item)
                pre = pre.link

    pre = Head
    ans = [0] * N * M
    ind = 0
    while pre.link != None:
        ans[ind] = pre.item
        pre = pre.link
        ind += 1
    ans[ind] = pre.item  
    # 출력
    print("#{} {}".format(tc + 1, ' '.join(list(map(str, ans[::-1][:10])))))
