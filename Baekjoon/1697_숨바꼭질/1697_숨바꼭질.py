from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        u = q.popleft()
        if u == K:
            print(time[u])
            return
        for next_step in (u-1, u+1, u*2):
            if 0 <= next_step < num and not time[next_step]:
                time[next_step] = time[u] + 1
                q.append(next_step)
            

N, K = map(int, input().split())
num = 100001
time = [0] * num
bfs()