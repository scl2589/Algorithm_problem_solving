


def dfs(n, end, count):
    if n == end:
        return visited
    
    if count == N-1:
        return visited

    for i in range(N):
        if i in G[n] and not visited[i]:
            visited[i] = 1
            dfs(i, end, count+1)


N = int(input())
start, end = map(int, input().split())
M = int(input())


#가족 관계 정립
G = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)

visited = [0 for _ in range(N+1)]
visited[start] = 1
dfs(start, end, 0)
print(visited)
print(sum(visited))