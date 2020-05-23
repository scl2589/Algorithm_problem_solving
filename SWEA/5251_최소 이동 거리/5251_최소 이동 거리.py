# dist, selected 배열 준비
# 시작점 선택
# 모든 정점이 선택될 때 까지
# 아직 선택되지 않고 dist의 값이 최소인 정점 :u
# 정점 u의 최단거리 결정
# 정점 u에 인접한 정점에 대해서 간선완화
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = {i:[] for i in range(N+1)}

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])

    dist = [float('inf')] * (N+1)
    selected = [False] * (N+1)

    dist[0] = 0
    cnt = 0
    while cnt < N+1:
        # dist가 최소인 정점 찾기 
        minV = float('inf')
        u = -1
        for i in range(N+1):
            if not selected[i] and dist[i] < minV:
                minV = dist[i]
                u = i
        # 결정
        selected[u] = True
        cnt += 1
        # 간선 완화
        for w, cost in adj[u]:  #도착 정점, 가중치 
            dist[w] = min(dist[w], dist[u]+cost)
    print(f'#{tc} {dist[N]}')