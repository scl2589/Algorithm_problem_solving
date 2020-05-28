import sys
from collections import deque

def bfs(start):
    global visited
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        if not visited[a]:
            visited[a] = 1
            q.extend(graph[a])

N, M = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)