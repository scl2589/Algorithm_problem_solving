from collections import deque

def bfs(n):
    cnt = 0
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        n = q.popleft()
        for w in G[n]:
            if not visited[w]:
                visited[w] = visited[n] + 1
                if visited[w] ==2 or visited[w] == 3:
                    q.append(w)
                    cnt += 1
    return cnt
    
                    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    visited = [0] * (N+1)
    print(f'#{tc} {bfs(1)}')