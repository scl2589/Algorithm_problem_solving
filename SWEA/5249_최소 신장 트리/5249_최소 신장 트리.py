import heapq
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append([n2, w])
        adj[n2].append([n1, w])
        
    key = [float('inf')] * (V+1)
    mst = [False] * (V+1)
    pq = []

    key[0] = 0
    heapq.heappush(pq, (0, 0 ))
=
    result = 0
    while pq:
        k, node = heapq.heappop(pq)
        if mst[node]:
            continue
        mst[node] = True
        result += k
        for dest, wt in adj[node]:
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest))
    print(f'#{tc} {result}')
                