N = int(input())
M = int(input())

G = [[] for _ in range(N+1)]
count = 0

def DFS(v):
    stack = []
    visited = []

    stack.append(v)
    while stack: 
        node = stack.pop(0)
        if node not in visited:
            visited.append(node)
            stack.extend(G[node])
    return visited


for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

result = DFS(1)
print(len(result)-1)
