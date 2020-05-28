from collections import deque

def bfs(i, j):
    q = deque()
    q.append([i, j])
    while q:
        i, j = q.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj <M and arr[ni][nj]=='1' and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])
                


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
print(bfs(0, 0))