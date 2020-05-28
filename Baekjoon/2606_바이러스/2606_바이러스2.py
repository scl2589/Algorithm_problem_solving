from collections import deque

def bfs(start):
    visited = []
    q = deque()
    q.append(start)
    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            q.extend(graph[n])
    return visited


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(len(bfs(1))-1)