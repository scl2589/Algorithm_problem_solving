N = int(input())
G = [[] for _ in range(N+1)]
visited = [[] for _ in range(N+1)]
#트리를 그래프 형태로 생성
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

#DFS 실행
def dfs(G, start, visited):
    stack = [start]

    while stack: 
        node = stack.pop()
        for i in G[node]:
            visited[i].append(node)
            stack.append(i)
            G[i].remove(node)
    return visited

result = dfs(G, 1, visited)[2:]
for i in result:
    print(*i)

