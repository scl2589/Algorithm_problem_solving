def dfs(n, k, c):
    global maxV
    if maxV < c+1:
        maxV = c+1
    visited[n] = 1
    for i in range(1, k+1):
        if i in G[n] and visited[i] == 0:
            dfs(i, k, c+1)
    visited[n] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[0] for _ in range(N+1)]
    visited=[0] * (N+1)
    maxV = 0
    for _ in range(M):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)
    for i in range(1, N+1):
        dfs(i, N, 0)
    print('#{} {}'.format(tc, maxV))