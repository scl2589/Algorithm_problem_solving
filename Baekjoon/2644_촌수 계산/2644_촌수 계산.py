#실패


def dfs(start, end):
    if start == end:
        return visited
    
    stack.append(start)
    while stack:
        u = stack.pop(0)
        if u not in visited:
            visited.append(u)
            stack.extend(G[u])
            if u == end:
                return visited
    return -1



N = int(input())
start, end = map(int, input().split())
M = int(input())


#가족 관계 정립
G = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)

visited = []
stack = [start]
result = dfs(start, end)
print(result)