#순환큐로 만든다면 아래와 같이 된다.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    front = 0
    rear = 0
    queue = [0] + list(map(int, input().split())
    rear = n
    qlen = n+1
    for _ in range(m):
        front = (front+1)%qlen #dequeue()
        t = queue[front]
        rear = (rear+1)%qlen