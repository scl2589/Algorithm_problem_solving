from collections import deque
def bfs(n):
    queue = deque([n])
    while queue:
        n = queue.popleft()
        if n == M:
            return visited[n]
        for calc in [n + 1, n - 1, n * 2, n - 10]:
            if 0 <= calc <= 1000000 and not visited[calc]:
                queue.append(calc)
                visited[calc] = visited[n]+1
    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0]*1000001
    minV = float('inf')
    res = bfs(N)
    print(f'#{tc} {res}')

"""
BFS
- 큐 생성
- 방문기록 생성
- 시작점 인큐
- 시작점 방문 표시
- 큐가 비어있지 않으면 반복
    t = 디큐
    t가 목표인 경우 중단
    t에 인접이고, 미방문인 i가 있으면 인큐 i, i에 방문표시
"""