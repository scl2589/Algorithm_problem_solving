# deque 사용 (708ms)
from collections import deque
def dfs(start, N):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            #작은 수 부터 배치
            stack.extend(sorted(graph[n], reverse=True))
    return visited

def bfs(start, N):
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            # 작은 수 부터 배치
            queue.extend(sorted(graph[n]))

    return visited

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(' '.join(map(str, dfs(V, N))))
print(' '.join(map(str, bfs(V, N))))




