from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        i, j = q.popleft()
        farm[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and farm[ni][nj]==1:
                farm[ni][nj] = 0
                q.append((ni, nj))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    count = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                count += 1
                bfs(i, j)
    print(count)