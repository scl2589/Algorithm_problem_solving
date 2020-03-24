#bfs
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(input()) for _ in range(n)]
apt = []

def bfs(i, j):
    q = deque()
    q.append((i, j))
    a[i][j] = '0'
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if a[nx][ny] == '1':
                a[nx][ny] = '0'
                cnt += 1
                q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            apt.append(bfs(i, j))

print(len(apt))
apt.sort()
for i in apt:
    print(i)


출처: https://rebas.kr/652 [PROJECT REBAS]