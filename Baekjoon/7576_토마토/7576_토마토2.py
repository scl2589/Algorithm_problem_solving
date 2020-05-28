from collections import deque

def bfs(M, N, box):
    days = -1
    while q:
        days += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < M and 0 <= nj < N and box[ni][nj] == 0:
                    box[ni][nj] = 1
                    q.append([ni, nj])
    for u in box:
        if 0 in u:
            return -1
    return days


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, M = map(int, input().split())
box = [list(map(int, input().split())) for i in range(M)]
q = deque()
for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            q.append([i, j])

print(bfs(M, N, box))