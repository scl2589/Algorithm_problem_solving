def bfs(start, end):
    global result
    q.append(start)
    visited[start] = 1

    while q:
        start = q.pop(0)
        for new in range(1, V+1):
            if graph[start][new] and not visited[new]:
                q.append(new)
                visited[new] = 1
                distance[new] = distance[start] + 1
                if new == end:
                    result = distance[new]
                    return
    return


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    distance = [0] * (V+1)
    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1][n2]=1
        graph[n2][n1]=1

    start, end = map(int, input().split())
    q= []
    result = 0
    bfs(start, end)
    print('#{} {}'.format(tc, result))