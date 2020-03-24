def dfs(V, start, end):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        visited.append(n)
        if n == end:
            return 1
        for k in G[n]:
            if k not in visited:
                stack.append(k)
                n = k
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
    start, end = map(int, input().split())
    print('#{} {}'.format(tc, dfs(V, start, end)))
    